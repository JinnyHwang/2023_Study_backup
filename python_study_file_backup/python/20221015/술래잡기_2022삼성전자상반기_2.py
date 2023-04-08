
'''
https://www.codetree.ai/frequent-problems/hide-and-seek/description

n*n 격자

술래 정중앙 n//2, n//2

도망자 m명. 지정된 위치, 방향 주어짐(중앙제외)
방향: 상하(아래쪽시작) , 좌우(오른쪽시작)
d1 = [(1,0),(-1,0)]
d2 = [(0,1),(0,-1)]


나무 h개 존재. 도망자 위치와 겹칠 수 있다.

- 1턴
1. 도망자 움직임
2. 술래 움직임


1. 도망자 움직임
현재 술래와의 거리가 3 이하인 도망자만 움직입니다.
도망자의 위치가 (x1, y1), 술래의 위치가 (x2, y2)라 했을 때 두 사람간의 거리는 |x1 - x2| + |y1 - y2|로 정의

모든 도망자가 동시에 움직임
-. 술래와의 거리가 3이하인 도망자
(1) 현재 방향으로 1칸 이동 시 격자를 벗어나지 않음
술래가 있으면 움직이지 않는다.
술래가 없으면 이동한다. 나무랑 겹쳐도 됨

(2) 재 방향으로 1칸 이동 시 격자를 벗어남
방향 전환. 술래가 없으면 1칸 이동


2. 술래 움직임
달팽이 모양으로 움직임 d1[i++]
끝에 도달하면 거꾸로 이동 d2[i++]
d1 = [(-1,0),(0,1),(1,0),(0,-1)] # 상 우 하 좌
d2 = [(1,0),(0,1),(-1,0),(0,-1)] # 하 우 상 좌

술래는 이동 후 다음으로 갈 방향으로 바로 전환
0,0 / 정중앙 도달 시에도 갈 방향으로 바로 전환


3. 술래잡기
현재 방향을 기준으로 본인 포함 3칸 확인
나무와 겹쳐있는 도망자를 제외하고 도망자를 잡음
도망자는 제거

점수: turn * 잡은 도망자의 수


k번 술래잡기 진행. 도망자가 없으면 게임 끝
술래가 얻게된 점수 출력.
'''

def show(l):
    for ll in l:
        print(ll)
    print('\n')


# n : 격자크기. 홀수
# m : 도망자 수
# h : 나무 개수
# k : turn
n, m, h, k = map(int, input().split())

do_list = []
tree_list = []

for _ in range(m):
    y, x, d = map(int, input().split())
    # do_d[do_list[n][2]][do_list[n][3]]
    # do_list[n][2] : do_d[0]좌우 do_d[1]상하 선택
    # do_list[n][3] : do_d[n][0]좌/우  do_d[n][1]상/하 선택
    if d == 1:
        do_list.append([y-1,x-1,0,0])
    elif d == 2:
        do_list.append([y-1,x-1,1,0])
        
        
for _ in range(h):
    y, x = map(int, input().split())
    tree_list.append((y-1,x-1))



# 도망자 방향
#방향: 좌우(오른쪽시작) , 상하(아래쪽시작)
do_d = [[(0,1),(0,-1)],[(1,0),(-1,0)]]

