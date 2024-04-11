
'''
def move(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    can_move = False
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] > grid[x][y]:
            can_move = True
            break
    if can_move:
        next_cnt[nx][ny] += 1
    

def move_all():
    
    for i in range(n):
        for j in range(n):
            next_cnt[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            if cnt[i][j] == 1:
                move(i,j)
    
    for i in range(n):
        for j in range(n):
            if next_cnt[i][j] == 1:
                cnt[i][j] = 1
            else:
                cnt[i][j] = 0
                
'''

'''
n, m, t = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
ball_pos = [[0 for _ in range(n)] for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    ball_pos[x-1][y-1] = 1

def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end = ' ')
        print()
    print()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    #num = grid[x][y]
    max_num = 0
    max_x, max_y = x, y
    for dx, dy in zip(dxs, dys):
        nx , ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] > max_num:
            max_num = grid[nx][ny]
            max_x, max_y = nx, ny
    return max_x, max_y
    

def simulate():
    global ball_pos
    new_ball_pos = [[0 for _ in range(n)] for _ in range(n)]
    print('start')
    print_grid(ball_pos)
    
    for i in range(n):
        for j in range(n):
            if ball_pos[i][j]:
                # move
                nx, ny = move(i, j)
                new_ball_pos[nx][ny] += 1
                print('??', (i,j), (nx,ny))
                
    print('end')
    print_grid(new_ball_pos)
    
    for i in range(n):
        for j in range(n):
            if new_ball_pos[i][j] == 1:
                ball_pos[i][j] = 1
            else:
                ball_pos[i][j] = 0
    
    print('end')
    print_grid(ball_pos)


for _ in range(t):
    simulate()


ans = 0
for bp in ball_pos:
    for b in bp:
        ans += b

print(ans)
'''

'''
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end= ' ')
        print()
    print()


def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def swap_num(x,y):
    global grid
    
    dxs = [-1, -1, -1, 0, 1, 1,  1,  0]
    dys = [-1,  0,  1, 1, 1, 0, -1, -1]
    
    swap_num = grid[x][y]
    max_num = 0
    max_x, max_y = -1,-1
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] > max_num:
            max_num = grid[nx][ny]
            max_x, max_y = nx, ny
    
    grid[x][y], grid[max_x][max_y] = max_num, swap_num


def find_num_pos(num):
    for i in range(n):
        for j in range(n):
            if grid[i][j] == num:
                return (i,j)
    return (-1,-1)

def simulate():
    global grid
    for ni in range(1, n*n+1):
        #print('simulate! ', ni)
        #print_grid(grid)
        
        pos_x, pos_y = find_num_pos(ni)
        
        swap_num(pos_x, pos_y)


for mi in range(m):
    #print('start turn ', mi)
    simulate()


print_grid(grid)
'''

