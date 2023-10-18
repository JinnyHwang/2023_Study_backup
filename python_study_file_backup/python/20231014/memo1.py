
n, m, k = tuple(map(int, input().split()))
game_map = [[0 for _ in range(n+1)]]
#print(game_map)
game_map += [[0]+list(map(int, input().split())) for _ in range(n)]
#print(game_map)

# 탈출하면 좌표 (-1,-1)로 바꾸기
people = [tuple(map(int, input().split())) for _ in range(m)]
#print(people)

exit_pos = tuple(map(int, input().split()))
#print(exit_pos)


def in_range(x,y):
    return 1 <= x and x <= n and 1 <= y and y <= n


def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if game_map[x][y] != 0:
        return False
    
    return True


def cal_dist(pos1,pos2):
    x1,y1 = pos1
    x2,y2 = pos2
    return abs(x1-x2)+abs(y1-y2)

def more_min_dist(curr_pos, next_pos):
    #exit_x,exit_y = exit_pos
    #curr_x,curr_y = curr_pos
    #next_x,next_y = next_pos
    
    #curr_dist = abs(exit_x-curr_x)+abs(exit_y-curr_y)
    #next_dist = abs(exit_x-next_x)+abs(exit_y-next_y)
    
    curr_dist = cal_dist(exit_pos, curr_pos)
    next_dist = cal_dist(exit_pos, next_pos)
    
    if curr_dist > next_dist:
        return True
    else:
        return False
    


def chk_not_exit_people():
    for x,y in people:
        if (x,y) != (-1,-1):
            return True
    return False


def move(x,y):
    dxs = [0,0,-1,1]
    dys = [-1,1,0,0]
    
    res_x, res_y = -1,-1
    for dx,dy in zip(dxs,dys):
        nx, ny = x+dx, y+dy
        # 갈 수 있는 좌표인가? 출구쪽에 가까워지는 방향인가 확인
        if can_go(nx,ny) and more_min_dist((x,y), (nx, ny)):
            if (res_x, res_y) == (-1,-1):
                res_x, res_y = nx,ny
            else:
                # 현재 탐색이 상하로 움직이는 좌표면 변경
                if dx != 0:
                    res_x, res_y = nx,ny
    return (res_x, res_y)
            
        

def all_move():
    global people, people_move
    
    for i, (x,y) in enumerate(people):
        if (x,y) != (-1,-1):
            # 탈출 전 참가자 이동
            nx,ny = move(x,y)
            # 움직일 수 있는 좌표 없으면 안움직임
            if (nx,ny) != (-1,-1):
                # 탈출여부 확인
                if (nx,ny) == exit_pos:
                    people[i] = (-1,-1)
                else:
                    people[i] = (nx,ny)
                # 이동 거리 기록
                people_move[i] += 1
                
    print('after all move')
    print('people? ', people)
    print('people_move? ', people_move)
    
    
        
def find_square():
    # 모든 정사각형을 확인
    global exit_pos, square_info
    
    ex, ey = exit_pos
    print('ex,ey? ', ex,ey)
    
    # 정사각형 사이즈
    for size in range(2,n+1):
        print('size? ', size)
        for x1 in range(1,n-size+2):
            for y1 in range(1,n-size+2):
                # 시작점 (x1,y1)
                # 끝점 (x2,y2)
                x2, y2 = x1+size-1, y1+size-1
                
                #print('x1, y1, x2, y2? ', x1, y1, x2, y2 )
                
                # exit_pos가 정사각형 안에 있는지 확인
                if not (x1 <= ex and ex <= x2 and y1 <= ey and ey <= y2):
                    continue
                
                #print('x1, y1, x2, y2? ', x1, y1, x2, y2 )
                
                exist_people = False
                for px,py in people:
                    if (px,py) != (-1,-1):
                        if (x1 <= px and px <= x2 and y1 <= py and py <= y2):
                            # 출구 위치에 있는 사람 제외..!!
                            if (px,py) != (ex,ey):
                                exist_people = True
                                break
                            
                if exist_people:
                    square_info = [size, (x1,y1)]
                    print('square_info?', square_info)
                    return
                    
                
                        
def move_game_map():
    global game_map
    
    # 벽 감소
    s_size = square_info[0]
    sx,sy = square_info[1]
    
    for i in range(sx, sx+s_size):
        for j in range(sy, sy+s_size):
            if game_map[i][j] != 0:
                game_map[i][j] -= 1
    
    
    new_game_map = [[0 for _ in range(n+1)] for _ in range(n+1) ]
    
    # 정사각형을 시계방향으로 90도 회전
    for x in range(sx, sx+s_size):
        for y in range(sy, sy+s_size):
            # sx,sy 위치를 0,0으로 옮기기
            ox, oy = x-sx, y-sy
            
            # 90도 회전 현재 좌표가 옮겨지는 좌표로
            rx, ry = oy, s_size-ox-1
            
            # 시작위치만큼 다시 더하기
            new_game_map[rx+sx][ry+sy] = game_map[x][y]
            
    print('after move_game_map')
    print('game_map? ', game_map)
    print('new_game_map? ', new_game_map)
    
    # 변경된 값만 game_map에 옮겨줌
    for x in range(sx, sx+s_size):
        for y in range(sy, sy+s_size):
            game_map[x][y] = new_game_map[x][y]
            
        
        
def move_people_exit_pos():
    global people, exit_pos
    
    s_size = square_info[0]
    sx,sy = square_info[1]
    
    for i, (px,py) in enumerate(people):
        if (px,py) != (-1,-1):
            if (sx <= px and px <= sx+s_size-1 and sy <= py and py <= sy+s_size-1):
                ox, oy = px-sx, py-sy
                rx, ry = oy, s_size-ox-1
                people[i] = (rx+sx, ry+sy)
    
    
    ex, ey = exit_pos
    ox, oy = ex-sx, ey-sy
    rx, ry = oy, s_size-ox-1
    exit_pos = (rx+sx, ry+sy)
    
    print('after move_people_exit_pos')
    print('people? ', people)
    print('game_map? ', game_map)
    
    




people_move = [0 for _ in range(m)]
exit_people_move_cnt = 0
# exit_people_move_cnt = sum(people_move)

# size와 시작좌표
square_info = [0,(-1,-1)]
for ki in range(k):
    
    print('\nki? ', ki)
    print('people? ', people)
    print('people_move? ', people_move)
    print('exit_pos? ', exit_pos)
    print('game_map? ', game_map)
    
    # 모든 참가자 이동
    all_move()
    
    # 참가자가 모두 탈출하면 False reutrn
    if not chk_not_exit_people():
        break
    
    find_square()
    print('square_info? ', square_info)
    
    move_game_map()
    
    move_people_exit_pos()



exit_people_move_cnt = sum(people_move)
print(exit_people_move_cnt)
print(exit_pos[0], exit_pos[1])

