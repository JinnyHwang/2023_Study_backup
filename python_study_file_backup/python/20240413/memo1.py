
# 0 이 갈 수 있는 구간을 탐색
# 0으로 갈 수 있고 1로도 갈 수 있는데
# 0을 기준으로 4면이 다 1이면 갈 수 없음

# 값이 항상 0인 (0,0)을 기준으로 탐색

'''
from collections import deque

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(m)] for _ in range(n)]
visited = [[False  for _ in range(m)] for _ in range(n)]
not_melt_water = []
start_pos = (0,0)
q = deque()

dxs = [-1, 1, 0, 0]
dys = [0, 0, -1, 1]

def print_grid(grid):
    for i in range(n):
        for j in range(m):
            print(grid[i][j], end=' ')
        print()
    print()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < m

def around_ice(water_zone_list):
    
    for ix, iy in water_zone_list:
        for dx, dy in zip(dxs, dys):
            nx, ny = ix+dx, iy+dy
            # 테두리는 water_zone_list에 없기 때문에 return False됨
            if in_range(nx,ny) and grid[nx][ny] == 0:
                if not (nx,ny) in water_zone_list:
                    return False
    return True
        

 
def delete_not_melt_wafer(wafer_list):
    global q
    
    #water_zone = deque()
    wafer_zone_visited = [[False  for _ in range(m)] for _ in range(n)]
    for w in wafer_list:
        wx, wy = w
        if wx == 0 or wx == n-1 or wy == 0 or wy == m-1:
            q.append((wx,wy))
            wafer_zone_visited[wx][wy] = True
            continue
        
        if not wafer_zone_visited[wx][wy]:
            water_zone = deque()
            water_zone_list = []
            water_zone.append((wx,wy))
            wafer_zone_visited[wx][wy] = True
            while water_zone:
                x, y = water_zone.popleft()
                print('water_zone', x,y)
                water_zone_list.append((x,y))
                
                for dx, dy in zip(dxs, dys):
                    nx, ny = x+dx, y+dy
                    #print('??', nx,ny, in_range(nx,ny), grid[nx][ny] == 0, wafer_zone_visited[nx][ny])
                    if in_range(nx,ny) and grid[nx][ny] == 0 and not wafer_zone_visited[nx][ny]:
                        water_zone.append((nx,ny))
                        wafer_zone_visited[nx][ny] = True
            
            print('water_zone_list', water_zone_list, wx, wy)
            print_grid(wafer_zone_visited)
            print(around_ice(water_zone_list))
            if around_ice(water_zone_list) == True:
                continue
            else:
                for ai in water_zone_list:
                    q.append(ai)

    

def bfs():
    
    while q:
        
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if in_range(nx,ny) and not visited[nx][ny]:
                next_grid[nx][ny] = 0
                visited[nx][ny] = True
    
        # 빙하 못녹이는 물을 pass
        #if can_melt_water(x, y):
        #    for dx, dy in zip(dxs, dys):
        #        nx, ny = x+dx, y+dy
        #        if in_range(nx,ny) and not visited[nx][ny]:
        #            next_grid[nx][ny] = 0
        #            visited[nx][ny] = True
        #else:
        #    print('not melt', x, y)
        
        

befor_ice = sum([ 1 for i in range(n) for j in range(m) if grid[i][j]])  
for t in range(1, 4001):
    
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            next_grid[i][j] = grid[i][j]
    
    wafer_list = []
    for i in range(n):
        for j in range(m):
            if grid[i][j] == 0 and not visited[i][j]:
                visited[i][j] = True
                wafer_list.append((i, j))
    
    
    #not_melt_water = []
    #make_not_melt_water_list()
    
    q = deque()
    print(wafer_list)
    delete_not_melt_wafer(wafer_list)
    
    print('before bfs')
    print(q)
    print_grid(grid)
    print_grid(next_grid)
    print_grid(visited)
        
    bfs()
    
    print('after bfs')
    print(q)
    print_grid(grid)
    print_grid(next_grid)
    print_grid(visited)
    
    for i in range(n):
        for j in range(m):
            grid[i][j] = next_grid[i][j]
               
                
    ice = sum([ 1 for i in range(n) for j in range(m) if grid[i][j]])
    if ice == 0:
        break
    else:
        befor_ice = ice



print(t, befor_ice)
'''

