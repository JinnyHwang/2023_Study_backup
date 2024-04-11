def grid_print():
    for g in grid:
        for gg in g:
            print(gg, end=' ')
        print()
    print()


def rotate_90_clock():
    
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
            
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[n-j-1][i]
                
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
    


def gravity():
    
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
            
    for j in range(n):
        next_row = n-1
        for i in range(n-1, -1, -1):
            if grid[i][j]:
                next_grid[next_row][j] = grid[i][j]
                next_row -= 1
            
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
    
    

def find_end_idx(start_idx, col, num):
    
    for end_idx in range(start_idx+1, n):
        if grid[end_idx][col] != num:
            return end_idx-1
    return n-1


def after_rotate_can_bomb():
    
    for i in range(n):
        curr_idx = 0
        while curr_idx < n:
            if grid[i][curr_idx] == 0:
                curr_idx += 1
                continue
                
            end_idx = find_end_idx(i, curr_idx, grid[i][curr_idx])
            
            if end_idx - curr_idx + 1 >= m:
                return True
            
            curr_idx = end_idx+1
            
    return False
            

def can_bomb():
    for j in range(n):
        curr_idx = 0
        while curr_idx < n:
            if grid[curr_idx][j] == 0:
                curr_idx += 1
                continue
                
            end_idx = find_end_idx(curr_idx, j, grid[curr_idx][j])
            
            
            if end_idx - curr_idx + 1 >= m:
                return True
            
            curr_idx = end_idx+1
            
    return False



def bomb():
    exploed = False
    for j in range(n):
        curr_idx = 0
        while curr_idx < n:
            if grid[curr_idx][j] == 0:
                curr_idx += 1
                continue
                
            end_idx = find_end_idx(curr_idx, j, grid[curr_idx][j])
            
            
            if end_idx - curr_idx + 1 >= m:
                for idx in range(curr_idx, end_idx+1):
                    grid[idx][j] = 0
                exploed = True
            
            curr_idx = end_idx+1
            
    return exploed
            
 
    
n, m, k = tuple(map(int, input().split()))         
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]


for _ in range(k):
    
    print('start!')
    
    bomb()
    print('bomb')
    grid_print()
    
    gravity()
    print('gravity')
    grid_print()
    
    rotate_90_clock()
    print('rotate_90_clock')
    #grid_print()
    
    gravity()
    print('gravity')
    grid_print()
    

print('Humm...')
while True:

    bomb()
    print('bomb')
    grid_print()
    
    gravity()
    print('gravity')
    grid_print()
    
    rotate_90_clock()
    print('rotate_90_clock')
    grid_print()
    
    gravity()
    print('gravity')
    grid_print()
    
    if not can_bomb():
        break



#grid_print()
cnt = 0
for i in range(n):
    for j in range(n):
        if grid[i][j]:
            cnt += 1
print(cnt)
