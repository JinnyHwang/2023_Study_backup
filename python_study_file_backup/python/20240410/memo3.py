
# 반시계방향으로 탐색
# 우 상 좌 하
dxs = [0, -1, 0, 1]
dys = [1, 0, -1, 0]

# 벽은? 진행방향의 오른쪽 벽을 짚으면서 감
# 진행방향은 d, 벽 위치는 d-1을 봄

def grid_print(grid):
    print()
    for g in grid:
        for gg in g:
            print(gg, end=' ')
        print()
    print()
            
n = int(input())
r, c = map(int, input().split())
grid = [[0 for _ in range(n)] for _ in range(n)]
visited = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    input_str = input()
    for j in range(n):
        if input_str[j] == '#':
            grid[i][j] = 1
        else:
            grid[i][j] = 0

#grid_print(grid)

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def exist_right_block(x, y, d):
    dd = (d+3)%4
    nddx, nddy = x+dxs[dd], y+dys[dd]
    if in_range(nddx, nddy) and grid[nddx][nddy] == 1:
        return True
    else:
        return False

'''
time = 0
x, y, d = r-1, c-1, 0
visited[x][y] += 1
no_move_turn = 0

while True:
    
    #print('start')
    #print(x, y, d)
    #grid_print(visited)
    if visited[x][y] >= 5:
        time = -1
        break
    
    if no_move_turn > 10:
        time = -1
        break
    
    nx, ny = x+dxs[d], y+dys[d]
    #print(nx, ny)
    if in_range(nx, ny):
        #print('next pos in range: yes')
        # 벽 없으면 전진
        if grid[nx][ny] == 0:
            #print('go go')
            x, y = nx, ny
            visited[x][y] += 1
            if not exist_right_block(nx, ny, d):
                #print('turn clock wise')
                # 시계 방향으로 전환
                d = (d+3)%4
            time += 1
            no_move_turn = 0
        # 벽 있으면 반시계방향 전환
        else:
            #print('can not go. turn counterclock wise')
            d = (d+1)%4
            no_move_turn += 1
    else:
        #print('exit!')
        time += 1
        #print(time)
        break
    
    
print(time)
'''

import sys

DIR_NUM = 4

n = int(input())
curr_x, curr_y = tuple(map(int, input().split()))
a = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 동일 위치, 동일 방향 진행한 적이 있었는지 표기
visited = [[[False for _ in range(DIR_NUM)] for _ in range(n+1)] for _ in range(n+1)]

elapsed_time = 0
curr_dir = 0

def in_ragne(x,y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def wall_exist(x,y):
    return in_range(x,y) and a[x][y] == '#'

def simulate():
    global curr_x, curr_y, curr_dir, elapsed_time
    
    if visited[curr_x][curr_y][curr_dir] == True:
        print(-1)
        sys.exit(0)
        
    visited[curr_x][curr_y][curr_dir] = True
    dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
    next_x, next_y = curr_x + dxs[curr_dir], curr_y + dys[curr_dir]
    
    if wall_exist(next_x, next_y):
        curr_dir = (curr_dir-1+4)%4
    elif not in_range(next_x, next_y):
        curr_x, curr_y = next_x, next_y
        elapsed_time += 1
    else:
        rx = next_x + dxs[(curr_dir+1)%4]
        ry = next_y + dys[(curr_dir+1)%4]
        
        if wall_exist(rx, ry):
            curr_x, curr_y = next_x, next_y
            elapsed_time += 1
        else:
            curr_x, curr_y = rx, ry
            curr_dir = (curr_dir+1)%4
            elapsed_time += 2
            

for i in range(1, n + 1):
    given_row = input()
    for j, elem in enumerate(given_row, start = 1):
        a[i][j] = elem

# 격자를 빠져나오기 전까지 계속 반복합니다.
while in_range(curr_x, curr_y):
    # 조건에 맞춰 움직여봅니다.
    simulate()

print(elapsed_time)















