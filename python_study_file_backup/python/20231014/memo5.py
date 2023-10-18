import heapq

# 우선순위가 높은 토끼

# 총 점프횟수가 적은 토끼
# 현재 서있는 행+열번호 작은 토끼
# 행번호 작은 토끼
# 열번호 작은 토끼
# rabbit_q = []
# heapq.heappush(rabbit_q, (jump_cnt, x+y, x, y, 고유번호))
# 우선순위 높은 토끼 결정

# 토끼가 이동할 위치
# dxs = [-1,1,0,0]
# dys = [0,0,-1,1]
# move_q = []
# heapq.heappush(move_q, (-(x+y), -x, -y))

# 점수 얻기
# 현재 토끼를 제외한 나머지 토끼들의 획득 점수 
# 현재 토끼가 이동한 좌표 행+열 값
# rabbit_info[고유번호][R_SCORE] += (x+y)

# 게임이 끝나면
# rabbit_q2 = []
# heapq.heappush(rabbit_q2, (-(x+y), -x, -y, -고유번호))
# 우선순위가 높은 토끼를 골라서 점수 S를 더해줌
# 단, 해당 토끼가 한 번이라도 뽑혔던 적이 있어야 함
# rabbit_info[고유번호][R_PICK] False면 다음토끼


# i번 토끼의 고유번호, 이동해야하는 거리

# 이동거리 변경

# 최고의 토끼 선정


n, m, p = 0, 0, 0

# (jump_cnt, x+y, x, y, 고유번호)
# 토끼의 우선순위를 보는 queue
rabbit_q = []
# 토끼 정보를 저장하는 dic: key:고유번호 , value(rabbit_num, d, score, pick)
R_NUM = 0
R_D = 1
R_SCORE = 2
R_PICK = 3
rabbit_info = {}

def in_range(x,y):
    return 1 <= x and x <= n and 1 <= y and y <= m


def input_rabbit_info(command):
    global rabbit_q, rabbit_info, n, m, p 
    
    cmd_l = list(command.split())
    n, m, p = int(cmd_l[1]), int(cmd_l[2]), int(cmd_l[3])
    
    rabbit_num = 1
    for i in range(4,len(cmd_l)-1,2):
        pid, d = int(cmd_l[i]), int(cmd_l[i+1])
        # heapq.heappush(rabbit_q, (jump_cnt, x+y, x, y, 고유번호))
        x,y = 1,1
        heapq.heappush(rabbit_q, (0, x+y, x, y, pid))
        rabbit_info[pid] = rabbit_info.get(pid,[rabbit_num, d, 0, False])
        rabbit_num += 1
    
    #print(rabbit_q, rabbit_info, n, m, p)
        
        
def move_rabbit(x,y,num):
    dxs = [-1,0,0,1]
    dys = [0,-1,1,0]
    
    rd = rabbit_info[num][R_D]
    move_q = [] # (-(x+y), -x, -y)
    
    for di in range(4):
        nd = di
        nx, ny = x, y
        for _ in range(rd):
            nx2 = nx+dxs[nd]
            ny2 = ny+dys[nd]
            if not in_range(nx2,ny2): # 범위 벗어나면 반대 방향으로 전환
                nd = 3-nd
                nx2 = nx+dxs[nd]
                ny2 = ny+dys[nd]
            nx, ny = nx2, ny2
            #print('di,nx,ny,nd? ', di,nx,ny,nd)
        # 현재 방향으로 이동했을 때 위치 값
        heapq.heappush(move_q, (-(nx+ny),-nx,-ny))
    
    #print(move_q)
    _, next_x, next_y = heapq.heappop(move_q)
    next_x, next_y = -next_x, -next_y
    return (next_x, next_y)
                
            
        
