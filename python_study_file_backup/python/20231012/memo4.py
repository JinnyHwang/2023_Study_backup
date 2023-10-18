
# 결국 해설 보기...ㅠ
# 빙하가 녹는 조건
# 인접한 곳에 빙하에 둘러 쌓여 있지 않은 물이 있는 경우
# 빙하에 둘러 쌓여 있지 않은 물의 영역 구하기는
# (0,0) 시작점으로 bfs를 돌리면 된다! (가장 자리가 모두 물이라는 조건이 걸려있기 때문에)
# bfs로 (0,0)을 시작으로 물인 부분을 모두 표시
# 방문하지 않은 영역 중 1값에 대해 visited와 인접해있는지 확인하여 인접해있으면 물로 바꿔줌

# 대박이다...
# 녹일 빙하를 찾는 문제
# 복잡하게가면 예외가 너무 많이 생김..
from collections import deque

n, m = tuple(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

def grid_print(grid):
    for g in grid:
        for gg in g:
            print(gg,end=' ')
        print()

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if visited[x][y] or a[x][y]:
        return False
    
    return True


dxs, dys = [-1,0,0,1],[0,-1,1,0]
        
def bfs():
    global visited
    
    q = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    q.append((0,0))
    visited[0][0] = True
    
    while q:
        cx, cy = q.popleft()
        
        for dx,dy in zip(dxs,dys):
            nx, ny = cx+dx, cy+dy
            #print(nx,ny)
            if can_go(nx,ny):
                #print('in?')
                visited[nx][ny] = True
                q.append((nx,ny))
                

def find_ice():
    res = 0
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                res += 1
    return res
            
                
                
last_ice_cnt = find_ice()

for t in range(1, n*m):
    
    #print('time! ', t)
    #grid_print(a)
    #grid_print(visited)

    bfs()
    
    #print('after bfs')
    #grid_print(a)
    #grid_print(visited)
    
    for i in range(n):
        for j in range(m):
            if a[i][j] == 1:
                for dx,dy in zip(dxs,dys):
                    nx, ny = i+dx, j+dy
                    if visited[nx][ny]:
                        a[i][j] = 0
                        break
    
    #print('after bfs')
    #grid_print(a)
                    
    ice_cnt = find_ice()
    #print('ice_cnt? ', ice_cnt)
    if ice_cnt == 0:
        break
    else:
        last_ice_cnt = ice_cnt
            

print(t,last_ice_cnt)



