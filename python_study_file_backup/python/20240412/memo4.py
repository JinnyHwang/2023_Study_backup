'''
# graph[i]는 각각 i번째 정점에 연결되어 있는 정점들 목록을 관리하는 동적 배열이 되어야함
# graph[vertex]안에 리스트 형태로 들어있게됨
def dfs(vertex):
    for curr_x in graph[vertex]:
        if not visited[curr_x]:
            print(curr_x)
            visited[curr_x] = True
            dfs(curr_x)
'''

'''
n, m = map(int, input().split())
graph = [list() for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

#print(graph)


visited = [False for _ in range(n+1)]
visited[1] = True
def dfs(node):
    global cnt
    for curr_n in graph[node]:
        if not visited[curr_n]:
            cnt += 1
            visited[curr_n] = True
            dfs(curr_n)

cnt = 0
dfs(1)
print(cnt)
'''

'''
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

start_pos = (0, 0)
target_pos = (n-1, m-1)

#dxs = [-1, 1, 0, 0]
#dys = [0, 0, -1, 1]
dxs = [1, 0]
dys = [0, 1]
ans = 0
visited = [[False for _ in range(m)] for _ in range(n)]
visited_1 = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def dfs_pos(x, y):
    global ans
    visited_1[x][y] = 1
    if (x,y) == target_pos:
        ans = 1
        return
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] == 1 and not visited[nx][ny]:
            visited[nx][ny] = True
            dfs_pos(nx, ny)
            

visited[0][0] = True
dfs_pos(0, 0)
print(ans)
print(visited_1[n-1][m-1])
'''

'''
# 총 마을의 개수와 같은 마을에 있는 사람의 수
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

town = []
dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def dfs(x, y, cnt):
    global max_cnt
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            max_cnt += 1
            dfs(nx, ny, cnt+1)
        
    
for i in range(n):
    for j in range(n):
        if grid[i][j] == 1 and not visited[i][j]:
            visited[i][j] = True
            max_cnt = 1
            dfs(i, j, 1)
            town.append(max_cnt)

town.sort()
print(len(town))
for t in town:
    print(t)
'''


'''
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False  for _ in range(n)] for _ in range(n)]

people_num = 0
people_nums = list()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def dfs(x,y):
    global people_num
    
    dxs, dys = [-1, 1, 0, 0],[0, 0, -1, 1]
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if in_range(nx, ny) and grid[nx][ny] and not visited[nx][ny]:
            visited[nx][ny] = True
            people_num += 1
            dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if grid[i][j] and not visited[i][j]:
            visited[i][j] = True
            people_num = 1
            dfs(i, j)
            people_nums.append(people_num)

people_nums.sort()
print(len(people_nums))
for p in people_nums:
    print(p)
'''

'''
import sys
sys.setrecursionlimit(2500)

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

min_k = n*m+1
max_k = -1

for g in grid:
    for gg in g:
        min_k = min(min_k, gg)
        max_k = max(max_k, gg)

#print(min_k, max_k)

def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end= ' ')
        print()
    print()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, k):
    
    if not in_range(x, y):
        return False
    
    if grid[x][y] <= k or visited[x][y]:
        return False
    
    return True

def dfs(x, y, k):
    global safe_zone_cnt
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if can_go(nx, ny, k):
            visited[nx][ny] = True
            dfs(nx, ny, k)
            
if min_k > 1:
    min_k -= 1
    
safe_zone_k = min_k
safe_zone_cnt = 0

for k in range(min_k, max_k):
    visited = [[False  for _ in range(m)] for _ in range(n)]
    curr_cnt = 0
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                visited[i][j] = True
                curr_cnt += 1
                dfs(i, j, k)
                #print(i, j, k, curr_cnt)
                #print_grid(visited)
                
    
    if safe_zone_cnt < curr_cnt:
        safe_zone_cnt = curr_cnt
        safe_zone_k = k
        
                
print(safe_zone_k, safe_zone_cnt)         
'''

'''
import sys
sys.setrecursionlimit(2500)

n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False  for _ in range(m)] for _ in range(n)]

zone_num = 0

def init_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False

def in_range(x, y):
    return 0 <= x < n and 0 <= y < m


def can_go(x, y, k):
    
    if not in_range(x, y):
        return False
    
    if grid[x][y] <= k or visited[x][y]:
        return False
    
    return True


def dfs(x, y, k):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
   for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if can_go(nx, ny, k):
            visited[nx][ny] = True
            dfs(nx, ny, k)


def get_son_num(k):
    global zone_num
    
    zone_num = 0
    init_visited()
    
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                visited[i][j] = True
                zone_num += 1
                dfs(i, j, k)
        
    
# 가능한 안전 영영의 최솟값은 0
max_zone_num = -1
answer_k = 0
max_height = 100

for k in range(1, max_height+1):
    
    get_son_num(k)
    
    if zone_num > max_zone_num:
        max_zone_num, answer_k = zone_num, k

print(answer_k, max_zone_num)

'''
import sys
sys.setrecursionlimit(2500)

# 2024.04.12 code
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
'''
min_k = n*m+1
max_k = -1

for g in grid:
    for gg in g:
        min_k = min(min_k, gg)
        max_k = max(max_k, gg)
'''
#print(min_k, max_k)

def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end= ' ')
        print()
    print()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def can_go(x, y, k):
    
    if not in_range(x, y):
        return False
    
    if grid[x][y] <= k or visited[x][y]:
        return False
    
    return True

def dfs(x, y, k):
    global safe_zone_cnt
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y+dy
        if can_go(nx, ny, k):
            visited[nx][ny] = True
            dfs(nx, ny, k)
            
            
'''         
if min_k > 1:
    min_k -= 1
''' 
safe_zone_k = 0
safe_zone_cnt = -1

for k in range(1, 101):
    visited = [[False  for _ in range(m)] for _ in range(n)]
    curr_cnt = 0
    for i in range(n):
        for j in range(m):
            if can_go(i, j, k):
                visited[i][j] = True
                curr_cnt += 1
                dfs(i, j, k)
                #print(i, j, k, curr_cnt)
                #print_grid(visited)
                
    
    if safe_zone_cnt < curr_cnt:
        safe_zone_cnt = curr_cnt
        safe_zone_k = k
        
                
print(safe_zone_k, safe_zone_cnt)         





