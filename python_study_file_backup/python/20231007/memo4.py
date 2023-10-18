


# 방향바꾸는데는 시간 소요 없음
# 방향과 속도 정보가 주어짐

# 구슬의 우선순위는 속도로 결정됨
# 모든 구슬은 구분지을 수 있는 지표가 필요함
# sort 사용 없이 하려면?
# 속도 빠른 구슬 먼저 탐색해서 정렬하고
# k만큼 남기기?


mapper = {'U':0, 'R':1, 'L':2, 'D':3}
dx = [-1, 0, 0, 1]
dy = [0, 1, -1, 0]

n, m, t, k = tuple(map(int, input().split()))
marbles = []

for mi in range(m):
    x, y, d, v = input().split()
    x, y, v = int(x)-1, int(y)-1, int(v)
    marbles.append((x,y,mapper[d],v, mi))

print(marbles)
# 우선순위 높은 구슬을 먼저 탐색하기 위해 속도 값으로 sort
marbles = sorted(marbles, key=lambda x: (x[3], x[4]), reverse=True)
print(marbles)


def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n


def move(marble):
    x, y, d, v, num = marble
    fx, fy, fd = x, y, d
    # 속도만킄 반복
    for _ in range(v):
        nx = fx + dx[fd]
        ny = fy + dy[fd]
        
        if in_range(nx,ny):
            fx, fy = nx, ny
        else:
            fd = 3-fd
            nx = fx + dx[fd]
            ny = fy + dy[fd]
            fx, fy = nx, ny
    return (fx, fy, fd, v, num)


def move_all():
    global marbles
    
    for i, marble in enumerate(marbles):
        marbles[i] = move(marble)


def remove_marbles():

    cnt_ball = [[0 for _ in range(n)] for _ in range(n)]
    next_marbles = []
    
    for marble in marbles:
        x, y = marble[0], marble[1]
        if cnt_ball[x][y] < k:
            cnt_ball[x][y] += 1
            next_marbles.append(marble)
    return next_marbles
    
    


def simulate():
    global marbles

    print(marbles)
    # 모든 구슬 이동
    move_all()
    print(marbles)
    # 우선순위 충돌
    marbles = remove_marbles()
    print(marbles)


for ti in range(t):
    print(ti)
    simulate()


print(len(marbles))



