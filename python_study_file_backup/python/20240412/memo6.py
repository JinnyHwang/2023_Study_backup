
from collections import deque

'''
def bfs_1():
    while q:
        curr_v = q.popleft()
        for next_v in range(1, VERTICES_NUM+1):
            if graph[curr_v][next_v] and not visited[curr_v][next_v]:
                print(next_v)
                visited[next_v] = True
                q.append(next_v)


def bfs():
    while q:
        curr_v = q.popleft()
        
        for next_v in graph[curr_v]:
            if not visited[next_v]:
                print(next_v)
                visited[next_v] = True
                q.append(next_v)
'''

'''
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]

q = deque()

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x, y):
    
    if not in_range(x,y):
        return False
    
    if visited[x][y] or grid[x][y] == 0:
        return False
    
    return True
    

def bfs():
    visited[0][0] = True
    q.append((0,0))
    
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while q:
        
        x, y = q.popleft()
        
        if (x, y) == (n-1, m-1):
            return 1
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                visited[nx][ny] = True
                q.append((nx, ny))
            
    return 0
        


print(bfs())
'''


'''
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
q = deque()


block_cnt = 0

for _ in range(k):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    q.append((r,c))
    visited[r][c] = True
    block_cnt += 1


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    
    if not in_range(x, y):
        return False
    
    if visited[x][y] or grid[x][y] == 1:
        return False
    
    return True


def dfs():
    global block_cnt
    dxs, dys = [-1, 1, 0, 0],[0, 0, -1, 1]
    
    while q:
        
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny):
                block_cnt += 1
                visited[nx][ny] = True
                q.append((nx, ny))
                
                
dfs()
print(block_cnt)
        
'''

'''
n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]
q = deque()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x, y):
    
    if not in_range(x, y):
        return False
    
    if visited[x][y] or grid[x][y] == 1:
        return False
    
    return True



def bfs():
    while q:
        x, y = q.popleft()
        
        dxs, dys = [-1, 1, 0, 0],[0, 0, -1, 1]
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            
            if can_go(nx, ny):
                q.append((nx, ny))
                visited[nx][ny] = True


for _ in range(k):
    x, y = map(int, input().split())
    q.append((x-1,y-1))
    visited[x-1][y-1] = True

bfs()

ans = sum([1 for i in range(n) for j in range(n) if visited[i][j]])
print(ans)
'''

# 시작 위치에서 bfs를해서 최댓값, 행열값이 작은 좌표를 찾음 q에 추가

n, k = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False  for _ in range(n)] for _ in range(n)]
r, c = map(int, input().split())
r, c = r-1, c-1

#q = deque()
#q.append((r,c))

def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x, y, num):
    
    if not in_range(x, y):
        return False
    
    if visited[x][y] or grid[x][y] >= num:
        return False
    
    return True


# 같은 visited를 사용할 수 있도록 함
def find_next_pos(x, y, pos_num):
    #visited = [[False  for _ in range(n)] for _ in range(n)]
    q = deque()
    q.append((x,y))
    visited[x][y] = True
    dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    max_num = 0
    max_x, max_y = n, n
    
    while q:
        x, y = q.popleft()
        #print('??', x, y)
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx, ny, pos_num):
                visited[nx][ny] = True
                q.append((nx, ny))
                #print('!', (nx, ny))
                if (max_num, -max_x, -max_y) < (grid[nx][ny], -nx, -ny):
                    max_num, max_x, max_y = grid[nx][ny], nx, ny
                    
    
    return (max_x, max_y)
        


pos_x, pos_y = r, c
#print('start')
#print(pos_x, pos_y)
for ki in range(k):
    visited = [[False  for _ in range(n)] for _ in range(n)]
    nx, ny = find_next_pos(pos_x, pos_y, grid[pos_x][pos_y])
    if (nx, ny) == (n, n):
        break

    #print('??', ki, nx, ny)
    pos_x, pos_y = nx, ny


print(pos_x+1, pos_y+1)

























