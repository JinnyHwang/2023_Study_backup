
# 오 위 왼 아
dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

# 가운데에서 시작 n은 항상 홀수
n = int(input())

grid = [[0 for _ in range(n)] for _ in range(n)]



def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

x, y = n//2, n//2
d = 0
grid[x][y] = 1

nx,ny = x + dxs[d], y + dys[d]
if in_range(nx,ny):
    grid[nx][ny] = 2
    x,y = nx,ny
    d = (d+1)%4
    
for i in range(3, n*n+1):
    # 방향을 꺽었을 경우 먼저 탐색
    nd = (d+1)%4
    nx, ny = x + dxs[nd], y + dys[nd]
    # range를 벗어나거나, 꺽어야 하는 방향에 0이면 꺽음
    if not in_range(nx,ny) or grid[nx][ny] == 0:
        x, y, d= nx, ny, nd
    else: # 방향 유지
        nx, ny = x + dxs[d], y + dys[d]
        x, y = nx, ny
        
    grid[x][y] = i


for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()














