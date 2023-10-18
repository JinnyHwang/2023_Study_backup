

n = int(input())
grid_l = []
pos_list = []
ans = 0
boom_grid = []

for i in range(n):
    grid_l = list(map(int, input().split()))
    for j in range(n):
        if grid_l[j] == 1:
            pos_list.append((i,j))
            
            
boom1 = [(0,0),(-1,0),(-2,0),(1,0),(2,0)]
boom2 = [(0,0),(1,0),(-1,0),(0,-1),(0,1)]
boom3 = [(0,0),(-1,-1),(-1,1),(1,1),(1,-1)]
booms = [boom1]+[boom2]+[boom3]
choose_boom = []


def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n


def cnt_grid(boom_grid):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if boom_grid[i][j] == 1:
                cnt += 1
    return cnt


def cnt_boom_area():
    boom_grid = [[0 for _ in range(n)] for _ in range(n)]
    
    for i in range(len(pos_list)):
        px,py = pos_list[i]
        cb = choose_boom[i]
        for cx, cy in booms[cb]:
            nx = px + cx
            ny = py + cy
            if in_range(nx,ny):
                boom_grid[nx][ny] = 1
                
    cnt = cnt_grid(boom_grid)
    return cnt        
    
        

def make_choose_boom(idx):
    global ans
    
    if idx == len(pos_list):
        cnt_area = cnt_boom_area()
        if ans < cnt_area:
            ans = cnt_area
        return
    
    for r in range(3):
        choose_boom.append(r)
        make_choose_boom(idx+1)
        choose_boom.pop()


make_choose_boom(0)
print(ans)





