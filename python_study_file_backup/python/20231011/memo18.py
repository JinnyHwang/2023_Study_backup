
from collections import deque

# 행이 작은 위치, 열이 작은 위치
dxs = [-1,0,0,1]
dys = [0,-1,1,0]

# 현재 위치를 기준으로 현재 값보다 작은 그룹을 확인

# 해당 그룹 안에서 값이 가장 큰 위치를 찾음
# 여러개 있을 경우 그 중 행,열이 작은 위치 선정

# 움직일 위치가 없으면 종료

n, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
r,c = map(int, input().split())
r,c = r-1, c-1

start_pos = (r,c)
start_pos_value = -1

max_num_pos = (-1,-1)
max_num = -1
visited = []

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if visited[x][y] or grid[x][y] >= start_pos_value:
        return False
    
    return True

def chk_max_num(x,y,num):
    global max_num_pos, max_num
    
    # position 구분위해서 같은 값도 확인
    if max_num < num:
        max_num = num
        max_num_pos = (x,y)
    elif max_num == num:
        # 행 비교
        if max_num_pos[0] != x:
            max_num_pos = (x,y) if max_num_pos[0] > x else max_num_pos
        else:
            max_num_pos = (x,y) if max_num_pos[1] > y else max_num_pos


def bfs():
    while q :
        cx,cy = q.popleft()
        
        for dx,dy in zip(dxs,dys):
            nx, ny = cx+dx, cy+dy
            if can_go(nx,ny):
                visited[nx][ny] = True
                chk_max_num(nx,ny,grid[nx][ny])
                q.append((nx,ny))
                #print('! ',(nx,ny))
                #print(start_pos, max_num)
                
    

for _ in range(k):
    
    #print('!!!', start_pos)
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append(start_pos)
    visited[start_pos[0]][start_pos[1]] = True
    start_pos_value = grid[start_pos[0]][start_pos[1]]
    max_num = -1
    bfs()
    
    # 변동이 없으면 탐색 중지
    if max_num_pos == start_pos:
        break
    else:
        start_pos = max_num_pos

#print(start_pos)
print(start_pos[0]+1, start_pos[1]+1)

