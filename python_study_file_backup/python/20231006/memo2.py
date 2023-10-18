
# 상 하 좌 우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

n, m, t = map(int, input().split())

ball_map = []
for _ in range(n):
    ball_map.append(list(map(int, input().split())))
print(ball_map)

# 2차원 격자 상에서 각 칸 단위로 객체를 관리하는 것이 더 좋습니다.
count = [[0 for _ in range(n)] for _ in range(n)]
for _ in range(m):
    x,y = map(int, input().split())
    count[x-1][y-1] = 1
print(count)

for _ in range(t):
    # 동시에 변화가 일어나야 하는 경우에는 새로운 배열을 만들어 주는 것이 항상 좋습니다.
    # step1 Next Count 초기화
    Nxt_count = [[0 for _ in range(n)] for _ in range(n)]

    # step2 구슬 이동
    for x in range(n):
        for y in range(n):
            if count[x][y]:
                max_num = 0
                fx, fy = 0, 0
                for i in range(4):
                    nx = x + dx[i]
                    ny = y + dy[i]
                    if 0 <= nx < n and 0 <= ny < n: 
                        if max_num < ball_map[nx][ny]:
                            max_num = ball_map[nx][ny]
                            fx, fy = nx, ny
                Nxt_count[fx][fy] += 1

    # step3 copy
    for x in range(n):
        for y in range(n):
            if Nxt_count[x][y] == 1:
                count[x][y] = 1
            else:
                count[x][y] = 0
    print(count)
    print(Nxt_count)

ans = 0
for c in count:
    for cc in c:
        if cc:
            ans += 1
print(ans)
