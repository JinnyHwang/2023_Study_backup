# 해설 확인
# 맨 처음에 구조체 설계와 어떻게 활용할지 보는게 가장 중요
import heapq

MAX_N = 2000
n, m, p = 0, 0, 0

# 각 토끼의 id 기록
pid = [0]*(MAX_N + 1)

# 각 토끼의 이동거리
pw = [0]*(MAX_N + 1)

# 점프 횟수 기록
jump_cnt = [0]*(MAX_N + 1)

# 각 토끼 점수 기록
result = [0]*(MAX_N + 1)

# 각 토끼 현재 위치 좌표
point = [(0,0)]*(MAX_N + 1)

# 토끼 고유넘버 idx로 변환
id_to_idx = {}

# 달리기 여부 기록
is_runned = [0]*(MAX_N + 1)

# 획득점수 모조리 합산
# 개별토끼한테는 마이너스 점수 기록
total_sum = 0


# 구조체 rabbit 정리
class Rabbit:
    # 좌표, 점프카운트, pid 정보를 가짐
    def __init__(self, x, y, j, pid):
        self.x = x
        self.y = y
        self.j = j
        self.pid = pid

    # 이동할 토끼를 결정하기 위한 정렬함수
    def __lt__(self, other):
        if self.j != other.j:
            return self.j < other.j
        if self.x + self.y != other.x + other.y:
            return self.x + self.y < other.x + other.y
        if self.x != other.x:
            return self.x < other.x
        if self.y != other.y:
            return self.y < other.y
        return self.pid < other.pid


# 가장 긴 위치 판단
# 가장 멀리 있는 토끼 우선순위 확인을 위함
# 토끼 객체를 보고 true, false return
def compare(a, b):
    if a.x + a.y != b.x + b.y:
        return a.x + a.y < b.x + b.y
    if a.x != b.x:
        return a.x < b.x
    if a.y != b.y:
        return a.y < b.y
    return a.pid < b.pid


def init(inp):
    global n,m,p
    
    n, m, p, *rabbits = inp
    for i in range(1, p+1):
        pid[i] = rabbits[i*2-2]
        pw[i] = rabbits[i*2-1]
        
        id_to_idx[pid[i]] = i
        point[i] = (1,1)
        

def copy_rabbit(rabbit):
    # 구조체 형식으로 return
    return Rabbit(rabbit.x, rabbit.y, rabbit.j, rabbit.pid)

def get_up_rabbit(cur_rabbit, dis):
    up_rabbit = cur_rabbit
    # 이동거리 구하기
    # 1 ≤ di ≤ 1,000,000,000
    # 하나씩 이동하면 무조건 시간초과
    # n개의 칸에서 토끼가 뛸 수 있는 횟수는 n-1
    # 벽에 부딪혀 되돌아오는 것을 고려하면 2*n길이에서 2*(n-1)번 움직일 수 있음
    # 중복 횟수 빼는 계산
    dis = dis%(2*(n-1))
    
    # 올라갈 길이 확인
    if dis >= up_rabbit.x -1:
        dis -= (up_rabbit.x -1) # 이동횟수 만큼 뺴주기
        cur_rabbit.x = 1 # 맨 위에 위치
    else:
        up_rabbit.x -= dis
        dis = 0
        
    # 남은 길이 down방향으로 확인
    if dis >= n - up_rabbit.x:
        dis -= (n - up_rabbit.x)
        up_rabbit.x = n # 맨 밑으로 이동 시킴
    else:
        up_rabbit.x += dis
        dis = 0
    
    # 다시 up 방향
    up_rabbit.x -= dis
    return up_rabbit
        
        
def get_down_rabbit(cur_rabbit, dis):
    down_rabbit = cur_rabbit
    # 이동거리 구하기
    # 1 ≤ di ≤ 1,000,000,000
    # 하나씩 이동하면 무조건 시간초과
    # n개의 칸에서 토끼가 뛸 수 있는 횟수는 n-1
    # 벽에 부딪혀 되돌아오는 것을 고려하면 2*n길이에서 2*(n-1)번 움직일 수 있음
    # 중복 횟수 빼는 계산
    dis = dis%(2*(n-1))
    
    # 남은 길이 down방향으로 확인
    if dis >= n - down_rabbit.x:
        dis -= (n - down_rabbit.x)
        down_rabbit.x = n # 맨 밑으로 이동 시킴
    else:
        down_rabbit.x += dis
        dis = 0
        
    # 올라갈 길이 확인
    if dis >= down_rabbit.x -1:
        dis -= (down_rabbit.x -1) # 이동횟수 만큼 뺴주기
        down_rabbit.x = 1 # 맨 위에 위치
    else:
        down_rabbit.x -= dis
        dis = 0
    
    # 다시 down 방향
    down_rabbit.x += dis
    return down_rabbit


def get_left_rabbit(cur_rabbit, dis):
    left_rabbit = cur_rabbit
    # 이동거리 구하기
    # 1 ≤ di ≤ 1,000,000,000
    # 하나씩 이동하면 무조건 시간초과
    # n개의 칸에서 토끼가 뛸 수 있는 횟수는 n-1
    # 벽에 부딪혀 되돌아오는 것을 고려하면 2*n길이에서 2*(n-1)번 움직일 수 있음
    # 중복 횟수 빼는 계산
    dis = dis%(2*(n-1))
    
    # 좌로 갈 수 있는 길이 확인
    if dis >= left_rabbit.y -1:
        dis -= (left_rabbit.y -1) # 이동횟수 만큼 뺴주기
        left_rabbit.y = 1 # 맨 위에 위치
    else:
        left_rabbit.y -= dis
        dis = 0
        
    # 남은 길이 우측 방향으로 확인
    if dis >= n - left_rabbit.y:
        dis -= (n - left_rabbit.y)
        left_rabbit.y = n # 맨 밑으로 이동 시킴
    else:
        left_rabbit.y += dis
        dis = 0
    
    # 다시 left 방향
    left_rabbit.y -= dis
    return left_rabbit
        
        
