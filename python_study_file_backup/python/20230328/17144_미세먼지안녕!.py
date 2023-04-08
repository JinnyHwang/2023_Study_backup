'''
https://www.acmicpc.net/problem/17144

RxC 격자
r,c에 있는 미세먼지양 실시간 체크

1부터 numbering되어 있음

R*C -> r,c 좌표는 r-1, c-1로 사용

공청기좌표 (0,a)(0,a+1)

1. 미세먼지의 확산
모든 칸에서 동시에 일어남
(r,c)에 있는 미세먼지는 인접한 4개 방향으로 확산됨
인접방향에 공청기 or 벽 확산 x
빈칸으로만 확산이 일어남 미먼//5 만큼
남은 미먼 = 미먼 - (미먼//5)*(확산개수)

2. 공청기 작동
(0,a): 반시계 순환
(0,a+1): 시계 순환
바람 방향대로 한 칸씩 이동함
공청기 안으로 들어간 미세먼지는 사라짐
'''

def map_print(imap):
    for i in imap:
        print(i)
    print()

# 공청기로 들어오는 칸 부터 옮기기
# 탐색방향
ud = [(-1,0),(0,1),(1,0),(0,-1)]
def up_air_move(ar):
    i = 0
    r,c = ar,0
    while(True):  
        nr, nc = r+ud[i][0], c+ud[i][1]
        if (0 <= nr < R and 0 <= nc < C) == False: #격자를 벗어나면 방향전환, 다시 계산
            i = (i+1)%4
            nr, nc = r+ud[i][0], c+ud[i][1]
        elif (nr,nc) == (ar+1, C-1): # 방향 꺽기
            i = (i+1)%4
            nr, nc = r+ud[i][0], c+ud[i][1]
        
        if room[r][c] != -1:
            room[r][c] = room[nr][nc]
        
        # 다시 원점으로 돌아오면 break
        if (nr,nc) == (ar,1):
            room[nr][nc] = 0 # 미먼 없애고 순환 끝
            break
        
        r,c = nr,nc
        
        
dd = [(1,0),(0,1),(-1,0),(0,-1)]
def down_air_move(ar):
    i = 0
    r,c = ar,0
    while(True):
        nr, nc = r+dd[i][0], c+dd[i][1]
        if (0 <= nr < R and 0 <= nc < C) == False: #격자를 벗어나면 방향전환, 다시 계산
            i = (i+1)%4
            nr, nc = r+dd[i][0], c+dd[i][1]
        elif (nr,nc) == (ar-1, C-1): # 방향 꺽기
            i = (i+1)%4
            nr, nc = r+dd[i][0], c+dd[i][1]
        
        if room[r][c] != -1:
            room[r][c] = room[nr][nc]
        
        # 다시 원점으로 돌아오면 break
        if (nr,nc) == (ar,1):
            room[nr][nc] = 0 # 미먼 없애고 순환 끝
            break
        
        r,c = nr,nc


R, C, T = map(int, input().split())

room = []
air = []

for r in range(R):
    room.append(list(map(int, input().split())))
    for c in range(C):
        if room[r][c] == -1:
            air.append(r)
            
#map_print(room)
#print(air)

'''        
up_air_move(air[0][0])
map_print(room)

down_air_move(air[1][0])
map_print(room)
'''

for _ in range(T):
    
    # 미세먼지 확산
    next_room = [ [0 for _ in range(C)] for _ in range(R)]
    next_room[air[0]][0], next_room[air[1]][0] = -1, -1
    #map_print(next_room)
    
    for r in range(R):
        for c in range(C):
            # 미세먼지 확산
            if room[r][c] > 0:
                cnt = 0
                nl = []
                for dr, dc in ud:
                    nr, nc = r+dr, c+dc
                    if 0 <= nr < R and 0 <= nc < C and room[nr][nc] != -1:
                        cnt += 1
                        nl.append((nr,nc))
                
                for _ in range(cnt):
                    nr, nc = nl.pop()
                    next_room[nr][nc] += (room[r][c])//5
                
                next_room[r][c] += room[r][c] - ((room[r][c])//5)*cnt
                
    #map_print(next_room)
    room = next_room
    #map_print(room)
    
    
    # 공청기 순환
    up_air_move(air[0])
    #map_print(room)
    
    down_air_move(air[1])
    #map_print(room)
    
hap = 0
for r in room:
    hap += sum(r)
    
print(hap+2)

