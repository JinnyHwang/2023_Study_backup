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


def can_go1(x,y,h):
    if not in_range(x,y):
        return False
    
    if visited[x][y]:
        return False
    
    h = abs(h-a[x][y])
    if u <= h and h <= d:
        return True
    
    return False


def can_go(x,y,target):
    if not in_range(x,y) or visited[x][y]:
        return False
    
    diff = abs(target - a[x][y])
    return u <= diff and diff <= d



def bfs():
    global visited
    print('11 : ',id(visited))
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

# 동일 변수를 사용하기 위해서 전역변수 global쓰기
# 아니면 function에서 아예 새로 선
def calc():
    '''
    for i in range(n):
        for j in range(n):
            visited[i][j] = 0
    '''
    global visited
    #print('1 : ',id(visited))
    #visited = [[False for _ in range(n)] for _ in range(n)]
    print('2 : ',id(visited))
    for cc in s_pos:
        visited[cc[0]][cc[1]] = True
        q.append(cc)
    print('3 : ',id(visited))
    bfs()
    print('4 : ',id(visited))
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

