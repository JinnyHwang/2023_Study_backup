'''
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y, num):
    
    if not in_range(x,y):
        return False
    
    if visited[x][y] or grid[x][y] != num:
        return False
    
    return True

def dfs(x, y, num):
    global block_cnt
    dxs, dys = [-1,1, 0, 0], [0, 0, -1, 1]
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if can_go(nx, ny, num):
            block_cnt += 1
            visited[nx][ny] = True
            dfs(nx, ny, num)
            
    
block_cnt = 0
max_block_cnt = 0
bomb_block_cnt = 0
for i in range(n):
    for j in range(n):
        if can_go(i,j, grid[i][j]):
            visited[i][j] = True
            block_cnt = 1
            dfs(i, j, grid[i][j])
            max_block_cnt = max(max_block_cnt, block_cnt)
            if block_cnt >= 4:
                bomb_block_cnt += 1
                

print(bomb_block_cnt, max_block_cnt)
'''














