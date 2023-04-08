# 기본 제공코드는 임의 수정해도 관계 없습니다. 단, 입출력 포맷 주의
# 아래 표준 입출력 예제 필요시 참고하세요.

# 표준 입력 예제
'''
a = int(input())                        정수형 변수 1개 입력 받는 예제
b, c = map(int, input().split())        정수형 변수 2개 입력 받는 예제 
d = float(input())                      실수형 변수 1개 입력 받는 예제
e, f, g = map(float, input().split())   실수형 변수 3개 입력 받는 예제
h = input()                             문자열 변수 1개 입력 받는 예제
'''

# 표준 출력 예제
'''
a, b = 6, 3
c, d, e = 1.0, 2.5, 3.4
f = "ABC"
print(a)                                정수형 변수 1개 출력하는 예제
print(b, end = " ")                     줄바꿈 하지 않고 정수형 변수와 공백을 출력하는 예제
print(c, d, e)                          실수형 변수 3개 출력하는 예제
print(f)                                문자열 1개 출력하는 예제
'''




'''
      아래의 구문은 input.txt 를 read only 형식으로 연 후,
      앞으로 표준 입력(키보드) 대신 input.txt 파일로부터 읽어오겠다는 의미의 코드입니다.
      여러분이 작성한 코드를 테스트 할 때, 편의를 위해서 input.txt에 입력을 저장한 후,
      아래 구문을 이용하면 이후 입력을 수행할 때 표준 입력 대신 파일로부터 입력을 받아올 수 있습니다.

      따라서 테스트를 수행할 때에는 아래 주석을 지우고 이 구문을 사용하셔도 좋습니다.
      아래 구문을 사용하기 위해서는 import sys가 필요합니다.

      단, 채점을 위해 코드를 제출하실 때에는 반드시 아래 구문을 지우거나 주석 처리 하셔야 합니다.
'''
#import sys
#sys.stdin = open("input.txt", "r")

# 도망자 방향
#방향: 좌우(오른쪽시작) , 상하(아래쪽시작)
do_d = [[(0,1),(0,-1)],[(1,0),(-1,0)]]

# 술래 위치
sul_d_out = [(-1,0),(0,1),(1,0),(0,-1)] # 상 우 하 좌
sul_d_in = [(1,0),(0,1),(-1,0),(0,-1)] # 하 우 상 좌

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
        

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    
    n, m, h, k = map(int, input().split())

    do_list = []
    tree_list = []
    sul_pos = [n//2, n//2]
    sul_d = [0,0]
    sul_move_len = 1 # 1~n
    
    for _ in range(m):
        y, x, d = map(int, input().split())
        if d == 1:
            do_list.append([y-1,x-1,0,0])
        elif d == 2:
            do_list.append([y-1,x-1,1,0])
            
    for _ in range(h):
        y, x = map(int, input().split())
        tree_list.append((y-1,x-1))
        
    turn = 1
    move_cnt = 0
    total_score = 0
    while turn <= k:
        
        # 도망자 움직임
        for i, do in enumerate(do_list):
            # 술래와의 거리 확인 3이하일 때만 움직일 수 있음
            if abs(do[0]-sul_pos[0])+abs(do[1]-sul_pos[1]) <= 3:
                next_do = func_do_move(do[0],do[1],do[2],do[3])
                do_list[i] = next_do
                
        # 술래 움직임
        func_sul_move(sul_pos, sul_d)
        
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
            
            if 0 <= ny < n and 0 <= nx < n:
                # 도망자 있는지 확인
                for i, do in enumerate(do_list):
                    if do[:2] == [ny,nx]:
                        if not (ny,nx) in tree_list:
                            do_list_copy.remove(do)
        
        if not do_list_copy is do_list:
            total_score += turn*(len(do_list)-len(do_list_copy))
            
        do_list = do_list_copy
        
        if not do_list:
            break
            
        turn += 1
            
                            
    print('#{} {}'.format(test_case,total_score))
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
