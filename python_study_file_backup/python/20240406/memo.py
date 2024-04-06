
# 색칠할 칸이 주어지면 그 칸을 틸한 후 편안한 상태인지 계속 확인
# (1,1) ~ (N,N)

N, M = map(int, input().split())

grid = [[0 for _ in range(N+1)] for _ in range(N+1)]

dxs = [0, -1, 1, 0]
dys = [1, 0, 0, -1]

def in_range(x, y):
    return 1 <= x <= N and 1 <= y <= N

def comfortable_sts(x, y):
    cnt = 0
    for dx, dy in zip(dxs, dys):
        nx, ny = x + dx, y + dy
        if in_range(nx, ny) and grid[nx][ny] != 0:
            cnt += 1
    if cnt == 3:
        return True
    else:
        return False


for _ in range(M):
    r, c = map(int, input().split())
    grid[r][c] = 1
    if comfortable_sts(r,c):
        print(1)
    else:
        print(0)










