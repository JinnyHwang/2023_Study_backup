from collections import deque

n, k, m = tuple(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
s_pos = []
stone_pos = [(i,j) for i in range(n) for j in range(n) if a[i][j] == 1]
selected_stones = []
ans = 0
q = deque()
visited = [[False for _ in range(n)] for _ in range(n)]


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y):
    return in_range(x, y) and not a[x][y] and not visited[x][y]


def bfs():
    while q:
        x,y = q.pop()
        
        dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]

        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y + dy
            
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True

def calc():
    for x,y in selected_stones:
        a[x][y] = 0
        
    for i in range(n):
        for j in range(n):
            visited[i][j] = False
    
    for x,y in s_pos:
        q.append((x,y))
        visited[x][y] = True
        
    bfs()
    
    for x,y in selected_stones:
        a[x][y] = 1
        
    cnt = 0
    for i in range(n):
        for j in range(n):
            if visited[i][j]:
                cnt += 1
    
    return cnt
    

def find_max(idx, cnt):
    global ans
    
    if idx == len(stone_pos):
        if cnt == m:
            ans = max(ans, calc())
        return
    
    selected_stones.append(stone_pos[idx])
    find_max(idx+1, cnt+1)
    selected_stones.pop()
    
    find_max(idx+1, cnt)
    

for _ in range(k):
    r,c = map(int, input().split())
    s_pos.append((r-1,c-1))

find_max(0,0)
print(ans)



