

#map = input()

#(A, B) - A: 북쪽에서 떨어진 칸의 개수 / B: 서쪽에서 떨어진 칸의 개수

# 0: 북쪽 / 1: 동쪽 / 2: 남쪽 / 3: 서쪽
#direct = [ (-1, 0), (0, 1), (1, 0), (0, -1) ]

# 맵 크기를 받음. n*m - n: 세로 / m: 가로
n, m = map(int, input().split())

# 방문 위치를 저장하기 위함
# d[m][n] 배열 0으로 초기화
d = [ [0]*m for _ in range(n) ]
print(d)

# 캐릭터의 위치와 방향.
x, y, direction = map(int, input().split())

#현재 위치 방문 표시
d[x][y] = 1

#전체 맵 입력 받기
# 0: 육지 / 1: 바다
map_array = []
for i in range(n) :
    map_array.append( list( map(int, input().split()) ) )

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# 0, 1, 2, 3 순서가 왼쪽으로 도는 방향(반시계 방향)
# 왼쪽으로 도는 함수
# 나는 +1이 왼쪽 방향으로 회전하는거라 생각.
# 그런데 답지는 -1로 되어 있네..
def turn_left() :
    global direction
    direction += 1
    if direction >= 4 :
        direction = 0
#p.121부터!

# 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향 90도)부터 차례로 갈 곳을 정함
# 캐릭터의 바로 왼쪽 방향에 가보지 않는 길이 존재 : 왼쪽 방향 회전 후 전진
# 왼쪽 방향에 가보지 않은 칸이 없다면, 회전만 하고 끝
# 4방향 모두 가본 길 or 바다일 경우 바라보는 방향 유지. 한 칸 뒤로.
# 뒤쪽 방향이 바다인 경우 움직임 멈춤

# 시뮬레이션시작

# 캐릭터가 방문한 칸의 수
count = 1

# 제자리 회전 횟수
turn_time = 0

while True :
    # 왼쪽 회전
    turn_left()
    nx = x + dx[direction]
    ny = y + dy[direction]

    # 왼쪽 회전 후 길이 가보지 않은 육지인 경우
    if d[nx][ny] == 0 and map_array[nx][ny] == 0 :
        x = nx
        y = ny
        d[nx][ny] = 1
        count += 1
        turn_time = 0
        continue
    
    # 왼쪽 회전 후 길이 가본길 or 바다
    else :
        turn_time += 1
        
        if turn_time == 4 :
            bx = x - dx[direction]
            by = y - dy[direction]
            if map_array[bx][by] == 0 :
                x = bx
                y = by
            else :
                break
            turn_time = 0

print(count)
