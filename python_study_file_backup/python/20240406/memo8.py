
# 변수 선언 및 입력
n = int(input())
grid = [[0 for _ in range(n)] for _ in range(n)]

cur_x, cur_y = n//2, n//2
move_dir, move_num = 0, 1

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def end():
    return not in_range(cur_x, cur_y)

def move():
    global  cur_x, cur_y
    
    dxs = [0, -1, 0, 1]
    dys = [1, 0, -1, 0]
    cur_x, cur_y = cur_x + dxs[move_dir], cur_y + dys[move_dir]

# 이동 횟수 정하기
cnt = 1
while not end():
    for _ in range(move_num):
        # 현재 값을 채우고
        grid[cur_x][cur_y] = cnt
        cnt += 1
        
        # 다음 좌표로 이동
        move()
        
        # 이동 했는데 격자 밖이면 종료
        if end():
            break
        
    # 방향 바꾸기
    move_dir = (move_dir+1)%4
    if move_dir == 0 or move_dir == 2:
        move_num += 1
        
# 출력:
for i in range(n):
    for j in range(n):
        print(grid[i][j], end=" ")
    print() 