def get_right_rabbit(cur_rabbit, dis):
    right_rabbit = cur_rabbit
    # 이동거리 구하기
    # 1 ≤ di ≤ 1,000,000,000
    # 하나씩 이동하면 무조건 시간초과
    # n개의 칸에서 토끼가 뛸 수 있는 횟수는 n-1
    # 벽에 부딪혀 되돌아오는 것을 고려하면 2*n길이에서 2*(n-1)번 움직일 수 있음
    # 중복 횟수 빼는 계산
    dis = dis%(2*(n-1))
    
    # 남은 길이 우측 방향으로 확인
    if dis >= n - right_rabbit.y:
        dis -= (n - right_rabbit.y)
        right_rabbit.y = n # 맨 밑으로 이동 시킴
    else:
        right_rabbit.y += dis
        dis = 0
        
    # 좌로 갈 수 있는 길이 확인
    if dis >= right_rabbit.y -1:
        dis -= (right_rabbit.y -1) # 이동횟수 만큼 뺴주기
        right_rabbit.y = 1 # 맨 위에 위치
    else:
        right_rabbit.y -= dis
        dis = 0
    
    # 다시 right 방향
    right_rabbit.y += dis
    return right_rabbit




def start_round(inp):
    global total_sum, is_runned
    
    k, bonus = inp
    rabbi_pq = []
    
    # 점프여부 초기화
    for i in range(1,p+1):
        is_runned[i] = False
    
    # p마리 토끼들 모두 priority queue에 넣어줌
    for i in range(1,p+1):
        x,y = point[i]
        # Rabbit 구조체 사용해서 객체 생성
        new_rabbit = Rabbit(x, y, jump_cnt[i], pid[i])
        # __lt__(self, other)에서 정의한 표준 정렬 순서에 따라 heapq 저장됨
        # heapq 정렬 시 구조체 활용하기!
        heapq.heappush(rabbi_pq, new_rabbit)
    
    for _ in range(k):
        cur_rabbit = heapq.heappop(rabbi_pq)
        
        # 상, 하, 좌, 우 4개 방향으로 이동
        # 각 방향으로 이동 후 최종위치를 구함
        # 시작점으로부터 벌리 있는 위치 확인
        dis = pw[id_to_idx[cur_rabbit.pid]]
        nex_rabbit = copy_rabbit(cur_rabbit)
        nex_rabbit.x = 0
        nex_rabbit.y = 0
        
        # 토끼 위로 이동 시키기
        up_rabbit = get_up_rabbit(copy_rabbit(cur_rabbit), dis)
        # 지금까지의 도착지들보다 더 멀리 가는 것이 가능하면 도착지 갱신
        if compare(nex_rabbit, up_rabbit):
            nex_rabbit = up_rabbit
            
        # 하
        down_rabbit = get_down_rabbit(copy_rabbit(cur_rabbit), dis)
        if compare(nex_rabbit, down_rabbit):
            nex_rabbit = up_rabbit
            
        # 좌
        left_rabbit = get_left_rabbit(copy_rabbit(cur_rabbit), dis)
        if compare(nex_rabbit, left_rabbit):
            nex_rabbit = up_rabbit
            
        # 우
        right_rabbit = get_right_rabbit(copy_rabbit(cur_rabbit), dis)
        if compare(nex_rabbit, right_rabbit):
            nex_rabbit = up_rabbit
        
        nex_rabbit.j += 1
        heapq.heappush(rabbi_pq, nex_rabbit)
        
        # 배열들도 갱신
        nex_idx = id_to_idx[nex_rabbit.pid]
        point[nex_idx] = (nex_rabbit.x, nex_rabbit.y)
        jump_cnt[nex_idx] = nex_rabbit.j
        is_runned[nex_idx] = True
        
        # 토끼가 받는 점수는?
        # 현재 토끼한테 마이너스 점수를 기록함
        result[nex_idx] -= (nex_rabbit.x + nex_rabbit.y)
        total_sum += (nex_rabbit.x + nex_rabbit.y)
    
    # bonus 점수를 받는 토끼는?
    # 가장 멀리있는 토끼!
    bonus_rabbit = Rabbit(0,0,0,0)
    while rabbi_pq:
        cur_rabbit = heapq.heappop(rabbi_pq)
        
        if not is_runned[id_to_idx[cur_rabbit.pid]]:
            continue
        
        if compare(cur_rabbit, bonus_rabbit):
            bonus_rabbit = cur_rabbit
            
    result[id_to_idx[cur_rabbit.pid]] += bonus
        

def power_up(inp):
    pid, l = inp
    pw[id_to_idx[pid]] *= l
           



def print_result():
    ans = 0
    for i in range(1,p+1):
        ans = max(ans, result[i]+total_sum)
    print(ans)


q = int(input())
for _ in range(q):
    query, *inp = list(map(int, input().split()))
    
    if query == 100:
        init(inp)
    if query == 200:
        start_round(inp)
    if query == 300:
        power_up(inp)
    if query == 400:
        print_result()


