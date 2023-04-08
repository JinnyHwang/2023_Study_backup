
from copy import deepcopy

d = [ (-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1) ]




def shark_move(arr, x, y, shark_pos):
    
    sd = arr[x][y][1]-1
    # 4*4 배열이기 때문
    for i in range(1,4):
        nx = x + d[sd][0]*i
        ny = y + d[sd][1]*i
        #print(nx,ny,sd)
        
        # next 좌표가 range 안이고, 물고기가 있으면 상어가 갈 수 있는 좌표
        if (0 <= nx < 4 and 0 <= ny < 4) and arr[nx][ny][0] != 0:
            shark_pos.append( [nx,ny] )



def find_fish(arr, num):
    #print(arr)
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == num:
                return [i, j]
    return [-1,-1]


def fish_move(arr, x, y):
    
    position = []
    
    # 1 ~ 16번 확인
    for num in range(1, 17):
        # 지금 탐색하는 i번 물고기 어디있는지 확인
        position = find_fish(arr, num)
        
        # 해당 번호 물고기 없음 다음으로
        if position[0] == -1:
            continue
        
        i = position[0]
        j = position[1]
        
        # 배열 index 값은 방향 값-1
        nd = arr[i][j][1]-1
        
        for _ in range(8):
            ni = i + d[nd][0]
            nj = j + d[nd][1]
            
            if 0 <= ni < 4 and 0 <= nj < 4:
                # 상어가 아니면 change
                if arr[ni][nj][0] != -1:
                    # 물고기의 방향 값을 최신으로 update
                    arr[i][j][1] = nd+1 # 방향값은 인덱스값+1
                    # i,j와 ni,nj 치환
                    arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
                    break
            # 조건에 충족 못하면 방향 바꿈 (0~7) 
            nd = (nd+1)%8 
        


# 상어 이동
# 상어 좌표
def bfs(fish_map, x, y, total):
    
    global answer
    
    # 해당 turn에서 쓸 리스트
    arr = deepcopy(fish_map)
    
    # 지금 상어 위치
    # 먹은 물고기 num에 저장
    num = arr[x][y][0]
    # 상어 -1로 변경
    arr[x][y][0] = -1
    #print(arr)
    
    #print(total,'\n',fish_map,'\n',arr)
    
    answer = max(answer, total+num)
    
    # 상어가 물고기를 먹었으니
    # 물고기 이동
    fish_move(arr, x, y)
    #print(arr)
    
    # 상어 이동 경우의 수
    shark_pos = []
    shark_move(arr, x, y, shark_pos)
    
    if not shark_pos:
        return

    #print(shark_pos,'\n\n')
    
    for sx, sy in shark_pos:
        #print(sx, sy)
        arr[x][y] = [0,0]
        bfs(arr, sx, sy, total+num)
        #fish_map[x][y] = [0,0]
    

fish_map = [ [[0,0]]*4 for _ in range(4) ]

#print(fish_map)

l = []
for x in range(4):
    l = list( map(int, input().split()) )
    for y in range(0,7,2):
        fish_map[x][y//2] = [ l[y], l[y+1] ] 

#print(fish_map)
answer = 0
bfs(fish_map, 0, 0, 0)
print(answer)


