
# 아ㅏㅏㅏ 배열 좌우가 너무 헷갈려!!!!
# map[a][b]
# 좌우로 움직이려면?

from copy import deepcopy
from collections import deque

def bomb(brick, bomb_w):
    # 원본을 해치지 않기 위해 복사
    new_brick = deepcopy(brick)
    
    # 추가로 부숴야하는 블록 확인하기 위함
    q = deque()
    
    for bomb_h in range(H):
        if new_brick[bomb_h][bomb_w]:
            if new_brick[bomb_h][bomb_w] > 1:
                q.append( (bomb_h, bomb_w, new_brick[bomb_h][bomb_w]) )
            new_brick[bomb_h][bomb_w] = 0
            break
        
    # while문을 타지 않는 경우
    # 배열의 모든 세로줄 값이 0
    # 값이1인 블록 하나만 깨트
    while q:
        qh, qw, b = q.popleft()
        for dh, dw in [(1,0), (-1,0), (0,1), (0,-1)]:
            for bb in range(1, b):
                nh = qh + dh*bb
                nw = qw + dw*bb
                if 0 <= nh < H and 0<= nw < W:
                    if new_brick[nh][nw] > 1:
                        q.append( (nh, nw, new_brick[nh][nw]) )
                    new_brick[nh][nw] = 0
    
    return new_brick

def gravity(brick):
    
    new_brick = deepcopy(brick)
    
    for gh in range(H-2, -1, -1):
        for gw in range(W):
            if new_brick[gh][gw] and new_brick[gh+1][gw] == 0:
                nh = 0
                flag = 0
                for hh in range(gh+1, H):
                    nh = hh
                    if new_brick[hh][gw]:
                        flag = 1
                        break
                if flag:
                    new_brick[nh-1][gw] = new_brick[gh][gw]
                else:
                    new_brick[nh][gw] = new_brick[gh][gw]
                new_brick[gh][gw] = 0
    
    return new_brick

        
def gravity_1(brick):
    
    new_brick = deepcopy(brick)
    #print('1??\n',new_brick,'\n\n')
    #print('1start')
    #for w in range(W):
    #    for h in range(H):
    #        print(new_brick[w][h],end=' ')
    #    print('\n')
    #print('1end')
    
    for gw in range(W):
        check_h = [ 0 for _ in range(H) ]
        index_h = 0
        for gh in range(H-1, -1, -1):
            #print(gh, gw, new_brick[gh][gw])
            if new_brick[gh][gw] > 0:
                check_h[index_h] = new_brick[gh][gw]
                index_h += 1
        
        
        for i in range(H):
            new_brick[H-1-i][gw] = check_h[i]
        #print(check_h,'\n',new_brick[gw])
        #new_brick[gw] = check_h[::-1]
    #print('2??\n',new_brick,'\n\n')
    
    #print('2start')
    #for w in range(W):
    #    for h in range(H):
    #        print(new_brick[w][h],end=' ')
    #    print('\n')
    #print('2end')

    return new_brick



def solve(cnt, brick):
    # 전역변수 사용
    global answer
    
    if cnt == N:
        brick_cnt  = 0
        for h in range(H):
            for w in range(W):
                if brick[h][w]:
                    brick_cnt += 1
                    
        answer = min(answer, brick_cnt)
        return
    
    # 구슬이 움직일 수 있는 범위는 0 ~ W-1
    # brick[h][w]
    for w in range(W):
        # W는 고정하고 H를 탐색
        new_brick = bomb(brick, w)
        
        # 벽돌꺠기가 끝났으면 밑으로 땡기기
        new_brick = gravity(new_brick)
        
        # i 단계에서 0 ~ W-1 또 돌림..
        # 진짜 모든 경우의 수를 확인하는구나....
        solve(cnt+1, new_brick)



T = int(input())

for t in range(T):
    N, W, H = map(int, input().split())
    # 행열 너무 헷갈리네! brick[w][h] 아님!!!!!
    # !!!brick[h][w]!!!
    # h개 세로줄
    # w개 가로줄
    brick = [ list(map(int, input().split())) for _ in range(H) ]
    
    # 무슨의미일까?
    # min 값을 return하기 위해서 가장 큰 값 넣은 것
    answer = W*H +1
    
    solve(0, brick)
    
    print('#{} {}'.format(t+1, answer))


