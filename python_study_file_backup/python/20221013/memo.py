

def show(l):
    for ll in l:
        print(ll)
    print('\n')
    
    
n = 5

#ball의 start point를 정하는 방향
#하 우 상 좌
d_1 = [(1,0),(0,1),(-1,0),(0,-1)]

#ball의 진행 방향
d_2 = [(0,1),(-1,0),(0,-1),(1,0)]

ball_start_pos = [(0,0),(n-1,0),(n-1,n-1),(0,n-1)]

ball_turn = 0
ball_turn_cnt = 0

for tt in range(50):

    game_map = [[0 for _ in range(n)] for _ in range(n)]

    if ball_turn_cnt > n-1:
        ball_turn_cnt = 0
        ball_turn = (ball_turn+1)%4    
        print('ball_turn, ball_turn_cnt?', ball_turn, ball_turn_cnt)

    start_by = ball_start_pos[ball_turn][0] + d_1[ball_turn][0]*ball_turn_cnt
    start_bx = ball_start_pos[ball_turn][1] + d_1[ball_turn][1]*ball_turn_cnt

    #print('Turn ',tt, ': ball_turn? ', ball_turn, ' ball_turn_cnt? ', ball_turn_cnt, ' start_bx? ', start_bx, '  start_bx? ', start_bx)

    # 공 던지기 시작
    for i in range(n):
        ny = start_by + d_2[ball_turn][0]*i
        nx = start_bx + d_2[ball_turn][1]*i
        
        game_map[ny][nx] = i

    ball_turn_cnt += 1
    print(tt, ' game_map')
    show(game_map)

