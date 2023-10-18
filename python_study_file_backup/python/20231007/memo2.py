
'''
# 마지막 풀이는 시간초과!

# U,D 0,3 / R,L 1,2
mapper = {'D':0, 'L':1, 'R':2, 'U':3}
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

T = int(input())
marbles = []

def in_range(x,y):
    return 1 <= x and x <= N and 1 <= y and y <= N

def move(marble):
    x, y, d = marble
    nx = x + dx[d]
    ny = y + dy[d]

    if in_range(nx,ny):
        return (nx,ny,d)
    else:
        return (x,y,3-d)

def move_all():
    for i, marble in enumerate(marbles):
        marbles[i] = move(marble)

# 구슬 충돌 확인에 M^2 소요됨
def duplicate_check(index):
    tx, ty, _ = marbles[index]
    # any() : interable type data 중 하나라도 참 data가 있으면 true
    # 비어있으면 false
    # 중복이 없으면 false 반환
    return any([i != index and (x,y) == (tx,ty) for i, (x,y,_) in enumerate(marbles)])

    #for i, (x,y,_) in enumerate(marbles):
    #    if i != index:
    #        if (x,y) == (tx,ty):
    #            return true
    #return False



def remove_marbles():
    global marbles
    
    # 충돌 없는 구슬만 기록
    marbles = [ marble for i, marble in enumerate(marbles) if not duplicate_check(i) ]




def simulate():
    # 모든 구슬 움직이기
    move_all()

    # 충돌 삭제
    remove_marbles()


for _ in range(T):
    marbles = []

    N, M = tuple(map(int, input().split()))
    for _ in range(M):
        x,y,d = input().split()
        x, y = int(x), int(y)
        marbles.append((x,y,mapper[d]))
    
    # 구슬은 2*N번째에 본래 위치로 돌아온다
    for _ in range(2*N):
        simulate()

    print(len(marbles))
'''



MAX_N = 50

# U,D 0,3 / R,L 1,2
mapper = {'D':0, 'L':1, 'R':2, 'U':3}
dx = [1, 0, 0, -1]
dy = [0, -1, 1, 0]

T = int(input())
marbles = []
# 가질 수 있는 최대 크기 board
marble_cnt = [[0 for _ in range(MAX_N+1)] for _ in range(MAX_N+1)]

def in_range(x,y):
    return 1 <= x and x <= N and 1 <= y and y <= N



def move(marble):
    x, y, d = marble
    nx = x + dx[d]
    ny = y + dy[d]

    if in_range(nx,ny):
        return (nx,ny,d)
    else:
        return (x,y,3-d)

def move_all():
    for i, marble in enumerate(marbles):
        marbles[i] = move(marble)

def duplicate_check(index):
    tx, ty, _ = marbles[index]
    return marble_cnt[tx][ty] >= 2


def remove_marbles():
    global marbles

    # 현재 구슬 위치에 count 증가
    for x, y, _ in marbles:
        marble_cnt[x][y] += 1
    
    # 충돌 없는 구슬만 기록
    remaine_marbles = [ marble for i, marble in enumerate(marbles) if not duplicate_check(i) ]

    # count 초기화
    for x, y, _ in marbles:
        marble_cnt[x][y] -= 1

    marbles = remaine_marbles


def simulate():
    # 모든 구슬 움직이기
    move_all()

    # 충돌 삭제
    remove_marbles()


for _ in range(T):
    marbles = []

    N, M = tuple(map(int, input().split()))
    for _ in range(M):
        x,y,d = input().split()
        x, y = int(x), int(y)
        marbles.append((x,y,mapper[d]))
    
    # 구슬은 2*N번째에 본래 위치로 돌아온다
    for _ in range(2*N):
        simulate()

    print(len(marbles))



