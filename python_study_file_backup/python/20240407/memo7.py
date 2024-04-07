
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

r, c, m1, m2, m3, m4, d = map(int, input().split())

def print_grid():
    global grid
    for gg in grid:
        for g in gg:
            print(g, end=' ')
        print()
    print()

# 방향 순서
dxs = [-1, -1, 1, 1]
dys = [1, -1, -1, 1]
lens = [m1, m2, m3, m4]

#print_grid()

# 좌표값을 저장
square_pos = []
cx, cy = r-1, c-1
square_pos.append([cx, cy])
for dx, dy, l in zip(dxs, dys, lens):
    for _ in range(l):
        cx, cy = cx+dx, cy+dy
        square_pos.append([cx, cy])
square_pos.pop()
#print(square_pos)

# 회전
new_grid = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        new_grid[i][j] = grid[i][j]

sl = len(square_pos)
# 반시계
if d == 0:
    next_pos = [square_pos[-1]] + square_pos[:sl-1]
# 시계
elif d == 1:
    next_pos = square_pos[1:] + [square_pos[0]]
#print(next_pos)
    
for i, (x, y) in enumerate(square_pos):
    #print(i, x, y)
    nx, ny = next_pos[i]
    new_grid[x][y] = grid[nx][ny]

grid = new_grid
print_grid()


