
# 초기 격자판의 상태와 폭탄을 놓아야 할 위치들이 주어졌을 때,
# 가장 많이 초토화시킬 수 있는 영역의 수

n = int(input())
grid_l = []
pos_list = []
ans = 0
boom_grid = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    grid_l = list(map(int, input().split()))
    for j in range(n):
        if grid_l[j] == 1:
            pos_list.append((i,j))
    
boom1 = [(0,0),(-1,0),(-2,0),(1,0),(2,0)]
boom2 = [(0,0),(1,0),(-1,0),(0,-1),(0,1)]
boom3 = [(0,0),(-1,-1),(-1,1),(1,1),(1,-1)]
booms = [boom1]+[boom2]+[boom3]
#print(booms)

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def boom_area(bi, px, py, boom_grid):
    
    for bx, by in booms[bi]:
        nx = px + bx
        ny = py + by
        if in_range(nx,ny):
            boom_grid[nx][ny] = 1
    print('[boom_area] bi? ', bi, ' boom_grid? ', boom_grid)
    return boom_grid


def cnt_grid(boom_grid):
    cnt = 0
    for i in range(n):
        for j in range(n):
            if boom_grid[i][j] == 1:
                cnt += 1
    return cnt
    

def choose_boom(idx, boom_grid):
    global ans
    
    print('idx? ',idx, ' boom_grid? ', boom_grid)
    if idx == len(pos_list):
        #print('idx? ',idx, ' area? ', area)
        area = cnt_grid(boom_grid)
        if ans < area:
            ans = area
        print('area? ', area, ' ans? ', ans)
        return
    
    px, py = pos_list[idx]
    next_boom_grid = []
    for bi in range(3):
        next_boom_grid = boom_area(bi, px, py, boom_grid)
        choose_boom(idx+1, next_boom_grid)


choose_boom(0,boom_grid)
print(ans)





