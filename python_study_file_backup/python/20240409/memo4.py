
'''
# 특정 열을 선택하면, 숫자가 적힌 칸 중 가장 위에 있는 칸을 중심으로 잡음 (0번째부터 탐색)
# 기준점부터 폭탄이 터지는데, 크기는 기준점의 값

def gird_print():
    for gg in grid:
        for g in gg:
            print(g, end=' ')
        print()
    print()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def select_pos(col):
    
    for i in range(n):
        if grid[i][col] != 0:
            return i
    return -1


def bomb(r, c, size):
    dxs = [0, 0, 1, -1]
    dys = [1, -1, 0, 0]
    
    x, y = r, c
    grid[x][y] = 0
    for dx, dy in zip(dxs, dys):
        x, y = r, c
        for _ in range(size-1):
            nx, ny = x+dx, y+dy
            if not in_range(nx, ny):
                break
            
            grid[nx][ny] = 0
            x, y = nx, ny
        

def gravity():
    
    next_grid = [[0 for _ in range(n)] for _ in range(n)]
    
    for j in range(n):
        next_idx = n-1
        for i in range(n-1, -1, -1):
            if grid[i][j] != 0:
                next_grid[next_idx][j] = grid[i][j]
                next_idx -= 1
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]



n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

for mi in range(m):
    
    col = int(input())-1
    row = select_pos(col)
    
    # 기준점을 잡을 수 없음
    if row == -1:
        #print('mi? ', mi)
        continue
    
    #print('start')
    gravity()
    
    bomb(row, col, grid[row][col])
    #print('bomb')
    #gird_print()
    
    gravity()
    #print('gravity')
    #gird_print()


gird_print()
'''

# 해설
OUT_OF_GRID = -1

n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]

def in_bomb_range(x, y, center_x, center_y, bomb_range):
    return ( x == center_x or y == center_y ) and ( abs(x-center_x)+abs(y-center_y) < bomb_range )


def bomb(center_x, center_y):
    
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
        
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
                


def get_bomb_row(col):
    for row in range(n):
        if grid[row][col] != 0:
            return row
    return OUT_OF_GRID



for _ in range(m):
    bomb_col = int(input())-1
    bomb_row = get_bomb_row(bomb_col)
    
    if bomb_row == OUT_OF_GRID:
        continue
    
    bomb(bomb_row, bomb_col)

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()



