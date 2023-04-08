
# 어렵다!!!!

# 진짜로 모든 경우의 수 다 확인
# (W^W)*N 회 탐색... WOW!
# 마지막 N회차까지 탐색해야해!!!
# dfs, bfs 할 때 누적 값 어떻게 받을지 봐야해!

from copy import deepcopy # 2차원 배열 copy
from collections import deque

# 좌표가 너무 헷갈리네

# map[i][j] , map[x][y]
# 좌우로 움직이고 싶을 땐 j를 변경
# 상하로 움직이고 싶을 땐 i를 변경
# solve에서 0 ~ W-1 탐색. j의 범위.
# bomb에서 0 ~ H-1 탐색. i의 범위.
# ex) map[i][j] -> i를 움직이면 H따라 탐색
def bomb(brick, bomb_w):
    # 현재 배열 복사. 원본을 해치지 않게하기 위함
    new_brick = deepcopy(brick)
    
    # 탐색하는 벽돌 q에 담음
    # 깨트리는건 한 번에
    # 선입선출
    q = deque()
    
    # 깨트릴 벽돌 탐색
    # 방문하면 무조건 폭파
    for bomb_h in range(H):
        # 블록이 있는지 확인
        if new_brick[bomb_w][bomb_h]:
            if new_brick[bomb_w][bomb_h] > 1:
                # 지금 당장 해당 블록 말고 추가로 깨트려야하는 벽돌 존재
                # 튜플 형식으로 좌표, 값 넣어줌
                q.append( (bomb_w, bomb_h, new_brick[bomb_w][bomb_h]) )
            # 확인된 벽돌은 바로 깨트린다.
            new_brick[bomb_w][bomb_h] = 0
            break
        
    # while문을 타지 않는 경우
    # 탐색했는데 모든 값이 0
    # 1벽돌 하나 깸
    
    # 1보다 큰 벽돌 하나 깨면 바로 queue
    while q:
        w, h, bn = q.popleft()
        # 튜플 원소로 확인
        # 현재 블록에서 상하좌우로 추가로 깨트려야하는 블록 탐색
        for dw, dh in [(1,0), (-1,0), (0,1), (0,-1)]:
            for bnn in range(1, bn):
                nw = w + dw*bnn
                nh = h + dh*bnn
                # brick 배열을 넘지 않는 선에서
                if 0 <= nh < H and 0<= nw < W:
                    # 추가로 깨트려야하는 벽돌 존재
                    if new_brick[nw][nh] > 1:
                        q.append( (nw, nh, new_brick[nw][nh]) )
                    # 확인된 벽돌은 바로 깨트린다.
                    new_brick[nw][nh] = 0
    
    return new_brick
            
def gravity(brick):
    
    new_brick = deepcopy(brick)
    
    
            


# 와... dfs, bfs 둘 다 쓰네... 미쳤네;;
def solve(cnt, brick):
    # 전역변수
    global answer
    
    # cnt N에 도달한 모든 배열의 블록 개수 확인ㅋㅋㅋㅋㅋㅋ
    if cnt == N:
        cnt_brick = 0
        for w in range(W):
            for h in range(H):
                if brick[w][h]:
                    cnt_brick += 1
        answer = min(answer, cnt_brick)
        return
    
    for w in range(W):
        # 현재 블록배열과 깨트릴 열 정보를 줌
        new_brick = bomb(brick, w)
        
        #
        new_brick = gravity()
        
        # i 단계에서 0 ~ W-1 또 돌림ㅋㅋㅋㅋㅋㅋㅋ...
        # 진짜 모든 경우의 수를 확인하는구나....
        solve(cnt+1, new_brick)


T = int(input())

for t in range(T):
    N, W, H = map(int, input().split())
    brick = [ list(map(int, input().split())) for _ in range(H) ]
    
    # 무슨의미일까?
    # min 값을 return하기 위해서 가장 큰 값 넣은 것
    answer = W*H +1
    
    print('#{} {}'.format(t, answer))






