'''
# 해설의 runtime은?
BLANK = -1
COLLIDE = -2

# 변수 선언 및 입력
t = int(input())
n, m = 0, 0
curr_dir = list()
next_dir = list()

# 입력으로 주어진 방향을 정의한 dx, dy에 맞도록
# 변환하는데 쓰이는 dict를 정의합니다.
mapper = {
    'U': 0,
    'R': 1,
    'L': 2,
    'D': 3
}


# 해당 위치가 격자 안에 들어와 있는지 확인합니다.
def in_range(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 해당 위치에 dir 방향을 갖는 구슬이 새롭게 추가되는 경우에 대한
# 처리를 합니다.
def update_next_dir(x, y, move_dir):
    # 빈 곳이었다면 해당 구슬을 넣어주고
    if next_dir[x][y] == BLANK:
        next_dir[x][y] = move_dir
    # 빈 곳이 아니었다면 이미 다른 구슬이 놓여져 있는 것이므로
    # 충돌 표시를 해줍니다.
    else:
        next_dir[x][y] = COLLIDE


def move(x, y, move_dir):
    # 구슬이 벽에 부딪혔을 때의 처리를 간단히 하기 위해
    # dir 기준 0, 3이 대칭 1, 2가 대칭이 되도록 설정합니다.
    dxs, dys = [-1, 0, 0, 1], [0, 1, -1, 0]
    
    # 바로 앞에 벽이 있는지를 판단합니다.
    nx, ny = x + dxs[move_dir], y + dys[move_dir]
    
    # Case 1 : 벽이 없는 경우에는 그대로 한 칸 전진합니다.
    # 따라서 그 다음 위치에 같은 방향을 갖는 구슬이 있게 됩니다.
    if in_range(nx, ny):
        update_next_dir(nx, ny, move_dir)
        
    # Case 2 : 벽이 있는 경우에는 방향을 반대로 틀어줍니다.
    # 따라서 같은 위치에 반대 방향을 갖는 구슬이 있게 됩니다.
    else:
        update_next_dir(x, y, 3 - move_dir)   


# 구슬을 전부 한 번씩 움직여봅니다.
def move_all():
    global next_dir
    
    # 그 다음 각 위치에서의 방향들을 전부 초기화 해놓습니다.
    next_dir = [
        [BLANK for _ in range(n + 1)]
        for _ in range(n + 1)
    ]
    
    # (i, j) 위치에 구슬이 있는경우
    # 움직임을 시도해보고, 그 결과를 전부 next_dir에 기록합니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if curr_dir[i][j] != BLANK:
                move(i, j, curr_dir[i][j])
    
    # next_dir 값을 다시 curr_dir에 복사합니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            curr_dir[i][j] = next_dir[i][j]


# 충돌이 일어나는 구슬을 전부 지워줍니다.
def remove_duplicate_marbles():
    # 충돌이 일어난 구슬들이 있는 위치만 빈 곳으로 설정하면 됩니다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            if curr_dir[i][j] == COLLIDE:
                curr_dir[i][j] = BLANK


# 조건에 맞춰 시뮬레이션을 진행합니다.
def simulate():
    # Step1
    # 구슬을 전부 한 번씩 움직여봅니다.
    move_all()
    
    # Step2
    # 움직임 이후에 충돌이 일어나는 구슬들을 골라 목록에서 지워줍니다.
    remove_duplicate_marbles()


for _ in range(t):
    # 입력
    n, m = tuple(map(int, input().split()))
    
    # 새로운 테스트 케이스가 시작될때마다 기존에 사용하던 값들을 초기화해줍니다.
    curr_dir = [
        [BLANK for _ in range(n + 1)]
        for _ in range(n + 1)
    ]
    
    for _ in range(m):
        x, y, d = tuple(input().split())
        x, y = int(x), int(y)
        curr_dir[x][y] = mapper[d]
    
    # 2 * n번 이후에는 충돌이 절대 일어날 수 없으므로
    # 시뮬레이션을 총 2 * n번 진행합니다.
    for _ in range(2 * n):
        simulate()
        
    marble_cnt = sum([
        curr_dir[i][j] != BLANK
        for i in range(1, n + 1)
        for j in range(1, n + 1)
    ])
    
    # 출력
    print(marble_cnt)
'''

