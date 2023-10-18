from collections import deque

n, m, k = tuple(map(int,input().split()))
board = [list(map(int,input().split())) for _ in range(n)]
rec = [[0 for _ in range(m)] for _ in range(n)]

# 빛의 공격을 할 때 방문 여부와 경로 방향 기록
vis = [[0 for _ in range(m)] for _ in range(n)]
back_x = [[0 for _ in range(m)] for _ in range(n)]
back_y = [[0 for _ in range(m)] for _ in range(n)]

# 공격과 무관했는지 기록
is_active = [[False for _ in range(m)] for _ in range(n)]

# 살아있는 포탑 관리
live_potop = []

dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]
dxs2 = [0, 0, 0, -1, -1, -1, 1, 1, 1]
dys2 = [0, -1, 1, 0, -1, 1, 0, -1, 1]
# 포탑 객체
class PoTop:
    def __init__(self, x, y, r, p):
        self.x = x
        self.y = y
        self.r = r
        self.p = p


def init():
    global turn
    
    turn += 1
    for i in range(n):
        for j in range(m):
            vis[i][j] = False
            is_active[i][j] = False

def awake():
    global live_potop, board, rec, is_active
    
    # 현재 포탑을 우선순위에 맞게 정렬
    live_potop.sort(key=lambda x:(x.p, -(x.r), -(x.x+x.y), -x.y))
    
    weak_potop = live_potop[0]
    x = weak_potop.x
    y = weak_potop.y
    
    board[x][y] += (n+m)
    rec[x][y] = turn
    weak_potop.p = board[x][y]
    weak_potop.r = rec[x][y]
    is_active[x][y] = True
    
    live_potop[0] = weak_potop
    

def laser_attack():
    global live_potop, board, is_active, back_x, back_y
    
    # 가장 약한 포탑
    weak_potop = live_potop[0]
    wx = weak_potop.x
    wy = weak_potop.y
    wp = weak_potop.p
    
    strong_potop = live_potop[-1]
    sx = strong_potop.x
    sy = strong_potop.y
    
    # 최단 경로 관리
    q = deque()
    vis[wx][wy] = True
    q.append((wx,wy))
    
    res = False
    while q:
        x, y = q.popleft()
        
        # 강한 포탑에 도달할 수 있으면 탐색 종료
        if (x,y) == (sx,sy):
            res = True
            break
        
        # 우 하 좌 상 순서로 방문하며 방문 가능한 포탑을 찾아 queue에 저장
        for dx, dy in zip(dxs, dys):
            nx, ny = (x+dx+n)%n, (y+dy+m)%m
            if vis[nx][ny] or not board[nx][ny]:
                continue
            
            vis[nx][ny] = True
            # 어느 지점에서 왔는지 확인하기 위함
            back_x[nx][ny] = x
            back_y[nx][ny] = y
            q.append((nx,ny))
    
    if res == True:
        # 공격 시작
        board[sx][sy] -= wp
        if board[sx][sy] < 0:
            board[sx][sy] = 0
        is_active[sx][sy] = True
        
        # 기존 경로 역추적
        cx = back_x[sx][sy]
        cy = back_y[sx][sy]
        
        while not ((cx,cy) == (wx,wy)):
            board[cx][cy] -= (wp//2)
        if board[cx][cy] < 0:
            board[cx][cy] = 0
        is_active[cx][cv] = True
        
        ncx = back_x[cx][cy]
        ncy = back_y[cx][cy]
        
        cx, cy = ncx, ncy
    
    return res
        

def bomb_attak():
    # 가장 약한 포탑
    weak_potop = live_potop[0]
    wx = weak_potop.x
    wy = weak_potop.y
    wp = weak_potop.p
    
    strong_potop = live_potop[-1]
    sx = strong_potop.x
    sy = strong_potop.y
    
    # 본인포함 가장 강한 포탑의 모든 방향 확인
    for dx, dy in zip(dxs2,dys2):
        nx = (sx+dx+n)%n
        ny = (sy+dy+m)%m
        
        if (nx,ny) == (wx,wy):
            continue
        
        if (nx,ny) == (sx,sy):
            board[nx][ny] -= wp
            if board[nx][ny] < 0:
                board[nx][ny] = 0
            is_active[nx][ny] = True
        else:
            board[nx][ny] -= (wp//2)
            if board[nx][ny] < 0:
                board[nx][ny] = 0
            is_active[nx][ny] = True
            
def reserve():
    for i in range(n):
        for j in range(m):
            if is_active[i][j] == False:
                if board[i][j]:
                    board[i][j] += 1
    
    

turn = 0
for _ in range(k):
    
    live_potop = []
    for i in range(n):
        for j in range(m):
            if board[i][j]:
                new_potop = PoTop(i, j, rec[i][j], board[i][j])
                live_potop.append(new_potop)

    if len(live_potop) <= 1:
        break
    
    # 초기화 작업
    init()
    
    # 가장 약한 포탑 정비
    awake()
    
    # 레이저 공격
    res = laser_attack()
    
    if not res:
        bomb_attak()
        
    reserve()
    
    
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, board[i][j])
print(board[i][j])





