
# 2024.04.13 code
from collections import deque

n, k, u, d = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

city_list = []
max_city_num = 0

def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end=' ')
        print()

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def can_go_height(nx, ny, city_h):
    next_h = grid[nx][ny]
    
    return u <= abs(next_h - city_h) <= d


def find_can_go_city(city_list):
    dxs, dys = [-1,1,0,0],[0,0,-1,1]
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    for cx, cy in city_list:
        q.append((cx, cy))
        visited[cx][cy] = True
    
    while q:
        cx, cy = q.popleft()
        city_h = grid[cx][cy]
        for dx, dy in zip(dxs, dys):
            nx, ny = cx+dx, cy+dy
            if in_range(nx, ny) and not visited[nx][ny]:
                if can_go_height(nx,ny, city_h):
                    visited[nx][ny] = True
                    q.append((nx,ny))

    #print(city_list)
    #print_grid(visited)
    return sum([1 for i in range(n) for j in range(n) if visited[i][j]])


# k개 도시를 고르기
def select_city_1(i, cnt):
    global city_list, max_city_num
    
    if cnt > k:
        return
    
    if i == n*n:
        if cnt == k:
             # 인접도시 탐색
            curr_city_num = find_can_go_city(city_list)
            print(city_list)
            max_city_num = max(max_city_num, curr_city_num)
        return
    
    x = i//n
    y = i%n
    
    city_list.append((x,y))
    select_city(i+1, cnt+1)
    city_list.pop()
    
    select_city(i+1, cnt)


def select_city(i, cnt):
    global city_list, max_city_num
    
    if i > n*n:
        return
    
    if cnt == k:
        # 인접도시 탐색
        curr_city_num = find_can_go_city(city_list)
        print(city_list)
        max_city_num = max(max_city_num, curr_city_num)
        return
    
    x = i//n
    y = i%n
    
    city_list.append((x,y))
    select_city(i+1, cnt+1)
    city_list.pop()
    
    select_city(i+1, cnt)
    





        
select_city(0,0)  
    
print(max_city_num)

