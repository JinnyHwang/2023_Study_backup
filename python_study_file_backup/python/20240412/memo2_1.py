
COORD_SIZE = 4000
OFFSET = 2000
BLANK = -1

t = int(input())
n = 0
marbles = []
next_marbles = []

next_marble_index = [[BLANK for _ in range(COORD_SIZE+1)] for _ in range(COORD_SIZE+1)]

curr_time = 0
last_collision_time = -1
mapper = {'U':0, 'D':1, 'L':2, 'R':3}


def move(marble):
    # 상 하 좌 우
    #dxs = [-1, 1, 0, 0]
    #dys = [0, 0, -1, 1]
    dxs = [0, 0, -1, 1]
    dys = [1, -1, 0, 0]
    x, y, w, d, i = marble
    nx, ny = x+dxs[d], y+dys[d]
    return (nx,ny,w, d, i)


def out_of_active_coordinate(marble):
    x, y, _, _, _ = marble
    return not(0 <= x <= COORD_SIZE) or not(0 <= y <= COORD_SIZE)

def collide(marble1, marble2):
    _, _, w1, _, mi1 = marble1
    _, _, w2, _, mi2 = marble2
    if (w1, mi1) > (w2, mi2):
        return marble1
    else:
        return marble2


def push_next_marble(marble):
    global last_collision_time
    # 범위 벗어나면 신경 안씀
    if out_of_active_coordinate(marble):
        return
    
    mx, my = marble[0], marble[1]
    idx = next_marble_index[mx][my]
    if idx == BLANK:
        next_marbles.append(marble)
        # 구슬 index값 기록
        next_marble_index[mx][my] = len(next_marbles)-1
    else:
        #next_marbles[idx], marble
        next_marbles[idx] = collide(next_marbles[idx], marble)
        last_collision_time = curr_time
    
    


def simulate():
    global marbles, next_marbles
    
    for marble in marbles:
        next_marble = move(marble)
        push_next_marble(next_marble)
    
    marbles = next_marbles[:]
    
    for x, y, _, _, _ in next_marbles:
        next_marble_index[x][y] = BLANK
    
    next_marbles = []


for _ in range(t):
    
    marbles = []
    last_collision_time = -1
    
    n = int(input())
    for i in range(1, n+1):
        x, y, w, d = input().split()
        x, y, w = OFFSET+int(x)*2, OFFSET+int(y)*2, int(w)
        marbles.append([x, y, w, mapper[d], i])
        
    # 모든 구슬이 영역 밖으로 벗어나면 종료
    for i in range(1, COORD_SIZE+1):
        curr_time = i
        simulate()

    print(last_collision_time)