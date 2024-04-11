
def print_grid(grid):
    for g in grid:
        for gg in g:
            #print(gg, end=' ')
            if gg:
                for ggg in gg[::-1]:
                    print(ggg, end = ' ')
            else:
                print('None', end = ' ')
            print()


def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def find_curr_pos(num):
    
    for i in range(n):
        for j in range(n):
            if num in grid[i][j]:
                return (i,j)
    return (-1,-1)

def find_move_pos(x, y):
    
    max_num = 0
    max_x, max_y = -1, -1
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx,ny):
            for gi in grid[nx][ny]:
                if gi > max_num:
                    max_num = gi
                    max_x, max_y = nx, ny
    return (max_x, max_y)

def move_num(num, cx, cy, nx, ny):
    
    c_idx = -1
    for g_idx, g_num in enumerate(grid[cx][cy]):
        if g_num == num:
            c_idx = g_idx
            break
    c_slice = grid[cx][cy][c_idx:]
    grid[cx][cy] = grid[cx][cy][:c_idx]
    
    grid[nx][ny] += c_slice
    



dxs = [-1, -1, -1, 0, 1, 1,  1, 0]
dys = [-1,  0,  1, 1, 1, 0, -1, -1]

n, m = map(int, input().split())

grid = [[list()  for _ in range(n)] for _ in range(n)]
#print_grid(grid)

for i in range(n):
    li = list(map(int, input().split()))
    for j in range(n):
        grid[i][j].append(li[j])
        
#print_grid(grid)


num_list = list(map(int, input().split()))
#print(num_list)

for num_i in num_list:
    cx, cy = find_curr_pos(num_i)
    nx, ny = find_move_pos(cx, cy)
    #print('??', num_i, cx, cy, nx, ny)
    if (nx, ny) != (-1, -1):
        move_num(num_i, cx, cy, nx, ny)
    #print_grid(grid)

print_grid(grid)



#grid[1][2].append(10)
#grid[1][2].append(7)
#grid[1][2].append(13)
#grid[1][2].append(2)
#grid[0][0].pop()
#grid[1][0].pop()
#grid[0][1].pop()
#grid[2][1].append(1)
#print(find_move_pos(0, 1))
#print(find_curr_pos(3))
#print_grid(grid)
#move_num(7, 1, 2, 2, 1)
#print_grid(grid)

