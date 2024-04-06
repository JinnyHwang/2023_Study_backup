
# 북 동 남 서
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

mapper = {'L':-1, 'R':1, 'F':0}

result = 0

N, T = map(int, input().split())

command = input()

grid = [list(map(int, input().split())) for _ in range(N)]

x, y, d = N//2, N//2, 0
result += grid[x][y]

def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

for c in command:
    nd = (d + mapper[c])%4
    if nd == d:
        nx, ny = x + dxs[d], y + dys[d]
        if in_range(nx,ny):
            x, y = nx, ny
            result += grid[x][y]
    else:
        d = nd

print(result)
  

