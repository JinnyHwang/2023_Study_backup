
n, m = tuple(map(int, input().split()))
a = [[0]*(n+1)] # a[0]에 0만들어있는 리스트
for _ in range(n):
    a.append([0]+list(map(int, input().split())))

def in_range(x,y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def get_max_neighber_pos(curr_x, curr_y):
    # 8개 방향
    dxs = [-1, -1, -1, 0, 1, 1, 1, 0]
    dys = [-1, 0, 1, 1, 1, 0, -1, -1]
    max_num, max_pos = 0, (0,0)

    for dx, dy in zip(dxs, dys):
        nx = curr_x + dx
        ny = curr_y + dy
        if in_range(nx, ny) and max_num < a[nx][ny]:
            max_num = a[nx][ny]
            max_pos = (nx,ny)
    return max_pos

def check_inorder():
    chk_num = 1
    while chk_num <= n*n:
        swap = 0
        for i in range(1, n+1):
            for j in range(1, n+1):
                if a[i][j] == chk_num:
                    swap_x,swap_y  = get_max_neighber_pos(i,j)
                    a[i][j], a[swap_x][swap_y] = a[swap_x][swap_y], a[i][j]
                    swap = 1
                    chk_num += 1
                    break
            if swap:
                break

for _ in range(m):
    check_inorder()

for i in range(1, n+1):
    for j in range(1, n+1):
        print(a[i][j], end=" ")
    print()

