
'''
완전탐색문제 많아 풀었다...

dfs, bfs좀 풀어볼까


 
'''

def bomb(brkck, bomb_w):
    new_brick = deepcopy(brick)
    
    # 추가로 부숴야 할 것 q에 저장
    q = deque()
    
    # 세로줄 쭉 탐색
    for bomb_h in range(H):
        if new_brick[bomb_h][bomb_w]:
            # 현재 블록으로 아래 블록도 깨지면 지금 블록 정보 input
            if new_brick[bomb_h][bomb_w] > 1:
                q.append( (bomb_h, bomb_w, new_brick[bomb_h][bomb_w]) )
            # 현재 블록은 0으로
            new_brick[bomb_h][bomb_w] = 0
            break
        
    # 만약 깨트린 블록이 1이면 while문 안타고 끝남
    while q:
        qh, qw, b = q.popleft()
        for dh, dw in [(1,0), (-1,0), (0,1), (0,-1)]:
            # 깨트린 블록의 숫자만큼
            for bb in range(1,b):
                nh = qh + dh*bb
                nw = qw + dw*bb
                if 0 <= nh < H and 0<= nw < W:
                    # 깨진 블록이 다른 블록을 깨트릴 수 있다?
                    # q에 append
                    if new_brick[nh][nw] > 1:
                        q.append((nh, nw, new_brick[nh][nw]))
                    new_brick[nh][nw] = 0 # 탐색 완료 블록 처리
        return new_brick
    
    
def gravity(arr):
    
    # 아래서부터 탐색
    # 맨 아래칸은 내릴 수 없으니까 빼고
    for h in range(H-2,-1,-1):
        for w in range(W):
            # 빈칸이 아니면?
            if arr[h][w] > 0:
                h2 = h
                while True:
                    h2 += 1
                    if 0 <= h2 < H and arr[h2][w] == 0:
                        arr[h2][w], arr[h][w] = arr[h][w], arr[h2][w]
                    else:
                        break
    return arr
    

def solve(cnt, brick):
    
    # turn이 끝나는 시점
    if cnt == N:
        # 모든 turn을 확인하고 그 중 블록 개수가 가장 작은 결과를 저장
        brick_cnt = 0
        for h in range(H):
            for w in range(W):
                if brick[h][w] > 0:
                    brick_cnt += 1
        answer = min(answer, brick_cnt)
        return
    
    # 아직 turn이 끝나기 전이면 탐색(재귀)
    # 지금 turn에서 시도할 수 있는 모든 경우의 수
    # 좌우로 이동
    for w in range(W):
        new_brick = bomb(brick,w)
        
        new_brick = gravity(new_brick)
        
        # 재귀 탐색. N회 도달할 때 까지
        solve(cnt+1, new_brick)




T = int(input())

for t in range(T):
    N, W, H = map(int, input().split())
    # W: 열 개수
    # H: 행 개수
    # brick[h][w]로 탐색
    brick = [ list(map(int, input().split())) for _ in range(H) ]

    # 답은 블록 개수를 세어라
    # 가질 수 있는 가장 큰 값+1
    answer = W*H+1
    
    # 게임 0회차 map 전달 
    solve(0, brick)
    