
n, m = map(int, input().split())
answer = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]
x, y = 0, 0           # 시작은 (0, 0) 입니다.
dir_num = 1           # 0: 오른쪽, 1: 아래쪽, 2: 왼쪽, 3: 위쪽

answer[x][y] = 1

for i in range(2, n*m+1):
    # 나아갈 수 있을 때 까지 방향을 바꿔가면서 확인
    while True:
        nx, ny = x + dxs[dir_num], y + dys[dir_num]
        
        if in_range(nx, ny) and answer[nx][ny] == 0:
            x,y = nx,ny
            answer[nx][ny]=i
            break
        else:
            dir_num = (dir_num+3)%4

for i in range(n):
    for j in range(m):
        print(answer[i][j], end=' ')
    print()

