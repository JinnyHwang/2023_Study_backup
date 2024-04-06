
n, t = tuple(map(int, input().split()))
commands = input()
board = [list(map(int, input().split())) for _ in range(n)]

ans = 0

# 초기 위치 선정
x, y, move_dir = n//2, n//2, 0

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n


def simulate():
    global ans
    global x, y, move_dir
    
    dxs = [-1, 0, 1, 0]
    dys = [0, 1, 0, -1]
    
    for command in commands:
        if command == 'R':
            move_dir = (move_dir+1)%4
        elif command == 'L':
            move_dir = (move_dir-1)%4
        else:
            nx, ny = x + dxs[move_dir], y + dys[move_dir]
            if in_range(nx, ny):
                ans += board[nx][ny]
                x, y = nx, ny


ans += board[x][y]
simulate()

print(ans)
