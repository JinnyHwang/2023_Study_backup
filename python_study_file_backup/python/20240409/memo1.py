'''
n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]

r, c = map(int, input().split())
r, c = r-1, c-1

def grid_print(grid):
    for gg in grid:
        for g in gg:
            print(g, end=' ')
        print()
    print()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def boob(r, c, num):
    global grid
    
    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]
    
    x, y = r, c
    grid[x][y] = 0
    for dx, dy in zip(dxs, dys):
        x, y = r, c
        for _ in range(num-1):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny):
                grid[nx][ny] = 0
                x, y = nx, ny
            else:
                break
            

def gravity():
    global grid
    temp  = []
    
    for j in range(n):
        temp  = []
        for i in range(n-1, -1, -1):
            if grid[i][j] != 0:
                temp.append(grid[i][j])
                grid[i][j] = 0
        
        index = n-1
        for t in temp:
            grid[index][j] = t
            index -= 1



#grid_print(grid)
boob(r, c, grid[r][c])
#grid_print(grid)

gravity()
grid_print(grid)
'''

# 해설 확인
n = int(input())

grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]

def grid_print(grid):
    for gg in grid:
        for g in gg:
            print(g, end=' ')
        print()
    print()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return (x == center_x or y == center_y) and abs(x - center_x) + abs(y-center_y) < bomb_range


def bomb(center_x, center_y):
    bomb_range = grid[center_x][center_y]
    
    for i in range(n):
        for j in range(n):
            if in_bomb_range(i, j, center_x, center_y, bomb_range):
                grid[i][j] = 0
    
    for j in range(n):
        next_row = n-1
        for i in range(n-1, -1, -1):
            if grid[i][j]:
                next_grid[next_row][j] = grid[i][j]
                next_row -= 1
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
            


r, c = map(int, input().split())
bomb(r-1, c-1)

grid_print(grid)