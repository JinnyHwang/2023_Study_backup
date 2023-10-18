from collections import deque


n, k = tuple(map(int, input().split()))

# 0은 이동 가능, 1은 이동 불가능
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

start_list = []
for _ in range(k):
    start_list.append(tuple(map(int, input().split())))
#print(n,k)
#print(grid)
#print(start_list)

dxs = [-1,0,0,1]
dys = [0,-1,1,0]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    return in_range(x,y) and not visited[x][y] and not grid[x][y]

def bfs():
    while q:
        i,j = q.popleft()
        
        for dx,dy in zip(dxs,dys):
            nx, ny = i+dx, j+dy
            if can_go(nx,ny):
                q.append((nx,ny))
                visited[nx][ny] = 1

q = deque()
for sx,sy in start_list:
    sx,sy = sx-1,sy-1
    q.append((sx,sy))
    visited[sx][sy] = 1
    
bfs()


print(sum([vv for v in visited for vv in v if vv == 1]))

