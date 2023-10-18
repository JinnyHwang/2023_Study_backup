from collections import deque
# 각 칸은 도시, 도시 높이 정보를 가지고 있음
# k개 도시 선택 (조합)
# k개 도시로부터 갈 수 있는 도시의 수 확인
# 두 도시간 높이 차이가 범위 안이면 갈 수 있음
n, k, u, d = tuple(map(int, input().split()))
city_map = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n


dxs = [-1,0,0,1]
dys = [0,-1,1,0]
combi_city = []
max_city = -1
q = deque()
visited = []

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n


def can_go(x,y,h):
    if not in_range(x,y):
        return False
    
    if visited[x][y]:
        return False
    
    h = abs(h-city_map[x][y])
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
            if can_go(nx,ny,city_map[x][y]):
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
    
    for cc in combi_city:
        visited[cc[0]][cc[1]] = True
        q.append(cc)
    
    bfs()
    
    return city_num()
    
    
    


def combi(r, c, cnt):
    global max_city
    
    if cnt == k:
        #cal_res = calc()
        #print(combi_city, cal_res)
        #max_city = max(max_city, cal_res)
        max_city = max(max_city, calc())
        return
    
    # 현재 좌표를 기준으로 (n-1,n-1) 까지 탐색
    for i in range(r,n):
        # 넘어온 좌표부터 진행시키기 위함
        c = c if i == r else 0
        for j in range(c,n):
            combi_city.append((i,j))
            combi(i, j+1, cnt+1)
            combi_city.pop()
            
    
combi(0,0,0)
print(max_city)




