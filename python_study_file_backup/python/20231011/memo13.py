
# 터지는 블럭 개수
# 최대 블럭 크기
# 1 <= num <= 100
# 1 <= n <= 100

n = int(input())
num_grid = [list(map(int,input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y,num):
    if not in_range(x,y):
        return False
    
    if visited[x][y] or num_grid[x][y] != num:
        return False
    
    return True

def dfs(x,y,num):
    global block
    
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]
    
    for dx, dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx,ny,num):
            block += 1
            visited[nx][ny] = True
            dfs(nx,ny,num)



bomb_block = 0
block = 0
max_block = -1
# 모든 index 탐색
for i in range(n):
    for j in range(n):
        if not visited[i][j]:
            block = 1
            visited[i][j] = True
            dfs(i,j,num_grid[i][j])
            max_block = max(max_block,block)
            #print(block)
            
            if block >= 4:
                bomb_block += 1
                

print(bomb_block, max_block)

