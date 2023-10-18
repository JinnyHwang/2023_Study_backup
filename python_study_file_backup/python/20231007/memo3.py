
# 격자 position
# 각 격자안에는 순서가 중요한 숫자 list 존재

# 숫자를 쌓는 방식
# list[start:]를 더한다

n, m = map(int, input().split())
grid = [[[] for _ in range(n) ] for _ in range(n)]
for i in range(n):
    gl = list(map(int, input().split()))
    for j in range(n):
        grid[i][j].append(gl[j])
print(grid)

num_list = list(map(int, input().split()))
print(num_list)


def find_mi_pos(mi):
    for i in range(n):
        for j in range(n):
            for gi, g in enumerate(grid[i][j]):
                if mi == g:
                    return (i, j, gi)

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n
    

# 숫자들이 정확히 한번씩만 등장하는 n * n 크기의 격자판
def find_move_pos(mx,my):
    # 8개 방향
    ds = [(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1)]
    max_num = 0
    max_x, max_y = 0, 0

    for dx,dy in ds:
        nx = mx+dx
        ny = my+dy
        if in_range(nx,ny):
            print('grid[nx][ny]?', grid[nx][ny])
            for ng in grid[nx][ny]:
                if max_num < ng:
                    max_num = ng
                    max_x, max_y = nx, ny
    
    if max_num == 0:
        return (mx,my)
    else:
        return (max_x, max_y)




def move(mi):
    global grid
    
    mx, my, gi = find_mi_pos(mi)
    print('mx, my, gi?', mx, my, gi)

    nx, ny = find_move_pos(mx, my)
    if (nx,ny) != (mx, my):
        grid[nx][ny] += grid[mx][my][gi:]
        grid[mx][my] = grid[mx][my][:gi]



for mi in num_list:
    print(grid)
    move(mi)
print(grid)

#grid = [[[], [], []], [[2], [7,6], [3]], [[4,1,9], [8], [5]]]
for i in range(n):
    for j in range(n):
        if not grid[i][j]:
            print(None)
        else:
            for g in grid[i][j][::-1]:
                print(g, end=' ')
            #for gg in range(len(grid[i][j])-1, -1, -1):
                #print(grid[i][j][gg], end=' ')
            #for g in grid[i][j]:
                #print(g, end=' ')
            print()




