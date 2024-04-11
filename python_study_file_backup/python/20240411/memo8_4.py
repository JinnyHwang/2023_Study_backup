# 상 하 좌 우
# (3-d)%4

dir_map = {'U':0, 'D':1, 'L':2, 'R':3}
grid = list()
next_grid = list()


def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end= ' ')
        print()
    print()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def move_1(x, y, d):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    nx, ny = x+dxs[d], y+dys[d]
    if in_range(nx, ny):
        return (nx, ny, d)
    else:
        # 방향을 바꾸는 작업에는 1초의 시간이 소요
        return (x, y, (5-d)%4)



def move_all_1(n, grid):
    
    next_grid = [[-1 for _ in range(n)] for _ in range(n)]
    
    #print('move_all')
    #print_grid(grid)
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] != -1:
                # 구슬 이동
                nx, ny, nd = move(i, j, grid[i][j])
                if next_grid[nx][ny] != -1: # 이미 한 번 접근 했다면
                    next_grid[nx][ny] = 5  # 존재하지 않는 방향값으로 초기화
                else:
                    next_grid[nx][ny] = nd
    
    #print('next_grid?')
    #print_grid(next_grid)
                
    for i in range(n):
        for j in range(n):
            if next_grid[i][j] != -1 and next_grid[i][j] != 5:
                grid[i][j] = next_grid[i][j]
            else:
                grid[i][j] = -1
    
    #print('grid!')
    #print_grid(grid)
              


# 아주 오랜시간이 흐른 후
def simulate_1(n, grid, visited):
    
    while True:
        #print('simulate')
        marble_cnt = 0
        # 해당 칸에 동일한 방향값을 가진 구슬이 4회 이상 방문했다면 break
        for i in range(n):
            for j in range(n):
                if grid[i][j] != -1:
                    marble_cnt += 1
                    visited[i][j][grid[i][j]] += 1
                    if visited[i][j][grid[i][j]] >= n:
                        return
                    
        if marble_cnt == 0 or marble_cnt == 1:
            return
        
        move_all(n, grid)


def update_next_grid(nx, ny, d):
    global next_grid
    if next_grid[nx][ny] == -1:
        next_grid[nx][ny] = d
    else:
        next_grid[nx][ny] = 5

def move(x, y, d):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    nx, ny = x+dxs[d], y+dys[d]
    if in_range(nx, ny):
        #return (nx, ny, d)
        update_next_grid(nx, ny, d)
    else:
        # 방향을 바꾸는 작업에는 1초의 시간이 소요
        #return (x, y, (5-d)%4)
        update_next_grid(x, y, (5-d)%4)


def move_all():
    global next_grid, grid
    next_grid = [[-1 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] != -1:
                # 구슬 이동
                move(i, j, grid[i][j])
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
            

def remove_duplicate_marbles():
    global grid
    
    for i in range(n):
        for j in range(n):
            if grid[i][j] == 5:
                grid[i][j] = -1


def simulate():
    move_all()
    remove_duplicate_marbles()


T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    grid = [[-1 for _ in range(n)] for _ in range(n)]
    #visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    
    for _ in range(m):
        r, c, cmd = input().split()
        r = int(r)-1
        c = int(c)-1
        d = dir_map[cmd]
        grid[r][c] = d
        
    #simulate(n, grid, visited)
    for _ in range(2*n):
        simulate()
    
    ans = 0
    for g in grid:
        for gg in g:
            if gg != -1:
                ans += 1
    print(ans)
    