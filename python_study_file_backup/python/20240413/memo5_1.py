from collections import deque

MAX_N = 31
MAX_L = 41
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

# grid
info = [[0 for _ in range(MAX_L)] for _ in range(MAX_L)]

# 기사 정보
bef_k = [0 for _ in range(MAX_N)]
r = [0 for _ in range(MAX_N)]
c = [0 for _ in range(MAX_N)]
h = [0 for _ in range(MAX_N)]
w = [0 for _ in range(MAX_N)]
k = [0 for _ in range(MAX_N)]
nr = [0 for _ in range(MAX_N)]
nc = [0 for _ in range(MAX_N)]
dmg = [0 for _ in range(MAX_N)]
is_moved = [False for _ in range(MAX_N)]


def try_movement(idx, move_dir):
    q = deque()
    is_pos = True
    
    # 모든 기사 초기화
    for i n range(1, n+1):
        dmg[i] = 0
        is_moved[i] = False
        nr[i] = r[i]
        nc[i] = c[i]
        
    q.append(idx)
    # 명령어 받은 기사는 움직임
    is_moved[idx] = True
    
    # 움직일 기사들 q에 담음
    while q:
        x = q.leftpop()
        
        # 다음 위치 초기화
        nr[x] += dx[dir]
        nc[x] += dy[dir]
        
        # 경계를 벗어나는지 확인
        # 기사 크기 구하는 것 1~l 사이에 있는지
        if nr[x] < 1 or nc[x] < 1 or nr[x] + h[x] -1 > l or nc[x] + w[x] -1 > l:
            return False
        
        # 지금 조각이 다른 조각이나 장애물하고 충돌하는가?
        for i in range(nr[x] , nr[x] + h[x]):
            for j in range(nc[x], nc[x] + w[x]):
                if info[i][j] == 1:
                    dmg[i][j] += 1
                elif info[i][j] == 2:
                    return False
                
        # 다른 조각과 충돌하는 경우
        for i in range(1, n+1):
            if is_moved[i] or k[i] <= 0:
                continue
            # q가 다음으로 갈 범위와 이미 기사가 차지하고있는 범위가 겹치는지 확인
            if r[i] + h[i] -1 < nr[x] or r[i] > nr[x] + h[x] -1:
                continue
            if c[i] + w[i] -1 < nc[x] or c[i] > nc[x] + w[x] -1:
                continue
            
            # 움직여야함
            is_moved[i] = True
            q.append(i)
    
    # 명령어를 받은 기사는 데미지를 받지 않음
    dmg[idx] = 0
    return True



def move_piece(idx, move_dir):
    # 체력이 바닥이면 return
    if k[idx] <= 0:
        return
    
    # 명령 받은 기사 움직이기 시작
    if try_movement(idx, move_dir):
        # 갱신 정보로 초기화
        for i in range(1, n+1):
            r[i] = nr[i]
            c[i] = nc[i]
            k[i] -= dmg[i]
    
    
    
l, n, q = map(int, input().split())
for i in range(1, l+1):
    info[i][1:] = map(int, input().split())
for i in range(1, n+1):
    r[i], c[i], h[i], w[i], k[i] = map(int, input().split())
    bef_k[i] = k[i]
    
        
for _ in range(q):
    idx, d = map(int, input().split())
    def move_pice(idx, d)


ans = sum([ bef_k[i]-k[i] for i in range(1, n+1) if k[i] > 0])
print(ans)


