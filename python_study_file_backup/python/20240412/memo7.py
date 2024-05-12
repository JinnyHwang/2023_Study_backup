
from collections import deque

# m개 돌을 치우는 경우의 수
# m개 돌을 치운 격자에서 시작점 k개로 탐색하는 구역 개수

n, k, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(n)] for _ in range(n)]

#q = deque()
print('start pos')
start_pos = []
for _ in range(k):
    r, c = map(int, input().split())
    r, c = r-1, c-1
    start_pos.append((r,c))
    print(r,c)
    #q.append((r,c))
    #visited[r][c] = True


    
    
# m개 돌을 치워 만들 수 있는 new_grid
rock_list = []
new_grid = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_grid[i][j] = grid[i][j]
        if grid[i][j] == 1:
            rock_list.append((i,j))
            
def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end=' ')
        print()
    

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n



def find_zone_size(new_grid):
    visited = [[False for _ in range(n)] for _ in range(n)]
    q = deque()
    
    for r,c in start_pos:
        q.append((r,c))
        visited[r][c] = True
    
    dxs, dys = [-1, 1, 0, 0],[0, 0, -1, 1]
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx, ny) and not visited[nx][ny] and not new_grid[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny))
            
    ans = sum([ 1 for i in range(n) for j in range(n) if visited[i][j]])
    print('visited')
    print_grid(visited)
    return ans



max_zone = 0

# new_grid[i][j]에 0을 넣었다 다시 1을 넣었다
def find_rock_combi(cur_idx, cnt):
    global max_zone
    
    if cur_idx == len(rock_list):
        # 돌 m개 선택한 경우
        if cnt == m:
            # bfs시작!
            print_grid(new_grid)
            zone_cnt = find_zone_size(new_grid)
            print(zone_cnt)
            max_zone = max(max_zone, zone_cnt)
        return
    
    x, y = rock_list[cur_idx]
    new_grid[x][y] = 0
    find_rock_combi(cur_idx+1, cnt+1)
    new_grid[x][y] = 1
    
    find_rock_combi(cur_idx+1, cnt)
    



find_rock_combi(0, 0)

print(max_zone)
