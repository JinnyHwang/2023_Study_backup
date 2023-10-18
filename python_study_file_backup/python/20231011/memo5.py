
def in_range(x,y):
    return 0 <= x < 5 and 0 <= y < 5

def can_go(x,y):
    
    if not in_range(x,y):
        return False
    
    if visited[x][y] or grid[x][y] == 0:
        return False
    
    return True


def dfs(x,y):
    global order
    
    dxs, dys = [1,0],[0,1]
    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy
        
        if can_go(nx,ny):
            answer[nx][ny] = order
            order += 1
            visited[nx][ny] = 1
            dfs(nx,ny)


def dfs2(x,y):
    global order
    
    dxs, dys = [1,0],[0,1]
    
    answer[x][y] = order
    order += 1
    visited[x][y] = 1
            
    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy
        
        if can_go(nx,ny):
            dfs(nx,ny)





answer[0][0] = order
order += 1
visited[0][0] = 1
dfs(0,0)