'''
구슬의 개수 M이 격자의 크기에 해당하는 N*N만큼 커질 수 있기 때문에
구슬의 목록을 격차 내에 직접 표시하여 관리해도
시간복잡도, 공간복잡도 모두 크게 차이나지 않음
격자 내에서 구슬의 상태를 관리
'''
'''
# 방향값을 0,1,2,3으로 사용하기 때문에 빈칸은 -1로 표기
BLANK = -1
COLLIDE = -2

T = int(input())
N, M = 0, 0
#N, M = tuple(map(int, input().split()))
curr_dir = list()
next_dir = list()


# U,D 0,3 / L,R 1,2 반대방향을 대칭으로 처기
# 방향 틀기는 3-dir
mapper = {'U':0, 'L':1, 'R':2, 'D':3}
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def in_range(x,y):
    return 0 <= x and x < N and 0 <= y and y < N


# next_dir을 채움
def set_next_dir(x,y,d):
    #print('set_next_dir?', x,y,d)
    if next_dir[x][y] == BLANK:
        next_dir[x][y] = d
    else:
        next_dir[x][y] = COLLIDE


def move(x,y,d):
    
    nx = x + dx[d]
    ny = y + dy[d]
    #print('nx,ny?',nx,ny)
    
    # 벽이 없다 전진
    if in_range(nx,ny):
        set_next_dir(nx,ny,d)
    # 벽이 있다 방향 틀기
    else:
        set_next_dir(x,y,3-d)
        
    

def move_all():
    global next_dir
    next_dir = [[BLANK for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if curr_dir[i][j] != BLANK:
                move(i,j,curr_dir[i][j])
                
    #print(curr_dir)
    #print(next_dir)
    
    for i in range(N):
        for j in range(N):
            if next_dir[i][j] == BLANK or next_dir[i][j] == COLLIDE:
                curr_dir[i][j] = BLANK
            else:
                curr_dir[i][j] = next_dir[i][j]



for _ in range(T):
    
    N, M = tuple(map(int, input().split()))
    
    # 초기화
    curr_dir = [[BLANK for _ in range(N)] for _ in range(N)]
    
    for _ in range(M):
        x, y, d = tuple(input().split())
        x, y = int(x)-1, int(y)-1
        curr_dir[x][y] = mapper[d]
    
    #print(T)
    #print(curr_dir)
    #print(next_dir)
    
    # 아주 오랜시간이 흐른 후..?
    # 구슬을 2*N번 반복하면 구슬은 다시 초기 위치, 초기 방향을 가지기 때문에
    # 2*N번 이후에는 충돌이 절대 일어날 수 없음
    for _ in range(2*N):
        move_all()
    
    
    ans = sum(curr_dir[x][y] != BLANK for x in range(N) for y in range(N))
    print(ans)

'''



'''
# 배열이 아닌 dictionary로 풀어보기
# 남은 구슬은?
# 구슬 좌표, 구슬 방향

T = int(input())
N, M = map(int, input().split())

# U D R L -> 0 1 2 3
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

balls = {}
for _ in range(M):
    x, y, ds = input().split()
    x = int(x) -1
    y = int(y) -1
    # 방향을 key값으로 구슬 좌표 기록
    balls[ds] = balls.get(ds, []) + [[x,y]]
'''

'''
T = int(input())
N, M = map(int, input().split())

# U D R L -> 0 1 2 3
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]

count = [[0 for _ in range(N)] for _ in range(N)]
next_count = [[0 for _ in range(N)] for _ in range(N)]
next_count_col = []

for _ in range(M):
    x, y, ds = input().split()
    x = int(x)-1
    y = int(y)-1
    if ds == 'U':
        count[x][y] = 0
    elif ds == 'D':
        count[x][y] = 1
    elif ds == 'R':
        count[x][y] = 2
    elif ds == 'L':
        count[x][y] = 3

def in_range(x,y):
    return 0 <= x and x < N and 0 <= y and y < N

def change_d(d):
    if d == 0 or d == 2:
        return d+1
    else:
        return d-1

def make_next(x,y,d):

    # 충돌포지션 확인
    for cx, cy in next_count_col:
        if cx,cy == x,y:
            return

    # 충돌 없으면 d 정보 넣어줌
    if next_count[x][y] == 0:
        next_count[x][y] = d
    # 충돌발생 d정보 없애고 충돌포지션 update
    else:
        next_count[x][y] = 0
        next_count_col.append((x,y))


def move_ball(x, y):
    d = count[x][y]
    nx = x + dx[d]
    ny = y + dy[d]

    if in_range(nx, ny):
        make_next(nx, ny, d)
    else: # 벽쿵
        d = change_d(d)
        nx = x + dx[d]
        ny = y + dy[d]
        make_next(nx, ny, d)


def move_all_ball():
    for i in range(N):
        for j in range(M):
            if count[i][j]:
                move_ball(x, y) # next_count에 다음 움직임 저장


def simulate():
    # next 정보 초기화
    next_count = [[0 for _ in range(N)] for _ in range(N)]
    next_count_col = []

    # 구슬 이동
    move_all_ball()

    # next_count를 count에 copy
    for i in range(N):
        for j in range(N):
            count[i][j] = next_count[i][j]

# 아주 오랜시간이 흐른 후 -> 배열로 안됨
def longtime():
    for _ in range(5):
        simulate()

def count_ball():
    ans = 0
    for i in range(N):
        for j in range(N):
            if count[i][j]:
                ans += 1
    print(ans)

def game():
    for _ in range(T):
        longtime()
        count_ball()
'''
