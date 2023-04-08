'''
https://www.acmicpc.net/problem/23290

https://yabmoons.tistory.com/719


'''

# ←, ↖, ↑, ↗, →, ↘, ↓, ↙
dd = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

# 상은 1, 좌는 2, 하는 3, 우는 4
# 우 하 좌 상 순서로 탐색
# DFS로 탐색. 가장 먼저 확인된 것이 우선순위 높은 것
sd = [(0,1),(1,0),(0,-1),(-1,0)]

# 우선순위가 가장 낮은 것 부터 탐색
# 상 좌 하 우
# BFS로 탐색. 가장 나중에 확인 된 max 값 좌표가 가장 우선순위가 높음
#sd = [(-1,0),(0,-1),(1,0),(0,1)]

'''
(d+1)%8 : 시계
(d-1)%8: 반시계
'''

mat_fish = [[list() for _ in range(4)] for _ in range(4)] # 각 좌표에 물고기 direction 저장
mat_smell = [[0 for _ in range(4)] for _ in range(4)] # 냄새 위치 저장. 2 count
M, S = map(int, input().split())
fish = []

for _ in range(M):
    r, c, d = map(int, input().split())
    mat_fish[r-1][c-1].append(d-1)
    #fish.append([r-1, c-1, d-1])
#print(mat_fish)

sr,sc = list(map(int, input().split()))
shark = [sr-1,sc-1]
#print(shark)


def DFS_shark(cnt, cur, point_list):
    
    global s_move_point, max_fish, shark
    
    if cnt == 3:
        eat_fish = 0
        s_move_point_chk = []
        for sr, sc in point_list:
            if [sr,sc] not in s_move_point_chk:
                eat_fish += len(mat_fish[sr][sc])
                s_move_point_chk.append([sr,sc])
        if eat_fish >= max_fish:
            max_fish = eat_fish
            shark = cur
            s_move_point = s_move_point_chk
            #print('?',point_list)
        return
    
    for i in range(4):
        nr = cur[0]+sd[i][0]
        nc = cur[1]+sd[i][1]
        if 0 <= nr < 4 and 0 <= nc < 4:
            point_list[cnt] = [nr,nc]
            DFS_shark(cnt+1, [nr,nc], point_list)
        



for _ in range(S):
    
    # 1. 모든 물고기 복제. 적용은 5번에서
    mat_fish_cp = [[list() for _ in range(4)] for _ in range(4)]
    
    for r in range(4):
        for c in range(4):
            if mat_fish[r][c] != []:
                mat_fish_cp[r][c].extend(mat_fish[r][c])
    
    '''
    for r, m1 in enumerate(mat_fish):
        for c, m2 in enumerate(m1):
            if m2 != []:
                 mat_fish_cp[r][c].extend(m2)
    '''
    '''
    print(mat_fish)
    print(mat_fish_cp)
    print(id(mat_fish_cp))
    print(id(mat_fish))
    print(mat_fish_cp[0][2], id(mat_fish_cp[0][2]))
    print(mat_fish[0][2], id(mat_fish[0][2]))
    '''
    
    # 2. 모든 물고기 한 칸 이동
    # 상어있는 칸, 물고기 냄새 있는 칸, 격자 벗어나는 칸 이동 불가능
    # 이동할 수 있을 때까지 방향 반시계 방향으로 전환
    # 이동 못하면 이동X
    new_mat_fish = [[list() for _ in range(4)] for _ in range(4)]
    for r in range(4):
        for c in range(4):
            if mat_fish[r][c] != []:
                for fi, fd in enumerate(mat_fish[r][c]):
                    for i in range(8):
                        nd = (fd-i)%8
                        #print(fd, nd)
                        #print(r,c,nd, dd[nd])
                        nr = r+dd[nd][0]
                        nc = c+dd[nd][1]
                        #격자를 벗어나지 않음, 상어 없음, 냄새 없음
                        if 0 <= nr < 4 and 0 <= nc < 4 and [nr,nc] != shark and mat_smell[nr][nc] == 0: # 상어 없음, 냄새 없음
                                new_mat_fish[nr][nc].append(nd)
                                #print('mat_fish[nr][nc]? ', mat_fish[nr][nc])
                                break
                    # 방향 다 돌아도 못움직임. 움직이지 않기
                    else:
                        new_mat_fish[r][c].append(fd)
                        continue
               
    #print(mat_fish)
    #print(new_mat_fish)
    mat_fish = new_mat_fish
    
    # 3. 상어 3칸 이동
    # 그래프로 가장 많은 물고기를 없앨 수 있는 칸 찾기
    # sd로 BFS해서 우선순위 가장 높은 3개 좌표 구함
    # DFS? BFS? 뭘 써야하지 DFS!
    # 중복순열!
    # 이전에 선택했던 방향으로 가는 것 가능
    # 상하상 == 상상하: 칸 동일, 그런데 순서에 따라 우선순위 있음
    s_move_point = []
    max_fish = -1
    DFS_shark(0, shark, [0,0,0])
    #print(max_fish, s_move_point)
    
    # 4. 사라진 물고기 냄새 기록
    # 기존 물고기 -1 해주고, 추가 물고기 2로 기록
    for r in range(4):
        for c in range(4):
            if mat_smell[r][c] > 0:
                mat_smell[r][c] -= 1
    
    for sr, sc in s_move_point:
        mat_smell[sr][sc] = 2
        mat_fish[sr][sc] = []
    #print(mat_smell)

    
    # 5. 물고기 복제 적용
    #print(mat_fish)
    #print(mat_fish_cp)
    for r in range(4):
        for c in range(4):
            if mat_fish_cp[r][c] != []:
                mat_fish[r][c].extend(mat_fish_cp[r][c])
    
    #print(mat_fish)
    #print(mat_fish_cp)
    
    
result = 0
for r in range(4):
    for c in range(4):
        if mat_fish[r][c] != []:
            result += len(mat_fish[r][c])
print(result)
            
    



