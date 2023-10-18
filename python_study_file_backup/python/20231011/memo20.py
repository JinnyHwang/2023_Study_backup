#import collections
from collections import deque

NOT_EXISTS = (-1,-1)

n, k = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]

# 현재 위치
r, c = tuple(map(int, input().split()))
curr_cell = (r - 1, c - 1)

bfs_q = deque()
visited = [
    [False for _ in range(n)]
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y, target_num):
    return in_range(x, y) and not visited[x][y] and grid[x][y] < target_num

# visited 배열을 초기화 해줍니다.
def initialize_visited():
    for i in range(n):
        for j in range(n):
            visited[i][j] = False


def bfs():
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    
    curr_x, curr_y = curr_cell
    visited[curr_x][curr_y] = True
    bfs_q.append(curr_cell)
    
    target_num = grid[curr_x][curr_y]

    # bfs 시작
    while bfs_q:
        curr_x,curr_y = bfs_q.popleft()
        
        for dx,dy in zip(dxs,dys):
            nx, ny = curr_x+dx, curr_y+dy
            
            if can_go(nx,ny, target_num):
                bfs_q.append((nx,ny))
                visited[nx][ny] = True


def need_update(best_pos, new_pos):
    if best_pos == NOT_EXISTS:
        return True
    
    bx,by = best_pos
    nx,ny = new_pos
    
    return (grid[nx][ny], -nx, -ny) > (grid[bx][by], -bx, -by)


def move():
    global curr_cell
    
    initialize_visited()
    
    bfs()
    
    # visited를 확인하며 최적위치 찾기
    best_pos = NOT_EXISTS
    for i in range(n):
        for j in range(n):
            if not visited[i][j] or (i,j) == curr_cell:
                continue
            new_pos = (i,j)
            if need_update(best_pos, new_pos):
                best_pos = new_pos
    
    if best_pos == NOT_EXISTS:
        return False
    else:
        curr_cell = best_pos
        return True
    
for _ in range(k):
    if not move():
        break
    
    
print(curr_cell[0]+1,curr_cell[1]+1)

