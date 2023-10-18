
# 시뮬막막...

# 구슬의 우선순위 무게, 구슬번호

# 2초에 한 칸씩 동일한 속도로 정해진 방향으로 움직이고 있습니다
# 충돌은 두 구슬이 이동하는 도중에 발생할 수도 있습니다
# 1초 가는 중, 2초 도착점
# 방향 변동 없음, 격자 벗어남 없음
# 구슬은 단방향으로 직진

mapper = {'U':0, 'L':1, 'R':2, 'D':3}
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

T = int(input())
marbles = []
move_marbles = []
next_marbles = []



def move_check():
    
    global move_marbles
    move_marbles = []
    
    for x, y, w, d, num in marbles:
        move_marbles.append((x+dx[d], y+dy[d], w, d, num))
    

def collide_check():
    
    global next_marbles, move_marbles
    next_marbles = []
    
    # marbles를 기준으로 move_marbles과 비교
    # 1초에 지나가면서 부딪힌 구슬 먼저 확인
    # marbles의 좌표와 next_marbles좌표가 같은데 방향이 (U marbles y > D marbles y) or (L marbles x > R marbles x)
    # next_marbles에 비교한 move_marbles을 넣지 않음(비교주체가 우선순위가 높은 구슬
    for i1, x1,y1,_,d1,_ in enumerate(marbles):
        for i2 in range(i1+1, len(marbles)):
            x2,y2,_,d2,_ = move_marbles[i2]
            if (x1,y1) == (x2,y2) and d1+d2 == 3 and ((d1 == 0 and y1 > y2) or (d1 == 1 and x1 > x2)):
                continue
            else:
                next_marbles.append(move_marbles[i2])
    # 쓸데없는 확인 줄이고 싶은데.. 흠...
    
    move_marbles = []
    # 2초 구슬 비교
    # next_marbles 내 x,y 좌표가 동일한 구슬이 있다면 뒷구슬 move_marbles에 넣지 않음
    for i3, x3,y3,_,_,_ in enumerate(next_marbles):
        for i4 in range(i3+1, len(next_marbles)):
            if (x3,y3) == next_marbles[i4][:2]:
                continue
    
    return move_marbles
    
    

# 더이상 충돌이 일어날 수 없다는 것은 어떻게 알 수 있나?
# 1. 같은 x좌표에 위치. U,D 방향 존재. U의y > D의y
# 2. 같은 y좌표에 위치. L,R 방향 존재. L의x > R의x
# 3. U,D구슬 L(U,D의x보다큼),R(U,D의x보다작음)확인 (L,R의y - U,D의y) == (L,R의x - U,D의x)
# 4. L,R구슬 U(L,R의y보다큼),D(L,R의y보다작음)확인 (L,R의y - U,D의y) == (L,R의x - U,D의x)

# 충돌이 일어나지 않으면 False 반환
def check_post_col():
    return Flase



def simulate():
    global marbles

    N = int(input())
    marbles = []
    
    # 구슬 번호가 작은 순서면 n을 역순으로 돌리면 됨
    for n in range(N):
        x, y, w, d = tuple(input().split())
        x, y, w = int(x), int(y), int(w)
        marbles.append((x,y,w,mapper[d],n))
    print(marbles)
    # 우선순위 정렬
    marbles = sorted(marbles, key=lambda x : (x[2], x[4]), reverse = True)
    print(marbles)
    
    time_cnt = 0
    while(True):
        
        if not check_post_col():
            # 충돌이 전혀 일어나지 않은 경우 -1로 초기화
            if time_cnt == 0 :
                time_cnt = -1
            break
            
        # move_marbles 확인
        move_check()
        
        # 충돌 marbles, move_marbles 비교해서 next_marbles 확인
        marbles = collide_check()
        
        time_cnt +=  2
        
    
    # 가장 마지막으로 충돌이 일어난 시간이 언제인지를 출력
    print(time_cnt)


for _ in range(T):
    simulate()

