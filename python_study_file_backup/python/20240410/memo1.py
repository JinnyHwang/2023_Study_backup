
n = int(input())
grid_input = [list(map(int, input().split())) for _ in range(n)]
grid = [[0 for _ in range(n)] for _ in range(n)]

def init_grid():
    global grid_input, grid
    for i in range(n):
        for j in range(n):
            grid[i][j] = grid_input[i][j]


def print_grid():
    global grid
    for g in grid:
        for gg in g:
            print(gg, end=' ')
        print()
    print()

def is_bomb_range(x, y, center_x, center_y, bomb_num):
    return ( x == center_x or y == center_y ) and ( abs(x- center_x)+abs(y - center_y) < bomb_num )
    

def bomb(r, c):
    global grid
    bomb_num = grid[r][c]
    for i in range(n):
        for j in range(n):
            if is_bomb_range(i, j, r, c, bomb_num):
                grid[i][j] = 0

    
def gravity():
    global grid
    temp = [[0 for _ in range(n)] for _ in range(n)]
    for j in range(n):
        temp_idx = n-1
        for i in range(n-1, -1, -1):
            if grid[i][j] != 0:
                temp[temp_idx][j] = grid[i][j]
                temp_idx -= 1
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = temp[i][j]
            

def find_twin():
    global grid
    cnt = 0
    # 가로로 확인
    for i in range(n):
        for j in range(n-1):
            if grid[i][j] != 0 and grid[i][j] == grid[i][j+1]:
                cnt += 1
                
    # 세로로 확인
    for j in range(n):
        for i in range(n-1):
            if grid[i][j] != 0 and grid[i][j] == grid[i+1][j]:
                cnt += 1
    
    return cnt
            

#print_grid()

max_cnt = 0
for i in range(n):
    for j in range(n):
        
        init_grid()
        #print('init')
        #print_grid()
        
        bomb(i, j)
        #print('bomb')
        #print_grid()
        
        gravity()
        #print('gravity')
        #print_grid()
        
        curr_cnt = find_twin()
        #print('find_twin(): ', curr_cnt)
        max_cnt = max(max_cnt, curr_cnt)

print(max_cnt)