def func_do_move(y,x,di1,di2):
    
    ny = y + do_d[di1][di2][0]
    nx = x + do_d[di1][di2][1]
    
    if 0 <= ny < n and 0 <= nx < n:
        if sul_pos != [ny,nx]:
            return [ny,nx,di1,di2]
        else:
            return [y,x,di1,di2]
    else:
        ndi2 = (di2+1)%2
        ny = y + do_d[di1][ndi2][0]
        nx = x + do_d[di1][ndi2][1]
        if sul_pos != [ny,nx]:
            return [ny,nx,di1,ndi2]
        else:
            return [y,x,di1,ndi2]
            
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
    

    # (0,0) (n//2,n//2) 확인
    # 맨 끝, 정중앙 도달 시
    if [ny,nx] == [0,0]:
        sul_d[0] = 1
        sul_d[1] = 0
        move_cnt = 1
        sul_pos[0] = ny
        sul_pos[1] = nx
        return
    elif [ny,nx] == [n//2,n//2]:
        sul_d[0] = 0
        sul_d[1] = 0
        move_cnt = 0
        sul_pos[0] = ny
        sul_pos[1] = nx
        return
    
    # 범위를 넘지 않을 것!
    sul_pos[0] = ny
    sul_pos[1] = nx
    move_cnt += 1
    
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

'''
sul_d_out = [(-1,0),(0,1),(1,0),(0,-1)] # 상 우 하 좌
sul_d_in = [(1,0),(0,1),(-1,0),(0,-1)] # 하 우 상 좌

# sul_d[0] - 밖으로? 아님 중앙으로? 0: d_out / 1: d_in
# sul_d[1] - 어떤 방향인지? d_out, d_in의 index
# sul_d_out[sul_d[1]] / sul_d_in[sul_d[1]]
sul_d = [0,0]
'''
'''
print('do_list?')
show(do_list)

print('sul_pos?', sul_pos)

print('tree_list?')
show(tree_list)
'''
turn = 1
move_cnt = 0
total_score = 0
while turn <= k:
    '''
    print('turn? ', turn)
    
    print('before move do_list?')
    show(do_list)
    '''
    #do_list_before = [[0 for _ in range(n)] for _ in range(n)]
    #do_list_after = [[0 for _ in range(n)] for _ in range(n)]
    
    # 도망자 움직임
    for i, do in enumerate(do_list):
        # 술래와의 거리 확인 3이하일 때만 움직일 수 있음
        if abs(do[0]-sul_pos[0])+abs(do[1]-sul_pos[1]) <= 3:
            #do_list_before[do[0]][do[1]] = i+1
            next_do = func_do_move(do[0],do[1],do[2],do[3])
            do_list[i] = next_do
            #do_list_after[next_do[0]][next_do[1]] = i+1
    '''        
    print('do before?')
    show(do_list_before)
    
    print('do after?')
    show(do_list_after)
    
    
    print('after move do_list?')
    show(do_list)
    '''
    
    #print('before sul_pos?', sul_pos)
    # 술래 움직임
    func_sul_move(sul_pos, sul_d)
    #print('after sul_pos?', sul_pos)
    
    
    #print('before catch do_list?')
    #show(do_list)
    
    #do_list_after2 = [[0 for _ in range(n)] for _ in range(n)]
    
    # 도망자 잡기
    if sul_d[0] == 0:
        sul_find_d = sul_d_out[sul_d[1]]
    elif sul_d[0] == 1:
        sul_find_d = sul_d_in[sul_d[1]]
    
    do_list_copy = [[0 for _ in range(4)] for _ in range(len(do_list))]
    for i in range(len(do_list)):
        for j in range(4):
            do_list_copy[i][j] = do_list[i][j]
        
    for i in range(3):
        ny = sul_pos[0] + sul_find_d[0]*i
        nx = sul_pos[1] + sul_find_d[1]*i
        
        #print(i,' search block ny, nx? ', ny, nx)
        
        if 0 <= ny < n and 0 <= nx < n:
            # 도망자 있는지 확인
            for i, do in enumerate(do_list):
                if do[:2] == [ny,nx]:
                    if not (ny,nx) in tree_list:
                        do_list_copy.remove(do)
                        #do_catch.append(i)
                        #del do_list[i]
                    #else:
                        #print('trre! can''t catch!')
    
    '''
    for i, do in enumerate(do_list):
        do_list_after2[do[0]][do[1]] = i+1
    print('do after?')
    show(do_list_after)
    
    
    print('after catch do_list?')
    show(do_list)
    '''
    
    if not do_list_copy is do_list:
        #do_catch.sort(reverse=True)
        total_score += turn*(len(do_list)-len(do_list_copy))
        #print('total_score, turn*do_catch_cnt? ', total_score, turn*len(do_catch))
        
    do_list = do_list_copy
    
    if not do_list:
        break
        
    turn += 1
        
                        
print(total_score)                
    
