
# 아래, 오른쪽, 위쪽, 왼쪽
dxs = [1, 0, -1, 0]
dys = [0, 1, 0, -1]

n, m = map(int, input().split())

grid = [[0 for _ in range(m)] for _ in range(n)]

x, y, d = 0, 0, 0
grid[x][y] = 1

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

for i in range(2, n*m+1):
    nx, ny = x + dxs[d], y + dys[d]
    #print('i?: ', i, 'nx, ny? ', nx, ny)
    if not in_range(nx, ny) or grid[nx][ny] != 0:
        nd = (d+1)%4
        nx, ny = x + dxs[nd], y + dys[nd]
        d = nd
    
    grid[nx][ny] = i
    x, y = nx,ny
        
#print(grid)
for gg in grid:
    for g in gg:
        print(g, end=' ')
    print()









