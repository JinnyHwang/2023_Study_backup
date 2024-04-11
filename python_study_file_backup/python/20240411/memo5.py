'''
# D L U R
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]

#d == 1
#5-d
#0,1 / 2,3

#d == 2
#3-d
#0,3 / 1,2

n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def check_time( start_pos, start_dir):
    
    x, y = start_pos
    d = start_dir
    time = 0
    while True:
        time += 1
        #print('check_time ', x, y, d, grid[x][y])
        
        # x,y pos로 이동
        
        # 방향 값 확인
        if grid[x][y] == 1:
            d = (5-d)%4
        elif grid[x][y] == 2:
            d = (3-d)%4
            
        nx, ny = x + dxs[d], y + dys[d]
        if not in_range(nx, ny):
            time += 1
            return time
        
        x, y = nx, ny


max_time = 0
for i in range(n*4):

    start_dir = i//n
    if start_dir == 0:
        start_pos = (0, i%n)
    elif start_dir == 1:
        start_pos = (i%n, n-1)
    elif start_dir == 2:
        start_pos = (n-1, (n-1)-(i%n))
    elif start_dir == 3:
        start_pos = ((n-1)-(i%n), 0)
    
    #print(i, start_dir, start_pos)
    curr_time = check_time(start_pos, start_dir)
    #print('curr_time?', curr_time)
    max_time = max(max_time, curr_time)
    

print(max_time)
'''

# 해설1
n = int(input())
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def calc(x, y, move_dir):
    # 상 하 좌 우
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    elapsed_time = 1
    
    while in_range(x,y):
        if grid[x][y] == 1:
            move_dir = 3-move_dir
        elif grid[x][y] == 2:
            move_dir = (move_dir+2) if move_dir<2 else (move_dir-2)
        
        x, y = x+dxs[move_dir], y+dys[move_dir]
        elapsed_time += 1
    
    return elapsed_time


ans = 0
for i in range(n):
    ans = max(ans, calc(n-1, i, 0))
    ans = max(ans, calc(0, i, 1))
    ans = max(ans, calc(i, n-1, 2))
    ans = max(ans, calc(i, 0, 3))

print(ans)

