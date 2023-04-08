
'''
n*n 격자  꼬리잡기놀이

3명 이상 한 팀

각 팀은 머리사람, 꼬리사람이 존재 (진행 방향을위함)
각 사람이 몇번째인지 찾는 func 필요

각 팀은 이동 선을 따라서 이동. 선은 이어져 있음

1. 각 팀은 머리사람을 따라 1칸씩 이동

2. 라운드마다 공을 던짐
0,0 우 / n-1,0 상 / n-1,n-1 좌 / 0,n-1 하

ball의 start point를 정하는 방향
하 우 상 좌
d_1 = [(1,0),(0,1),(-1,0),(0,-1)]


ball의 진행 방향
d_2 = [(0,1),(-1,0),(0,-1),(1,0)]


ball_start_pos = [(0,0),(n-1,0),(n-1,n-1),(0,n-1)]

ball_turn = 0

# 공의 시작 점 찾기
start_by = ball_start_pos[ball_turn][0] + d_1[ball_turn][0]*(n-1)
start_bx = ball_start_pos[ball_turn][1] + d_1[ball_turn][1]*(n-1)
if not ( 0 <= y < n and 0 <= x < n ):
    ball_turn += 1
    start_by = ball_start_pos[ball_turn][0] + d_1[ball_turn][0]*(n-1)
    start_bx = ball_start_pos[ball_turn][1] + d_1[ball_turn][1]*(n-1)

# 공 던지기 시작
for i in range(n):
    ny = start_by + d_2[ball_turn][0]*i
    nx = start_bx + d_2[ball_turn][1]*i
    
    if arr[ny][nx] > 0:
        gain grade
        k번째 사람이면 K제곱 만큼 점수 얻음
        
        머리사람, 꼬리사람 방향 change
        
        # 최초에 만나게 되는 사람만이 공을 얻게 되어 점수를 얻게 됩니다.
        break
else:
    # 아무도 안맞음
    

점수의 총합은?

'''

def show(l):
    for ll in l:
        print(ll)
    print('\n')


# 격자의 크기, 팀의 개수, 라운드 수
n, m, k = map(int, input().split())

game_map = [ list(map(int, input().split())) for _ in range(n) ]

# 값이 있는 곳 줄따라 이동

#ball의 start point를 정하는 방향
#하 우 상 좌
d_1 = [(1,0),(0,1),(-1,0),(0,-1)]

#ball의 진행 방향
d_2 = [(0,1),(-1,0),(0,-1),(1,0)]

ball_start_pos = [(0,0),(n-1,0),(n-1,n-1),(0,n-1)]

#from collections import deque


