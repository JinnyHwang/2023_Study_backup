from collections import deque 

n, m = tuple(map(int, input().split()))
snake_map = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

end_pos = (n-1,m-1)

dxs = [-1,0,0,1]
dys = [0,-1,1,0]

q = deque()
q.append((0,0))
visited[0][0] = True

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if visited[x][y] or not snake_map[x][y]:
        return False
    
    return True

def push(x,y):
    q.append((x,y))
    visited[x][y] = True

route = 0
def bfs():
    global route
    
    while q:
        cx, cy = q.popleft()
        
        if (cx,cy) == end_pos:
            #print(q, cx, cy)
            route = 1
            return
        
        for dx,dy in zip(dxs,dys):
            nx, ny = cx+dx, cy+dy
            if can_go(nx,ny):
                push(nx,ny)
                

def bfs2():
    
    while q:
        cx, cy = q.popleft()
        
        for dx,dy in zip(dxs,dys):
            nx, ny = cx+dx, cy+dy
            if can_go(nx,ny):
                push(nx,ny)
                


#bfs()
#print(route)

bfs2()
ans = 1 if visited[n-1][m-1] else 0
print(ans)


