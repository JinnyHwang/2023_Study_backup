
# 집의 높이에 대한 범위가 1~100까지
# 특정 높이 만큼 비가 왔다 가정하고 dfs활용하여 안전영역개수 count
# 중복 영역에 대해 탐색하지 않음
# 각 위치에 대하여 N*M 시간복잡도를 가짐
import sys
sys.setrecursionlimit(2500) # 재귀 사용할 때 setrecursionlimit() 사용

# 변수 선언 및 입력
n, m = tuple(map(int, input().split()))
grid = [list(map(int, input().split())) for _ in range(n)]
visited = [[False for _ in range(m)] for _ in range(n)]
zone_num = 0
#print(grid)

# visited 배열을 초기화해줍니다.
def initialize_visited():
    for i in range(n):
        for j in range(m):
            visited[i][j] = False
            
def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m

def can_go(x,y,k):
    if not in_range(x,y):
        return False
    
    # 그러네...
    # 따로 만들지 않고  grid[x][y] <= k 이 조건을 사용
    if visited[x][y] or grid[x][y] <= k:
        return False
    
    return True

def dfs(x,y,k):
    
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]
    
    for dx,dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx,ny,k):
            visited[nx][ny] = True
            dfs(nx,ny,k)


# k값에 대해 영역개수 구하기
def get_zone_num(k):
    global zone_num, visited
    
    zone_num = 0
    visited = [[False for _ in range(m)] for _ in range(n)]
    
    for i in range(n):
        for j in range(m):
            if can_go(i,j,k):
                visited[i][j] = True
                zone_num += 1
                #print(zone_num, i,j,k)
                dfs(i,j,k)
                


max_zone_num = -1
answer_k = 0
max_height = 100

# 예외 상황을 최소화할 수 있는 코드를 만들자
for k in range(1,max_height+1):
    get_zone_num(k)
    #print(zone_num)
    if zone_num > max_zone_num:
        max_zone_num = zone_num
        answer_k = k
        
print(answer_k, max_zone_num)




