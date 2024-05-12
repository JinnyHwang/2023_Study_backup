
# 중간에 충돌할 수 있음
# 칸이 2배라고 생각하자
# 무게가 가장 크거나, 구슬의 번호가 가장 클 경우

# 가장 마지막으로 충돌이 일어난 시간이 언제인지

center_x = 2000
center_y = 2000
grid_len = 4001

range_x1 = 4001
range_x2 = -1
range_y1 = 4001
range_y2 = -1


# 격자 크기 0 ~ 4000 / 0 ~ 4000
grid = [[list() for _ in range(grid_len)] for _ in range(grid_len)]
next_grid = [[list() for _ in range(grid_len)] for _ in range(grid_len)]
marbles = {}

def print_grid(grid):
    for i in range(range_x1, range_x2+1):
        for j in range(range_y1, range_y2+1):
            print(grid[i][j], end=' ')
        print()
    print()

# center = 2000, 2000
# 좌표는?
# center_x, center_y = 2000, 2000
# curr_x, curr_y = center_x+(input_x*2), center_y+(input_y*2)

# 상 하 좌 우
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]
dir_map = {'U':0, 'D':1, 'L':2, 'R':3}


def can_collision():
    
    # 같은 행에 있는 구슬의 위치와 방향 확인
    # 같은 열에 있는 구슬의 위치와 방향 확인
    # 같은 거리같에 있는 구슬의 위치와 방향 확인
    for i in range(range_x1, range_x2+1):
        for j in range(range_y1, range_y2+1):
            if grid[i][j] != 0:
                now_d = marbles[grid[i][j]][1]
                # 진행 방향이 상 같은 열, 나보다 작은 행 확인
                if now_d == 0:
                    for ii in range(range_x1, i):
                        if grid[ii][j] != 0 and marbles[grid[ii][j]][1] == 1:
                            return True
                # 진행 방향이 하 같은 열, 나보다 큰 행 확인
                elif now_d == 1:
                    for ii in range(i+1, range_x2+1):
                        if grid[ii][j] != 0 and marbles[grid[ii][j]][1] == 0:
                            return True
                # 진행 방향이 좌 같은 행, 나보다 작은 열 확인
                elif now_d == 2:
                    for jj in range(range_y1, j):
                        if grid[i][jj] != 0 and marbles[grid[i][jj]][1] == 2:
                            return True
                elif now_d == 3:
                    for jj in range(j+1, range_y2+1):
                        if grid[i][jj] != 0 and marbles[grid[i][jj]][1] == 1:
                            return True
                
                for ii in range(range_x1, range_x2+1):
                    for jj in range(range_y1, range_y2+1):
                        if grid[ii][jj] != 0 and (ii != i and jj != j):
                            if abs(i-ii) == abs(j-jj):
                                
                                
                        
def move_all():
    global grid
    next_grid = [[0 for _ in range(grid_len)] for _ in range(grid_len)]
    collision = False
    
    #for i in range(grid_len):
    for i in range(range_x1, range_x2+1):
        #for j in range(grid_len):
        for j in range(range_y1, range_y2+1):
            if grid[i][j] != 0:
                mi = grid[i][j]
                d = marbles[mi][1]
                nx, ny = i+dxs[d], j+dys[d]
                
                if not next_grid[nx][ny]:
                    next_grid[nx][ny] = mi
                    change_range(nx, ny)
                else:
                    collision = True
                    m1_mi = mi
                    m1_w = marbles[mi][0]
                    
                    m2_mi = next_grid[nx][ny]
                    m2_w = marbles[m2_mi][0]
                    # 무게와 구슬 번호 비교
                    # 우선 순위가 큰 구슬을 기록 낮은건 삭제
                    if (m1_w, m1_mi) > (m2_w, m2_mi):
                        next_grid[nx][ny] = m1_mi
                        del marbles[m2_mi]
                    else:
                        next_grid[nx][ny] = m2_mi
                        del marbles[m1_mi]
                            
    grid = next_grid
    return collision

def change_range(x, y):
    global range_x1, range_x2, range_y1, range_y2
    if x < range_x1:
        range_x1 = x
    if x > range_x2:
        range_x2 = x
    if y < range_y1:
        range_y1 = y
    if y > range_y2:
        range_y2 = y
    


def simulate():
    collision = False
    final_time = -1
    time = 0
    #while True:
    while time < 2:
        
        #if not can_collision():
        #    return final_time
        
        print('1')
        print_grid(grid)
        # 1초 가는 도중에 충돌
        time += 1
        collision = False
        collision = move_all()
        if collision:
            final_time = time
        
        print('2')
        print_grid(grid)
        # 2초 이동 끝나고 충돌
        time += 1
        collision = False
        collision = move_all()
        if collision:
            final_time = time
        
        print('3')
        print_grid(grid)
    
    return final_time
        

T = int(input())

for _ in range(T):
    m = int(input()) # 구슬 개수
    # 구슬 번호를 가지고 있음
    grid = [[0 for _ in range(grid_len)] for _ in range(grid_len)]
    # 각 번호별 구슬의 무게, 방향 정보를 가지고 있음
    marbles = {}
    for mi in range(1, m+1):
        r, c, w, d = input().split()
        x = center_x + (int(c)*2)
        y = center_y + (int(r)*2)
        w = int(w)
        d = dir_map[d]
        change_range(x, y)
       
        #print(x, y, w, d)
        #print(range_x1, range_x2, range_y1, range_y2)
        #grid[x][y].append((w, mi, dir_map[d]))
        #grid[x][y].append(mi)
        grid[x][y] = mi
        marbles[mi] = marbles.get(mi, []) + [w, d]
        

    print_grid(grid)
    #print(range_x1, range_x2, range_y1, range_y2)
    #print(marbles)
    
    #last_collision_time = simulate()
    print(simulate())
    


