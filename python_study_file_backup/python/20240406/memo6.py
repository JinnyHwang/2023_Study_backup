
# 오른 아래 왼 위
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

n, m = map(int, input().split())

grid = [[0 for _ in range(m)] for _ in range(n)]

x, y, d = 0, 0, 0
grid[x][y] = 'A'

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

for i in range(1, n*m):
    nx, ny = x + dxs[d], y + dys[d]
    #print('i?: ', i, 'nx, ny? ', nx, ny)
    if not in_range(nx, ny) or grid[nx][ny] != 0:
        nd = (d+1)%4
        nx, ny = x + dxs[nd], y + dys[nd]
        d = nd
    
    grid[nx][ny] = chr(ord('A') + (i%26))
    #if (ord(grid[x][y]) + 1) > ord('Z'):
    #    grid[nx][ny] = 'A'
    #else:
    #    grid[nx][ny] = chr( (ord(grid[x][y]) + 1) )
    x, y = nx,ny
        
#print(grid)
for gg in grid:
    for g in gg:
        print(g, end=' ')
    print()

