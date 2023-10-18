from collections import deque

n, k, u, d = tuple(map(int,input().split()))
a = [list(map(int, input().split())) for _ in range(n)]

ans = 0
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]

s_pos = []
pos = [ (i,j) for i in range(n) for j in range(n) ]

dxs = [-1,0,0,1]
dys = [0,-1,1,0]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x,y,h):
    if not in_range(x,y):
        return False
    
    if visited[x][y]:
        return False
    
    h = abs(h-a[x][y])
    if u <= h and h <= d:
        return True
    
    return False



def bfs():
    global q, visited
    
    while q:
        x,y = q.popleft()
        
        for dx,dy in zip(dxs,dys):
            nx, ny = x+dx, y+dy
            #height = abs(city_map[x][y]-city_map[nx][ny])
            if can_go(nx,ny,a[x][y]):
                q.append((nx,ny))
                visited[nx][ny] = True

def city_num():
    res = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                res += 1
    return res


def calc():
    global q, visited
    
    q = deque()
    visited = [[False for _ in range(n)] for _ in range(n) ]
    
    for cc in s_pos:
        visited[cc[0]][cc[1]] = True
        q.append(cc)
    
    bfs()
    
    return city_num()
    



def find_pos(idx,cnt):
    global ans
    
    if cnt > k:
        return
    
    if idx == n*n:
        if cnt == k:
            ans = max(ans, calc())
        return
    
    s_pos.append(pos[idx])
    find_pos(idx+1,cnt+1)
    s_pos.pop()
    
    find_pos(idx+1,cnt)
    


find_pos(0,0)
print(ans)
