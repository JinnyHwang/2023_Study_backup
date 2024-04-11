'''
# 상하좌우 우선순위 이므로 진행방향 순서 설정

# 가장 마지막에 탐색하는 숫자가 우선순위가 높도록
# 우좌하상
dxs = [0, 0, 1, -1]
dys = [1, -1, 0, 0]

n, r, c = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

x, y = r-1, c-1
while True:
    print(grid[x][y], end=' ')
    curr_num = grid[x][y]
    next_x, next_y = x, y
    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] > curr_num:
            next_x, next_y = nx, ny
    
    # 이동할 수 없음
    if (next_x, next_y) == (x, y):
        break

    x, y = next_x, next_y

print()
'''
'''
# 상하좌우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

n, r, c = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

x, y = r-1, c-1
while True:
    print(grid[x][y], end=' ')
    curr_num = grid[x][y]
    next_x, next_y = x, y
    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] > curr_num:
            next_x, next_y = nx, ny
            break
    
    # 이동할 수 없음
    if (next_x, next_y) == (x, y):
        break

    x, y = next_x, next_y

print()

'''

'''
# 한곳에라도 이미 격자판 위에 놓여있던 블럭과 맞닿게 된다거나,
# 혹은 바닥에 닿게 된다면 떨어지는 것을 멈추게 됩니다.

n, m, k = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

block = [0 for _ in range(n)]
block[k-1:k-1+m] = [1]*m
print(block)

def grid_print():
    for g in grid:
        for gg in g:
            print(gg, end=' ')
        print()
    print()

def find_drop_row():
    
    row = -1
    for i in range(n):
        for bi, b in enumerate(block):
            if b == 1 and grid[i][bi] != 0:
                return row
        else:
            row = i
    
    return row


next_turn = True
while next_turn:
    
    next_turn = True
    row = find_drop_row()
    if row == -1:
        break
    
    print('row? ', row)
    
    if row == n-1:
        next_turn = False
    
    for bi, b in enumerate(block):
        if b == 1:
            grid[row][bi] = 1
            if row != n-1 and grid[row+1][bi] == 1:
                next_turn = False
    #grid_print()
    

grid_print()
'''

n, m, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

# 해당 row에 col_s, col_e 열에 전부 블록이 없느지 확인
def all_blank(row, col_s, col_e):
    return all([ not grid[row][col] for col in range(col_s, col_e+1) ])

def get_target_row():
    for row in range(n-1):
        # 블록이 존재하는 위치를 찾음
        if not all_blank(row+1, k, k+m-1):
            return row
    return n-1


k -= 1

target_row = get_target_row()

for col in range(k, k+m):
    grid[target_row][col] = 1

for i in range(n):
    for j in range(n):
        print(grid[i][j], end=' ')
    print()





















