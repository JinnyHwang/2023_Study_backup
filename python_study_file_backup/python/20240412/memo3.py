
# 무게, 방향 변함

n, m, t = map(int, input().split())
grid = [[list() for _ in range(n)] for _ in range(n)]
next_grid = [[list() for _ in range(n)] for _ in range(n)]

mapper = {'U':0, 'D':1, 'R':2, 'L':3}

def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end=' ')
        print()
    print()


for mi in range(1, m+1):
    r, c, d, w = input().split()
    r, c, d, w = int(r)-1, int(c)-1, mapper[d], int(w)
    # 번호로 결정됨
    grid[r][c].append((mi, w, d))

print_grid(grid)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def move(x, y, d):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, 1, -1]
    
    nx, ny = x+dxs[d], y+dys[d]
    if in_range(nx,ny):
        return (nx,ny,d)
    else:
        return (x,y,(5-d)%4)


def move_all():
    global grid
    next_grid = [[list() for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                for m, w, d in grid[i][j]:
                    nx, ny, nd = move(i, j, d)
                    next_grid[nx][ny].append((m, w, nd))
                
    grid = next_grid


def collision():
    global grid
    max_w = -1
    cnt = 0
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) > 1:
                grid[i][j].sort(reverse=True)
                mi1, _, d1 = grid[i][j][0]
                w1 = 0
                for g in grid[i][j]:
                    w1 += g[1]
                grid[i][j] = [(mi1, w1, d1)]
                max_w = max(max_w, w1)
                cnt += 1
            elif grid[i][j]:
                max_w = max(max_w, grid[i][j][0][1])
                cnt += 1
    return (max_w, cnt)          
            

def simulate():
    global biggest_w, marble_cnt
    print('1')
    print_grid(grid)
    move_all()
    
    print('2')
    print_grid(grid)
    (biggest_w,marble_cnt) = collision()
    
    print('3')
    print_grid(grid)


print('start')
print_grid(grid)
for _ in range(t):
    biggest_w = -1
    marble_cnt = -1
    simulate()
    print(marble_cnt, biggest_w)

