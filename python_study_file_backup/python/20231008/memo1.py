
# 1초씩 시뮬 돌리려면 칸을 2배로 늘리기!
# 가장 마지막 충돌시간은?
# 좌표 범위는 -1,000 ≤ x ≤ 1,000 , -1,000≤ y ≤ 1,000
# 칸을 2배로 늘리면? `2000 ~ 2000
# 그럼 좌표의 최대 크기는 4000
# 모든 구슬은 4000번이 최대 그 이상은 범위를 벗어나기 때문
# 주어진 조건의 범위도 잘 생각하기!

# 위 조건을 고려해서 다시 풀어보기!
# 이동과 postion만 고려하면 될 

C = 2000

mapper = {'U':0, 'L':1, 'R':2, 'D':3}
dx = [0, -1, 1, 0]
dy = [1, 0, 0, -1]

T = int(input())
marbles = []
next_marbles = []


def out_of_active_coordinate(target):
    x,y = target
    return (-1)*C <= x and x <= C and (-1)*C <= y and y <= C


def simulate():
    global marbles, next_marbles, last_collision_time
    next_marbles = []
    
    #print(marbles)
    # move all
    for i, marble in enumerate(marbles):
        (x,y),w,d,n = marble
        nx = x + dx[d]
        ny = y + dy[d]
        marbles[i] = ((nx,ny),w,d,n)
    #print(marbles)
        
    for i in range(len(marbles)):
        target = marbles[i]
        # -2000~2000 범위를 벗어난 구슬을 out
        if out_of_active_coordinate(target):
            for (nx,ny),_,_,_ in next_marbles:
                #print('(nx,ny)? ', (nx,ny), '  target[0]? ', target[0])
                if target[0] == (nx,ny):
                    last_collision_time = curr_time
                    break
            else:
                next_marbles.append(target)
    #print(next_marbles)
    
    marbles = next_marbles[:]
    #for i in range(len(next_marbles)):
        #marbles.append(next_marbles[i])
        

for _ in range(T):
    
    curr_time = 0
    last_collision_time = -1
    
    N = int(input())
    
    # 구슬 번호가 작은 순서면 n을 역순으로 돌리면 됨
    for n in range(N):
        x, y, w, d = tuple(input().split())
        x, y, w = 2*int(x), 2*int(y), int(w)
        marbles.append(((x,y),w,mapper[d],n))
    #print('1:',marbles)
    # 우선순위 정렬
    marbles = sorted(marbles, key=lambda x : (x[1], x[3]), reverse = True)
    #print('2:',marbles)
    
    for i in range(1, 2*C + 1):
    #for i in range(1,4):
        curr_time = i
        # 구슬 이동
        simulate()
   
    # 가장 마지막으로 충돌이 일어난 시간이 언제인지를 출력
    print(last_collision_time)






