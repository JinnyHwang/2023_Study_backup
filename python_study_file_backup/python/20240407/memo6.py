
n, m, q = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]

def print_grid():
    global grid
    for gg in grid:
        for g in gg:
            print(g, end=' ')
        print()
    print()


def move_colck_dir(r1, c1, r2, c2):
    global grid
    #(r1,c1) (r2,c2)
    
    temp = grid[r1][c1]
    
    # step1
    for i in range(r1+1, r2+1):
        grid[i-1][c1] = grid[i][c1]
    #print_grid()
    
    # step2
    for j in range(c1+1, c2+1):
        grid[r2][j-1] = grid[r2][j]
    #print_grid()
    
    #step3
    for i in range(r2, r1, -1):
        grid[i][c2] = grid[i-1][c2]
    #print_grid()
    
    # step4
    for j in range(c2, c1, -1):
        grid[r1][j] = grid[r1][j-1]
    #print_grid()
    
    grid[r1][c1+1] = temp     


def in_range(x,y):
    return 0 <= x < n and 0 <= y < m


def cal_average(new_grid, r1, c1, r2, c2):
    global grid
    dxs = [0, 1, -1, 0, 0]
    dys = [0, 0, 0, 1, -1]
    
    for i in range(r1, r2+1):
        for j in range(c1, c2+1):
            cal_sum = 0
            cal_cnt = 0
            for dx, dy in zip(dxs, dys):
                nx, ny = i+dx, j+dy
                if in_range(nx,ny):
                    cal_sum += grid[nx][ny]
                    cal_cnt += 1
            cal_avg = cal_sum//cal_cnt
            new_grid[i][j] = cal_avg
            
    return new_grid


#print_grid()
for _ in range(q):
    r1, c1, r2, c2 = map(int, input().split())
    r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
    
    # 시계방향으로 이동
    move_colck_dir(r1, c1, r2, c2)
    #print_grid()
    
    # 인접 칸 평균값 계산
    new_grid = [[0 for _ in range(m)] for _ in range(n)]
    for i in range(n):
        for j in range(m):
            new_grid[i][j] = grid[i][j]
    
    #new_grid에 평균값 계산하여 넣음
    new_grid = cal_average(new_grid, r1, c1, r2, c2)
    grid = new_grid
    #print_grid()


print_grid()








