
n, m, t, k = map(int, input().split())

# 방향 상 하 좌 우 (5-d)%4
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
dir_map = {'U':0, 'D':1, 'L':2, 'R':3}


# 구슬 번호, 구슬 좌표, 방향 정보, 속도
# (i, d, v)
grid = [[list() for _ in range(n)] for _ in range(n)]
new_grid = [[list() for _ in range(n)] for _ in range(n)]

def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end=' ')
        print()
    print()


print_grid(grid)
for mi in range(1, m+1):
    r, c, d, v = input().split()
    r = int(r)-1
    c = int(c)-1
    d = dir_map[d]
    v = int(v)
    #grid[r][c].append((mi, d, v))
    grid[r][c].append((v, mi, d))

print('start')
print_grid(grid)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def move(r, c, d, v):
    
    x, y, cur_d = r, c, d
    for _ in range(v):
        nx, ny = x+dxs[cur_d], y+dys[cur_d]
        if in_range(nx, ny):
            x, y = nx, ny
        else:
            nd = (5-cur_d)%4
            nx, ny = x+dxs[nd], y+dys[nd]
            x, y, cur_d = nx, ny, nd
    return (x, y, cur_d)


def move_all():
    global grid
    new_grid = [[list() for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j]:
                #for mi, d, v in grid[i][j]:
                for v, mi, d in grid[i][j]:
                    nx, ny, nd = move(i, j, d, v)
                    #new_grid[nx][ny].append((mi, nd, v))
                    new_grid[nx][ny].append((v, mi, nd))
    grid = new_grid



def marble_collision():
    
    for i in range(n):
        for j in range(n):
            if len(grid[i][j]) > k:
                print('??', grid[i][j])
                #grid[i][j].sort(reverse=True)
                grid[i][j].sort(key=lambda x : (-x[0], -x[1]))
                print('!!', grid[i][j])
                new_list = grid[i][j][:k]
                grid[i][j] = new_list


def simulate():
    
    print('before move')
    print_grid(grid)
    # 모든 구슬 움직이기
    move_all()
    
    print('after move')
    print_grid(grid)
    
    # 우선순위에 따라 구슬 충돌 확인하기
    marble_collision()
    print('before collision')
    print_grid(grid)



for _ in range(t):
    simulate()


print('final')
print_grid(grid)

ans = 0
for g in grid:
    for gg in g:
        if gg:
            ans += len(gg)
print(ans)