def rabbit_game_simulate(k,s):
    global rabbit_q, rabbit_info
    
    for _ in range(k):
        
        # 우선순위가 가장 높은 토끼 뽑기
        # (jump_cnt, x+y, x, y, 고유번호)
        jump_cnt, _, curr_x, curr_y, curr_r_num = heapq.heappop(rabbit_q)
        #print('1: ',jump_cnt, curr_x, curr_y, curr_r_num)
        
        # 토끼가 다음으로 갈 좌표 정보 획득
        next_x, next_y = move_rabbit(curr_x, curr_y, curr_r_num)
        #print('2: ', next_x, next_y)
        # 변경된 토끼 정보 넣어주기
        heapq.heappush(rabbit_q, (jump_cnt+1, next_x + next_y, next_x, next_y, curr_r_num))
        rabbit_info[curr_r_num][R_PICK] = True
        #print('rabbit_q? ', rabbit_q)
        #print('rabbit_info? ', rabbit_info)
        
        # 다른 토끼 점수 획득
        other_score = next_x + next_y
        for k, v in rabbit_info.items():
            if k != curr_r_num:
                rabbit_info[k][R_SCORE] += other_score
        #heapq.heappush(rabbit_q, (jump_cnt, x+y, x, y, pid))
        #rabbit_info[pid] = rabbit_info.get(pid,(rabbit_num, d, score))
        #print('rabbit_info? ', rabbit_info)
    
    # 게임 끝!
    # (현재 서있는 행 번호 + 열 번호가 큰 토끼, 행 번호가 큰 토끼, 열 번호가 큰 토끼, 고유번호가 큰 토끼) 순
    final_rabbit_q = []
    for _ in range(p):
        jump_cnt, xy, x, y, num = heapq.heappop(rabbit_q)
        heapq.heappush(final_rabbit_q, (-(xy), -x, -y, -num, jump_cnt))
    #print('final_rabbit_q?', final_rabbit_q)
    #print('final_rabbit_q?', final_rabbit_q[0])
    #print('rabbit_q?', rabbit_q)
    
    # 조건에 맞는 토끼 점수 올려줌
    # rabbit_q 초기화
    for pi in range(p):
        xy, x, y, num, jump_cnt = heapq.heappop(final_rabbit_q)
        #print('pi?: ', pi, xy, x, y, num, jump_cnt)
        xy, x, y, num = -xy, -x, -y, -num
        if rabbit_info[num][R_PICK] == True:
            #print('rabbit_info? ', rabbit_info)
            rabbit_info[num][R_SCORE] += s
            heapq.heappush(rabbit_q, (jump_cnt, xy, x, y, num))
            rabbit_info[num][R_PICK] = False
            break
        else:
            heapq.heappush(rabbit_q, (jump_cnt, xy, x, y, num))
            rabbit_info[num][R_PICK] = False
    
    while final_rabbit_q:
        xy, x, y, num, jump_cnt = final_rabbit_q.pop()
        xy, x, y, num = -xy, -x, -y, -num
        heapq.heappush(rabbit_q, (jump_cnt, xy, x, y, num))
        rabbit_info[num][R_PICK] = False
        
    #print('final_rabbit_q?', final_rabbit_q)
    #print('rabbit_q?', rabbit_q)
    #print('rabbit_info?', rabbit_info)
        
        
def print_max_score():
    max_score = -1
    for vl in rabbit_info.values():
        max_score = max(max_score, vl[R_SCORE])
    print(max_score)
        

q = int(input())
for _ in range(q):
    
    command = input()
    
    # 토끼 정보 입력
    if command.startswith("100"):
        input_rabbit_info(command)
        
    # 경주 시작
    elif command.startswith("200"):
        cmd, k, s = command.split()
        k, s = int(k), int(s)
        rabbit_game_simulate(k,s)
        
    # 이동 거리 변경
    elif command.startswith("300"):
        cmd, pid, l = command.split()
        pid, l = int(pid), int(l)
        rabbit_info[pid][R_D] *= l
        
    elif command == "400":
        print_max_score()
        #break
        
    else:
        print('worng command')
        break