def func_group_move(y, x, visited, game_map):
    
    group = []
    
    tail_change_flag = 0
    while_end_flag = 0
    
    visited[y][x] = 1

    #print('!!game_map')
    #show(game_map)
    
    # 맨 처음 방향 잡기
    # head 기준으로 4방향 모두 확인
    for di in d_1:
        ny = y + di[0]
        nx = x + di[1]
        if 0 <= ny < n and 0 <= nx < n:
            # head를 앞으로 이동
            if game_map[ny][nx] == 4:
                #print('[1]')
                # next_pos
                game_map[ny][nx] = 1
                game_map[y][x] = 2
                group.append([ny,nx])
                group.append([y,x])
                
                visited[ny][nx] = 1
                visited[y][x] = 1
            # 이동 동선이 사람으로 꽉 차있으면?
            # head를 앞으로 이동
            # 꼬리도 변경
            elif game_map[ny][nx] == 3:
                for di in d_1:
                    # 이동시킴
                    nny = ny + di[0]
                    nnx = nx + di[1]
                    if 0 <= nny < n and 0 <= nnx < n:
                        # 꼬리의 다음 위치 찾기
                        if game_map[nny][nnx] == 2:
                            game_map[ny][nx] = 1
                            game_map[y][x] = 2
                            game_map[nny][nnx] = 3 # 얘는 그룹 탐색 맨 마지막에 append 될 것
                            group.append([ny,nx])
                            group.append([y,x])
                            tail_change_flag = 1
                            
                            visited[ny][nx] = 1
                            visited[y][x] = 1
                            break
            # 탐색 방향 ny, nx에 저장
            elif game_map[ny][nx] == 2:
                #print('[2]')
                sy = ny
                sx = nx
                #group.append([ny,nx])
                visited[ny][nx] = 1

    '''
    print('sy, sx? ', sy, sx)
    print('??game_map')
    show(game_map)
    print('visited')
    show(visited)
    print('group??? ', group)
    '''
    
    group.append([sy, sx])
        
    # group 탐색
    # head 다음 사람부터 확인
    while while_end_flag == 0:
        
        for di in d_1:
            ny = sy + di[0]
            nx = sx + di[1]
            
            # 시작점 빼고 확인
            #if (ny == y and nx == x):
            #    continue
            
            # 범위내에 있고 값이 있는 것만 확인
            if 0 <= ny < n and 0 <= nx < n and game_map[ny][nx] > 0 and visited[ny][nx] == 0:
                #print('?? ny, nx ', ny, nx, ' game_map[ny][nx]??', game_map[ny][nx])
                if game_map[ny][nx] == 2:     
                    group.append([ny, nx])
                    sy = ny
                    sx = nx
                    visited[ny][nx] = 1
                # 꼬리 만남!
                elif game_map[ny][nx] == 3:
                    visited[ny][nx] = 1
                    sy = ny
                    sx = nx
                    while_end_flag = 1
                    break
    '''
    print('sy, sx??', sy, sx)
    print('tail_change_flag??', tail_change_flag)
    print('group[-1]??', group[-1])
    '''
    # 앞에 탐색에서 꼬리변경이 이루어졌으면 값 변경 진행하지 않음
    if tail_change_flag == 0:
        # 앞으로 옮기기
        #꼬리 옮기기
        game_map[sy][sx] = 4
        #group[-1][0]
        game_map[group[-1][0]][group[-1][1]] = 3
    else:
        group.append([sy, sx])
        
    '''
    print('!!game_map')
    show(game_map)
    print('visited')
    show(visited)
    print('group? ', group)
    '''
    return group


total_grade = 0

turn = 1
ball_turn = 0
ball_turn_cnt = 0

while turn <= k:
        
    # groups[n][0] : 머리
    # groups[n][-1] : 꼬리
    groups = []
    small_group = []

    print('strat!! turn ', turn)
    visited = [ [ 0 for _ in range(n) ] for _ in range(n) ]
    #print('visited')
    #show(visited)
    
    print('before game_map')
    show(game_map)

    # group 확인 및 인원 이동
    for y in range(n):
        for x in range(n):
            if visited[y][x] == 0 and game_map[y][x] == 1:
                # 격자 탐색
                small_group = func_group_move(y, x, visited, game_map)
                groups.append(small_group)
                '''
                print('small_group? ',small_group)
                print('groups?', groups)
                print('visited')
                show(visited)
                print('game_map')
                show(game_map)
                '''
              
    print('after move game_map')
    show(game_map)
    print('groups')
    show(groups)
    
    
    #func_shot_ball()
    # 공의 시작 점 찾기
    if ball_turn_cnt > n-1:
        if ball_turn >= 4:
            ball_turn = 0
        else:
            ball_turn += 1
        #ball_turn += 1
        ball_turn_cnt = 0
    
    start_by = ball_start_pos[ball_turn][0] + d_1[ball_turn][0]*ball_turn_cnt
    start_bx = ball_start_pos[ball_turn][1] + d_1[ball_turn][1]*ball_turn_cnt
    
    print('ball_turn? ', ball_turn, ' ball_turn_cnt? ', ball_turn_cnt, ' start_bx? ', start_bx, '  start_bx? ', start_bx)
    
    # 공 던지기 시작
    for i in range(n):
        ny = start_by + d_2[ball_turn][0]*i
        nx = start_bx + d_2[ball_turn][1]*i
        
        if 1 <= game_map[ny][nx] <= 3:
            
            for g in groups:
                for gi, g2 in enumerate(g, start=1):
                    if g2 == [ny,nx]:
                        print('점수 획득 g? ', g, '  g2? ', g2, '  grade?? ', (gi*gi))
                        total_grade += (gi*gi)
                        game_map[g[0][0]][g[0][1]] = 3
                        game_map[g[-1][0]][g[-1][1]] = 1
            
            # 최초에 만나게 되는 사람만이 공을 얻게 되어 점수를 얻게 됩니다.
            break
    #else:
        # 아무도 안맞음
    
    ball_turn_cnt += 1
    
    print('after shot ball game_map')
    show(game_map)
    
    print('total_grade?', total_grade)
    
    turn += 1
