
# 구슬을 한 칸 씩 움직이는 것이 아닌, 모든 구슬쌍에 대해 충돌이 일어나는지 확인
# 시간순으로 정렬하여 먼저 충돌이 일어나는 구슬쌍부터 문제 조건에 맞춰 합치기
# 일어날 수 있는 모든 충돌의 개수는 모든 구슬쌍에 해당하는 N*N

# 각 구슬쌍에 대해 전부 충돌시간을 구함
# 두 구슬을 비교
# 구슬의 방향이 동일하면 충돌 일어날 수 없다
# 1. 두 구슬의 이동 방향이 동일하면 충돌 일어날 수 없음
# 2. 이동 방향이 반대. x or y가 동일. 두 구슬의 거리를 반으로 나눈만큼 움직였을 때 같은 위치로 도달
# 3. 이동 방향이 ㄱ,ㄴ x,y좌표차이가 일치해야함

mapper = {'U':0, 'R':1, 'L':2, 'D':3}

n = 0
marbles = []
collisions = []
last_collision_time = -1
disappear = []

def cmp(marble):
    _,_,w,_,num = marble
    return (-w, -num) # 역순


# 구슬의 k초 후 위치를 반환
def move(marble, k):
    dx = [0, 1, -1, 0]
    dy = [1, 0, 0, -1]
    
    x,y,_,d,_ = marble
    return (x+dx[d]*k, y+dy[d]*k)


def collision_occur_time(marble1, marble2):
    x1, y1,_,d1,_ = marble1
    x2, y2,_,d2,_ = marble2
    
    # 두 구슬 방향이 같은 경우
    if d1 == d2:
        return -1
    
    # 두 구슬의 방향이 반대방향
    # x 또는 y가 일치해야함
    if d1+d2 == 3:
        if x1 != x2 and y1 != y2:
            return -1
        
        # 처음에 모든 좌표를 2배씩 했기 때문에 좌표는 무조건 2의배수
        # 동일하지 않은 좌표값들의 차이를 구해줌
        dist = abs(x1-x2) if x1 != x2 else abs(y1-y2)
        #dist = 0
        #if x1 != x2:
            #dist = abs(x1-x2)
        #else:
            #dist = abs(y1-y2)
        
        # 두 구슬의 만날 수 있는 절반 지점
        half = dist//2
        if move(marble1, half) == move(marble2, half):
            return half
        else:
            return -1
    
    # ㄱ,ㄴ 충돌 고려. 길이가 같으면 move 결과 보기
    x_dist, y_dist = abs(x1-x2), abs(y1-y2)
    if x_dist == y_dist and move(marble1, x_dist) == move(marble2, x_dist):
        return x_dist
    else:
        return -1
        
        
def arrange_collisions():
    # 모든 구슬 탐색
    for i in range(n):
        for j in range(i+1,n):
            # 두 구슬의 충돌 시간을 구함
            time = collision_occur_time(marbles[i], marbles[j])
            if time != -1:
                # 몇 초 후 볓번쨰 구슬들이 충돌하는지 구함
                collisions.append((time, i, j))
    
    #  가장 먼저 발생하는 충돌 순서대로 정렬
    collisions.sort()


def simulate():
    global last_collision_time
    
    # mi2 구슬은 충돌로 소멸
    for time, mi1, mi2 in collisions:
        # 둘 중 하나라도 없어진 구슬이면 충돌 pass
        if disappear[mi1] or disappear[mi2]:
            continue
        
        disappear[mi2] = True
        last_collision_time = time



T = int(input())
for _ in range(T):
    
    n = int(input())
    
    marbles = []
    collisions = []
    last_collision_time = -1
    disappear = [0 for _ in range(n+1)]
    
    for i in range(n):
        x,y,w,d = tuple(input().split())
        # 좌표를 2배로 늘려서 1초에 한 칸 이동으로 계산
        x,y,w = 2*int(x),2*int(y),int(w)
        marbles.append((x,y,w,mapper[d],i))
    
    # cmp로 함수 만들어서 정렬
    marbles.sort(key=cmp)
    
    # 모든 구슬쌍에 대해 충돌이 일어나는 경우를 구해서 시간순 정렬
    arrange_collisions()
    
    # 가능한 충돌 진행 중 사라지는 구슬에 대해 탐색
    simulate()
    
    print(last_collision_time)
    


