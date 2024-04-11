
'''
n = 4
grid = [list(map(int, input().split())) for _ in range(n)]

def grid_print():
    for gg in grid:
        for g in gg:
            print(g, end=' ')
        print()
    print()


# 1번 중력 작용
# 2번 중력 끝나고 합칠지, 말지
# 숫자가 다르거나, 이미 합쳐졌거나


def move_left():
    
    for i in range(n):
        temp = [0, 0, 0, 0]
        hap = [0, 0, 0, 0]
        temp_idx = 0 # temp에 채워야하는 index
        for j in range(n):
            #print('start', i, temp)
            if grid[i][j] != 0:
                # temp 채우기
                if temp_idx != 0:
                    if temp[temp_idx-1] == grid[i][j] and hap[temp_idx-1] == 0:
                        # 합치기 진행. temp_idx 증가 없음
                        temp[temp_idx-1] = grid[i][j]*2
                        hap[temp_idx-1] = 1
                    else:
                        temp[temp_idx] = grid[i][j]
                        temp_idx += 1
                else:
                    temp[temp_idx] = grid[i][j]
                    temp_idx += 1
            #print('end', i, temp)
                    
        # temp 채우기 끝
        for jj in range(n):
            grid[i][jj] = temp[jj]
            

def move_right():
    
    for i in range(n):
        temp = [0, 0, 0, 0]
        hap = [0, 0, 0, 0]
        temp_idx = n-1 # temp에 채워야하는 index
        for j in range(n-1, -1, -1):
            #print('start', i, temp)
            if grid[i][j] != 0:
                # temp 채우기
                if temp_idx != n-1:
                    if temp[temp_idx+1] == grid[i][j] and hap[temp_idx+1] == 0:
                        # 합치기 진행. temp_idx 증가 없음
                        temp[temp_idx+1] = grid[i][j]*2
                        hap[temp_idx+1] = 1
                    else:
                        temp[temp_idx] = grid[i][j]
                        temp_idx -= 1
                else:
                    temp[temp_idx] = grid[i][j]
                    temp_idx -= 1
            #print('end', i, temp)
                    
        # temp 채우기 끝
        for jj in range(n):
            grid[i][jj] = temp[jj]


def move_up():
    
    for j in range(n):
        temp = [0, 0, 0, 0]
        hap = [0, 0, 0, 0]
        temp_idx = 0 # temp에 채워야하는 index
        for i in range(n):
            #print('start', i, temp)
            if grid[i][j] != 0:
                # temp 채우기
                if temp_idx != 0:
                    if temp[temp_idx-1] == grid[i][j] and hap[temp_idx-1] == 0:
                        # 합치기 진행. temp_idx 증가 없음
                        temp[temp_idx-1] = grid[i][j]*2
                        hap[temp_idx-1] = 1
                    else:
                        temp[temp_idx] = grid[i][j]
                        temp_idx += 1
                else:
                    temp[temp_idx] = grid[i][j]
                    temp_idx += 1
            #print('end', i, temp)
                    
        # temp 채우기 끝
        for ii in range(n):
            grid[ii][j] = temp[ii]
            
            

def move_down():
    
    for j in range(n):
        temp = [0, 0, 0, 0]
        hap = [0, 0, 0, 0]
        temp_idx = n-1 # temp에 채워야하는 index
        for i in range(n-1, -1, -1):
            #print('start', i, temp)
            if grid[i][j] != 0:
                # temp 채우기
                if temp_idx != n-1:
                    if temp[temp_idx+1] == grid[i][j] and hap[temp_idx+1] == 0:
                        # 합치기 진행. temp_idx 증가 없음
                        temp[temp_idx+1] = grid[i][j]*2
                        hap[temp_idx+1] = 1
                    else:
                        temp[temp_idx] = grid[i][j]
                        temp_idx -= 1
                else:
                    temp[temp_idx] = grid[i][j]
                    temp_idx -= 1
            #print('end', i, temp)
                    
        # temp 채우기 끝
        for ii in range(n):
            grid[ii][j] = temp[ii]



cmd = input()
if cmd == 'L':
    move_left()
elif cmd == 'R':
    move_right()
elif cmd == 'U':
    move_up()
elif cmd == 'D':
    move_down()
                
grid_print()
'''

# 해설1
# 4개 방향 다 구현하면 실수함.. 맞음..ㅠㅠㅠ
# 90도 만큼 시계 방향으로 특정 횟수만큼 회전하면서
# 아래 방향으로 떨어트리면 됨...!
# 아래 방향으로 떨어뜨리는 과정만 구현하면 됨

# 2번 이상 합쳐지지 않게 하려면, 가장 최근에 떨어진 숫자를 keep하면 됨!

NONE = -1

n = 4
grid = [list(map(int, input().split())) for _ in range(n)]
next_grid = [[0 for _ in range(n)] for _ in range(n)]

def grid_print():
    for gg in grid:
        for g in gg:
            print(g, end=' ')
        print()
    print()


# grid를 시계 방향으로 90도 회전
def rotate_90_clock():
    # next grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[n-j-1][i]
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]



# grid를 반시계 방향으로 90도 회전
def rotate_90_counterclock():
    # next grid 초기화
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
    
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = grid[j][n-i-1]
    
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]


def drop():
    
    for i in range(n):
        for j in range(n):
            next_grid[i][j] = 0
            
    # 아래 방향으로 떨어뜨림
    for j in range(n):
        keep_num, next_row = NONE, n-1
        for i in range(n-1, -1, -1):
            if grid[i][j] == 0:
                continue
            
            # 떨어진 숫자 없으면 갱신
            # 이 숫자는 지금 입력하지 않음 다음 탐색 때 진행할것
            # 다음 탐색 때 뒤에오는 값이랑 같으면 협쳐서 떨굴것이고
            # 값이 다르면 떨구고 keep num 초기화해서 다음 탐색 진행 할 것
            if keep_num == NONE:
                keep_num = grid[i][j]
            # 최근에 이동했던 숫자가 지금이랑 동일하면 합치기
            elif keep_num == grid[i][j]:
                next_grid[next_row][j] = keep_num*2
                keep_num = NONE # 떨어지지 않고 합쳐졌으므로 NONE
                next_row -= 1
            # 합쳐지지 않고 이동만 함
            else:
                next_grid[next_row][j] = keep_num
                keep_num = grid[i][j]
                next_row -= 1
        
        # 열 탐색이 끝났는데 keep num 값이 남아있으면 채우기
        if keep_num != NONE:
            next_grid[next_row][j] = keep_num
        
    for i in range(n):
        for j in range(n):
            grid[i][j] = next_grid[i][j]
                

def tilt(move_dir):
    
    for _ in range(move_dir):
        rotate_90_clock()
    
    drop()
    
    for _ in range(move_dir):
        rotate_90_counterclock()
    



dir_char = input()
dir_mapper = {'D':0, 'R':1, 'U':2, 'L':3}

tilt(dir_mapper[dir_char])

grid_print()


