
# 이번 map에서 최대로 탐색할 k 구함

# 아니다 이렇게 하는게 아님

# 마름모의 정의를 활용
# 격자를 순회하며 마름모 중심 후보를 정함
# 마름모의 중심위치와 k가 주어지면 특정 위치가 마름모에 포함되어 있는지 어떻게 알 수 있을까?
# 마름모 중앙위치와 임의의 위치의 차를 보면 됨
# (a,b)와 (c,d)의 x,y 좌표 차이
# |a-c|+|b-d|가 k랑 같거나 작으면 마름모 범위 안

# 그럼 가능한 K의 범위는 어떻게 구할 수 있는가?
# 최악의 경우를 산정해서 범위를 구한다
# 마름모가 모든 격자를 커버하려면 k의 크기는?
# 격자에서 잡을 수 있는 거리가 가장 먼 두 점을 커버하기 위해서는?
# N의 대각선 거리는? (1,1)과 (N,N) : (N-1)+(N-1) 즉 2*(N-1)이 최대 K 크기

'''
# 해설 1
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def mine_cost(k):
    return k*k+(k+1)*(k+1)


def get_num_of_gold(x, y, k):
    return sum(
            [grid[i][j]
            for i in range(n)
            for j in range(n)
            if abs(x-i)+abs(y-j) <= k]
        )
    
    
#    for i in range(n):
#        for j in range(n):
#            if abs(x - i) + abs(y - j) <= k:
#                if grid[i][j]:
#                    cnt += 1


max_k = 2*(n-1)
max_gold = 0

for i in range(n):
    for j in range(n):
        for k in range(max_k+1):
            now_gold = get_num_of_gold(i, j, k)
            if mine_cost(k) <= now_gold*m:
                max_gold = max(max_gold, now_gold)
            
print(max_gold) 
'''

'''
# 해설2
# 모든 격자를 다 탐색하는 것 은 비효율적
# 마름모 내부 영역만 탐색은 어떻게 할 수 있을까?

# 앞에서 탐색했던 k값에 누적해서 금의 개수를 더해주는 방식
# 가장자리는 어떻게 탐색?
# 4개 방향 값에 대해 미리 선언해서 x,y좌표 더하고 뺴고 하면서 찾아준다

# 마름모 중심위치와, k에 대해 내부에 있는 금의 개수를 구하고
# 가능한 k 범위에 대해 탐색하고
# 손해 보지 않고 채굴할 수 있는 최대 금의 개수 저장

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def mine_cost(k):
    return k*k+(k+1)*(k+1)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

# 주어진 k에 대해 채굴 가능한 금의 개수 return
def get_num_of_gold(x, y, k):
    num_of_gold = 0
    # 마름모 가장자리를 탐색하는 dx, dy 방향값
    dxs = [1, 1, -1, -1]
    dys = [1, -1, -1, 1]
    
    # 현재 위치 k = 0일 때
    num_of_gold += grid[x][y]
    
    for ck in range(1, k+1):
        # 가장 북쪽 위쪽 좌표를 시작점으로 함
        cx,cy = x-ck, y
        for dx, dy in zip(dxs, dys):
            # k크기만큼 순회
            for size in range(ck):
                if in_range(cx, cy):
                    num_of_gold += grid[cx][cy]
                cx = cx + dx
                cy = cy + dy
                    
    return num_of_gold



max_gold = 0

for i in range(n):
    for j in range(n):
        for k in range(2*(n-1)+1):
            now_gold = get_num_of_gold(i, j, k)
            
            if mine_cost(k) <= now_gold*m:
                max_gold = max(max_gold, now_gold)

print(max_gold)
'''

# 해설3
# 이전 k에서 구했던 값을 누적하기


n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def mine_cost(k):
    return k*k+(k+1)*(k+1)

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n



# 주어진 k에 대해 채굴 가능한 금의 개수 return
def get_num_of_gold_nowk(x, y, k):
    # 마름모 가장자리를 탐색하는 dx, dy 방향값
    dxs = [1, 1, -1, -1]
    dys = [1, -1, -1, 1]
    
    # 현재 위치 k = 0일 때
    if k == 0:
        return grid[x][y]
    
    num_of_gold = 0
    cx, cy = x-k, y
    for dx, dy in zip(dxs, dys):
        for size in range(k):
            if in_range(cx, cy):
                num_of_gold += grid[cx][cy]
            cx, cy = cx + dx, cy + dy
                    
    return num_of_gold



max_gold = 0

for i in range(n):
    for j in range(n):
        now_gold = 0
        for k in range(2*(n-1)+1):
            now_gold += get_num_of_gold_nowk(i, j, k)
            
            if mine_cost(k) <= now_gold*m:
                max_gold = max(max_gold, now_gold)

print(max_gold)