'''
from collections import deque
import enum
#from enum import IntEnum

# enum.Enum을 상속하여 만든 Enum 자료형에는 다음처럼 name과 value 속성으로 접근할 수 있다.
class Element(enum.Enum):
#class Element(IntEnum):
    WATER = 0
    GLACIER = 1

# Enum을 상송해서 만든 자료형 Element
#print(Element.WATER.value)
#print(Element.WATER.name)
#print(Element.GLACIER.value)
#print(Element.GLACIER.name)


n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(n)]

q = deque()
glaciers_to_melt = deque()
visited = [[False for _ in range(m)] for _ in range(n)]
cnt = 0

# 소요 시간과 가장 마지막으로 녹은 빙하의 수를 저장합니다.
elapsed_time = 0
last_melt_cnt = 0

dxs, dys = [-1, 1, 0, 0], [0, 0, -1, 1]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m


def can_go(x,y):
    return in_range(x,y) and a[x][y] == Element.WATER.value and not visited[x][y]


def is_glacier(x,y):
    return in_range(x,y) and a[x][y] == Element.GLACIER.value and not visited[x][y]


# visited 배열 초기화
def init_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False


# 빙하에 둘러쌓여있지 않은 물을 전부 구하는 bfs
# (0,0)에서 시작하면 빙하에 둘러 쌓여있지 않은 물을 모두 탐색할 수 있음
# 지니어스..?
def bfs():
    init_visited()
    
    q.append((0,0))
    visited[0][0] = True
    
    while q:
        x, y = q.popleft()
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            if can_go(nx,ny):
                q.append((nx,ny))
                visited[nx][ny] = True



# 빙하에 둘러쌓여있지 않은 물이 있는가?
def outside_water_exist_in_neighbor(x, y):
    for dx, dy in zip(dxs, dys):
        nx, ny = x+dx, y + dy
        if in_range(nx, ny) and visited[nx][ny]:
            return True
    return False


def melt():
    global last_melt_cnt
    
    for i in range(n):
        for j in range(m):
            if a[i][j] == Element.GLACIER.value and outside_water_exist_in_neighbor(i,j):
                 a[i][j] == Element.WATER.value
                 last_melt_cnt += 1
    

def simulate():
    global elapsed_time, last_melt_cnt
    
    elapsed_time += 1
    last_melt_cnt = 0
    
    bfs()
    
    melt()
    
    
def glacier_exist():
    for i in range(n):
        for j in range(m):
            if a[i][j] == Element.GLACIER.value:
                return True
    return False


while True:
    simulate()
    
    if not glacier_exist():
        break

print(elapsed_time, last_melt_cnt)
'''

from collections import deque
import enum

class Element(enum.Enum):
    WATER = 0
    GLACIER = 1
    
# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))

a = [
    list(map(int, input().split()))
    for _ in range(n)
]

# bfs에 필요한 변수들 입니다.
q = deque()
glaciers_to_melt = deque()
visited = [
    [False for _ in range(m)]
    for _ in range(n)
]
cnt = 0

# 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

# 소요 시간과 가장 마지막으로 녹은 빙하의 수를 저장합니다.
elapsed_time = 0
last_melt_cnt = 0

# 주어진 위치가 격자를 벗어나는지 여부를 반환합니다.
def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < m

# 범위를 벗어나지 않으면서 물이여야 하고 방문한적이 
# 없어야 갈 수 있습니다.
def can_go(x, y):
    return in_range(x, y) and a[x][y] == Element.WATER.value and not visited[x][y]


def is_glacier(x, y):
    return in_range(x, y) and a[x][y] == Element.GLACIER.value and not visited[x][y]


# visited 배열을 초기화합니다.
def initialize():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            
            
# 빙하에 둘러쌓여 있지 않은 물들을 전부 구해주는 BFS입니다.
# 문제에서 가장자리는 전부 물로 주어진다 했기 때문에
# 항상 (0, 0)에서 시작하여 탐색을 진행하면
# 빙하에 둘러쌓여 있지 않은 물들은 전부 visited 처리가 됩니다.
def bfs():
    # BFS 함수가 여러 번 호출되므로
    # 사용하기 전에 visited 배열을 초기화 해줍니다.
    initialize()
    
    # 항상 (0, 0)에서 시작합니다.
    q.append((0, 0))
    visited[0][0] = True
    
    while q:
        # queue에서 가장 먼저 들어온 원소를 뺍니다.
        x, y = q.popleft()
        
        # queue에서 뺀 원소의 위치를 기준으로 네 방향을 확인합니다.
        for dx, dy in zip(dxs, dys):
            new_x, new_y = x + dx, y + dy

            # 더 갈 수 있는 곳이라면 Queue에 추가합니다.
            if can_go(new_x, new_y):
                q.append((new_x, new_y))
                visited[new_x][new_y] = True

                
# 현재 위치를 기준으로 인접한 영역에
# 빙하에 둘러쌓여 있지 않은 물이 있는지를 판단합니다.   
def outside_water_exist_in_neighbor(x, y):
    for dx, dy in zip(dxs, dys):
        new_x, new_y = x + dx, y + dy
        if in_range(new_x, new_y) and visited[new_x][new_y]:
            return True
        
    return False


# 인접한 영역에 빙하에 둘러쌓여 있지 않은 물이 있는 빙하를 찾아
# 녹여줍니다.
def melt():
    global last_melt_cnt
    
    for i in range(n):
        for j in range(m):
            if a[i][j] == Element.GLACIER.value and \
                    outside_water_exist_in_neighbor(i, j):
                a[i][j] = Element.WATER.value
                last_melt_cnt += 1
                
                
# 빙하를 한 번 녹입니다.
def simulate():
    global elapsed_time, last_melt_cnt
    
    elapsed_time += 1
    last_melt_cnt = 0
    
    # 빙하에 둘러쌓여 있지 않은 물의 위치를 전부
    # visited로 체크합니다.
    bfs()
    
    # 인접한 영역에 빙하에 둘러쌓여 있지 않은 물이 있는 빙하를 찾아
    # 녹여줍니다.
    melt()
    

# 빙하가 아직 남아있는지 확인합니다.
def glacier_exist():
    for i in range(n):
        for j in range(m):
            if a[i][j] == Element.GLACIER.value:
                return True
    return False


while True:
    simulate()
    
    # 빙하가 존재하는 한 계속 빙하를 녹입니다.
    if not glacier_exist():
        break
        
print(elapsed_time, last_melt_cnt)


