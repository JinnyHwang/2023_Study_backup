'''
n, m, r, c = map(int, input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]

r -= 1
c -= 1

def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end= ' ')
        print()
    print()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def new_bomb(x, y, time):
    global grid, next_grid
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    #print('bomb_before ', x, y)
    
    dis = 2**(time-1)
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx*dis, y + dy*dis
        if in_range(nx, ny) and grid[nx][ny] == 0:
            #print(' bomb after ', nx, ny, end = ' ')
            next_grid[nx][ny] = 1

grid[r][c] = 1
for time in range(1, m+1):
    #print_grid(grid)
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[i][j]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 1:
                new_bomb(i, j, time)
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
                
    
#print_grid(grid)
num = 0
for g in grid:
    for gg in g:
        num += gg
print(num)
'''

n, m, r, c = map(int, input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def expand(x, y, dist):
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx*dist , y + dy*dist
        if in_range(nx, ny):
            next_grid[nx][ny] = 1



def simulate(dist):
    
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
            
    for i in range(n):
        for j in range(n):
            expand(i, j, dist)
    
    for i in range(n):
        for j in range(n):
            if next_grid[i][j]:
                grid[i][j] = 1
            


# 총 m번 simulation 진행
dist = 1
for _ in range(m):
    simulate(dist)
    # 시간이 지날 때 마다 2 곱해줌 -> 2^(t-1)
    dist *= 2









