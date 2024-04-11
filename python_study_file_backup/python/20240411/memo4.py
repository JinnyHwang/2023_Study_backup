
dir_mapper = {'U':0, 'D':1, 'R':2, 'L':3}
dxs = [-1, 1, 0, 0]
dys = [0, 0, 1, -1]

n, m, k = map(int, input().split())
apple = [[0 for _ in range(n)] for _ in range(n)]

# 해당 좌표를 지났을 때 방향 값 가지고 있기
snake = [[-1 for _ in range(n)] for _ in range(n)]

# 사과 표시
for _ in range(m):
    x, y = map(int, input().split())
    apple[x-1][y-1] = 1

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end= ' ')
        print()
    print()


x, y = 0, 0
snake_head = (x,y)
snake_tail = (x,y)

time = 0
d_before = 0


cmd_list = []
for _ in range(k):
    dd, p = input().split()
    d = dir_mapper[dd]
    p = int(p)
    cmd_list.append([d,p])

if cmd_list:
    snake[snake_head[0]][snake_head[1]] = cmd_list[0][0]

# 방향 전환 명령
for cmd in cmd_list:
    d, p = cmd
    end_flag = False
        
    print('start')
    print('apple')
    print_grid(apple)
    print('snake')
    print_grid(snake)
    print(snake_head, snake_tail)

    for pi in range(p):
        print('d,p, pi? ', d,p,pi)
        time += 1
        if end_flag:
            break
            
        nx, ny = x+dxs[d], y+dys[d]
        if in_range(nx, ny):
            
            # 뱀의 몸이 있는가?
            if snake[nx][ny] != -1:
                print('!! ', nx, ny , snake_head, snake_tail)
                if (nx, ny) == snake_tail:
                    stx, sty = snake_tail
                    std = snake[stx][sty]
                    snake_tail = (stx+dxs[std], sty+dys[std])
                    snake[stx][sty] = -1
                    
                    # 그냥 이동
                    snake_head = (nx,ny)
                    #snake[nx][ny] = d
                    snake[x][y] = d
                    x, y = nx, ny
                    print('?? ', snake_head, snake_tail)
                    continue
                else:
                    end_flag = True
                    break
            
            # 사과가 있는가?
            if apple[nx][ny] == 1:
                snake_head = (nx,ny)
                #snake[nx][ny] = d
                snake[x][y] = d
                x, y = nx, ny
                apple[nx][ny] = 0
            else:
                # 그냥 이동
                snake_head = (nx,ny)
                #snake[nx][ny] = d
                snake[x][y] = d
                x, y = nx, ny
                
                stx, sty = snake_tail
                std = snake[stx][sty]
                snake_tail = (stx+dxs[std], sty+dys[std])
                snake[stx][sty] = -1
    
        else:
            end_flag = True
            break
        
        print('apple')
        print_grid(apple)
        print('snake')
        print_grid(snake)
        print(snake_head, snake_tail)
        
    if end_flag:
            break


print('end')
print('apple')
print_grid(apple)
print('snake')
print_grid(snake)

print(time)







