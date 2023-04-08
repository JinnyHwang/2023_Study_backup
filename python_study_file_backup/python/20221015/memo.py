
n = 5

# 술래 위치
sul_pos = [n//2, n//2]

sul_d_out = [(-1,0),(0,1),(1,0),(0,-1)] # 상 우 하 좌
sul_d_in = [(1,0),(0,1),(-1,0),(0,-1)] # 하 우 상 좌

# sul_d[0] - 밖으로? 아님 중앙으로? 0: d_out / 1: d_in
# sul_d[1] - 어떤 방향인지? d_out, d_in의 index
# sul_d_out[sul_d[1]] / sul_d_in[sul_d[1]]
sul_d = [0,0]

# out으로 진행할 때
# sul_d_out[0], sul_d_out[2] :상 하 이동시 sul_move_len_max+1
# sul_d_out[1], sul_d_out[3] :우 좌 이동시 sul_move_len_max 유지

# in으로 진행할 때
# sul_d_in[1], sul_d_in[3] :우 좌 이동시 sul_move_len_max-1
# sul_d_in[0], sul_d_in[0] :하 상 이동시 sul_move_len_max 유지
sul_move_len = 1 # 1~n
move_cnt = 0

def show(l):
    for ll in l:
        print(ll)
    print('\n')

def func_sul_move(sul_pos, sul_d):
    
    global sul_move_len
    global move_cnt
    
    # 다음 위치 정하기
    
    # 현재위치의 달팽이 out? in?
    # 방향이 상하좌우?
    if sul_d[0] == 0:
        sul_nd = sul_d_out[sul_d[1]]
    elif sul_d[0] == 1:
        sul_nd = sul_d_in[sul_d[1]]
    
    # y, x direction : sul_nd[0] sul_nd[1]
    ny = sul_pos[0] + sul_nd[0]
    nx = sul_pos[1] + sul_nd[1]
    print('nx:{}, ny:{}, x:{}, y:{}'.format(nx, ny, sul_pos[0], sul_pos[0]))
    print('[1] sul_pos:{}, sul_d:{}, move_cnt:{}, sul_move_len:{}'.format(sul_pos, sul_d, move_cnt, sul_move_len))


    # (0,0) (n//2,n//2) 확인
    # 맨 끝, 정중앙 도달 시
    if [ny,nx] == [0,0]:
        sul_d[0] = 1
        sul_d[1] = 0
        move_cnt = 1
        sul_pos[0] = ny
        sul_pos[1] = nx
        #sul_pos = [ny, nx]
        print('[2] sul_pos:{}, sul_d:{}, move_cnt:{}, sul_move_len:{}'.format(sul_pos, sul_d, move_cnt, sul_move_len))
        return
    elif [ny,nx] == [n//2,n//2]:
        sul_d[0] = 0
        sul_d[1] = 0
        move_cnt = 0
        sul_pos[0] = ny
        sul_pos[1] = nx
        #sul_pos = [ny, nx]
        print('[3] sul_pos:{}, sul_d:{}, move_cnt:{}, sul_move_len:{}'.format(sul_pos, sul_d, move_cnt, sul_move_len))
        return
    
    # 범위를 넘지 않을 것!
    sul_pos[0] = ny
    sul_pos[1] = nx
    move_cnt += 1
    #sul_pos = [ny, nx]
    print('[4] sul_pos:{}, sul_d:{}, move_cnt:{}, sul_move_len:{}'.format(sul_pos, sul_d, move_cnt, sul_move_len))

    
    # 맨 끝, 정중앙 도달하지 않았을 때만 체크
    # 움직임이 끝난 후
    # 범위 체크
    if move_cnt == sul_move_len:
        # 방향 전환
        sul_d[1] = (sul_d[1]+1)%4
        
        # sul_move_len 재정의
        if sul_d[0] == 0: # out방향
            if sul_d[1] == 0 or sul_d[1] == 2: # 상 하
                sul_move_len += 1
        elif sul_d[0] == 1: # in방향
            if sul_d[1] == 1 or sul_d[1] == 3: # 우 좌
                sul_move_len -= 1
        
        move_cnt = 0
    
    print('[5] sul_pos:{}, sul_d:{}, move_cnt:{}, sul_move_len:{}'.format(sul_pos, sul_d, move_cnt, sul_move_len))


list1 = [[0 for _ in range(n)] for _ in range(n)]

for i in range(2*(n*n)):
    
    list1[sul_pos[0]][sul_pos[1]] = i
    
    print('turn ', i)
    show(list1)
    
    func_sul_move(sul_pos, sul_d)















