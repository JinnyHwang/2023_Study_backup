
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
        if (cx,cy) == (x,y):
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
    print(count)
    print(next_count)

    # next_count를 count에 copy
    for i in range(N):
        for j in range(N):
            count[i][j] = next_count[i][j]


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

