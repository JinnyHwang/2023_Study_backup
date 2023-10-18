
n, m = tuple(map(int, input().split()))

start_pos = (0,0)
end_pos = (n-1,m-1)

# 하 우
dxs = [1,0]
dys = [0,1]

graph = [ list(map(int, input().split())) for _ in range(n)]
print(graph)
visited = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

re = 0
def dfs(x,y):
    global re
    #print(x,y)
    '''
    if (x,y) == end_pos:
        re = 1
        return
    '''
    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy
        #print(nx,ny)
        #print(graph[nx][ny])
        #print(in_range(nx,ny), graph[nx][ny], visited[nx][ny])
        if in_range(nx,ny) and graph[nx][ny] and not visited[nx][ny]:
            #print('?',nx,ny)
            visited[nx][ny] = 1
            dfs(nx,ny)


def dfs2(x,y):
    global re
    
    visited[x][y] = 1
    
    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy

        if in_range(nx,ny) and graph[nx][ny] and not visited[nx][ny]:
            dfs(nx,ny)
    
# visited 갱신 시점이 다름
dfs2(0,0)       

visited = [[0 for _ in range(m)] for _ in range(n)]
visited[0][0] = 1
dfs(0,0)
#print(re)
print(visited[n-1][m-1])
