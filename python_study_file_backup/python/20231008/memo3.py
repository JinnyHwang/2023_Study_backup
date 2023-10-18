
mapper = {'U':0, 'L':1, 'R':2, 'D':3}
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]
marbles = []
max_w = -1

def cmp(marble):
    _,_,_,w,num = marble
    return(-w, -num)

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def move_all():
    global marbles
    
    for i, (x,y,d,w,num) in enumerate(marbles):
        nx = x+dx[d]
        ny = y+dy[d]
        if in_range(nx,ny):
            marbles[i] = (nx,ny,d,w,num)
        else:
            marbles[i] = (x,y,3-d,w,num)
        

def combine_all():
    
    new_marbles = []
    
    for i1, (x1,y1,d1,w1,num1) in enumerate(marbles):
        for i2, (x2,y2,d2,w2,num2) in enumerate(new_marbles):
            if (x1,y1) == (x2,y2):
                # 방향 정하기
                if num1 > num2:
                    nd = d1
                    nnum = num1
                else:
                    nd = d2
                    nnum = num2
                new_marbles[i2] = (x2,y2,nd,w1+w2,nnum)
                break
        else:
            new_marbles.append(marbles[i1])
    
    return new_marbles
                

def simulate():
    global marbles
    
    # 모든 구슬 이동 or 방향전환
    move_all()
    
    # 구슬 병합 확인
    marbles = combine_all()
    

n, m, t = tuple(map(int, input().split()))

for i in range(m):
    x,y,d,w = tuple(input().split())
    x,y,w = int(x)-1, int(y)-1, int(w)
    marbles.append((x,y,mapper[d],w,i))
    
marbles.sort(key=cmp)

for _ in range(t):
    simulate()
    
    # 결과값 출력
    for _,_,_,w,_ in marbles:
        if max_w < w:
            max_w = w
    
print(len(marbles), max_w)









