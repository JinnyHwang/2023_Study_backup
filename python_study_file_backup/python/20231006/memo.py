
# 코테 문제 따라잡기

# 변수 선언 및 입력
n, m, t = tuple(map(int, input().split()))
a = [ [0] * (n+1) ]
print(a)
for _ in range(n):
    a.append([0] + list(map(int, input().split())))
print(a)

count = [[0 for _ in range(n+1)] for _ in range(n+1)]
next_count = [[0 for _ in range(n+1)] for _ in range(n+1)]

# 범위가 격자 안에 들어가는가?
def in_range(x,y):
    return 1 <= x and x <= n and 1 <= y and y <= n

# 인접한 곳 중 가장 값이 큰 위치 반환
def get_max_neighbor_pos(curr_x, curr_y):
    dxs, dys = [-1,1,0,0], [0,0,-1,1]
    max_num, max_pos = 0, (0,0)
    
    for dx, dy in zip(dxs, dys):
        nx = curr_x + dx
        ny = curr_y + dy
        
        if in_range(nx,ny) and max_num < a[nx][ny]:
            max_num = a[nx][ny]
            max_pos = (nx,ny)
    return max_pos

# (x,y)위치에 있는 구슬 옮기기
def move(x,y):
    nx, ny = get_max_neighbor_pos(x,y)
    next_count[nx][ny] += 1

# 구슬을 하나씩 움직이기
def move_all():
    
    #  next count 초기화
    for i in range(1, n+1):
        for j in range(1, n+1):
            next_count[i][j] = 0
    
    # 구슬이 있으면 move
    for i in range(1, n+1):
        for j in range(1, n+1):
            if count[i][j]:
                move(i,j) # next에 결과 기록
    
    # count에 값 복사
    for i in range(1, n+1):
        for j in range(1, n+1):
            if next_count[i][j] == 1:
                count[i][j] = next_count[i][j]
            else:
                count[i][j] = 0

for _ in range(m):
    x,y = tuple(map(int, input().split()))
    count[x][y] = 1
'''
for _ in range(t):
    move_all()

ans = 0
for c in count:
    for cc in c:
        ans += cc
print(ans)

'''







