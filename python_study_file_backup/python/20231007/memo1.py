
'''
구슬의 개수 M이 격자의 크기에 해당하는 N*N만큼 커질 수 있기 때문에
구슬의 목록을 격차 내에 직접 표시하여 관리해도
시간복잡도, 공간복잡도 모두 크게 차이나지 않음
격자 내에서 구슬의 상태를 관리
'''

# 방향값을 0,1,2,3으로 사용하기 때문에 빈칸은 -1로 표기
BLANK = -1
COLLIDE = -2

T = int(input())
N, M = 0, 0
#N, M = tuple(map(int, input().split()))
curr_dir = list()
next_dir = list()

'''
mapper = {'U':0, 'D':1, 'R':2, 'L':3}
dx = [-1, 1, 0, 0]
dy = [0, 0, 1, -1]
'''

# U,D 0,3 / L,R 1,2 반대방향을 대칭으로 처기
# 방향 틀기는 3-dir
mapper = {'U':0, 'L':1, 'R':2, 'D':3}
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]


def in_range(x,y):
    return 0 <= x and x < N and 0 <= y and y < N


# next_dir을 채움
def set_next_dir(x,y,d):
    #print('set_next_dir?', x,y,d)
    if next_dir[x][y] == BLANK:
        next_dir[x][y] = d
    else:
        next_dir[x][y] = COLLIDE


'''
    구슬이 벽에 부딪히면 움직이는 방향이 반대로 뒤집혀 동일한 속도로 움직이는 것을 반복합니다.
    이때 역시 방향을 바꾸는 것까지 포함해 정확히 1초의 시간이 소요됩니다.
    '''
def move(x,y,d):
    
    nx = x + dx[d]
    ny = y + dy[d]
    #print('nx,ny?',nx,ny)
    
    # 벽이 없다 전진
    if in_range(nx,ny):
        set_next_dir(nx,ny,d)
    # 벽이 있다 방향 틀기
    else:
        set_next_dir(x,y,3-d)
        
    

def move_all():
    global next_dir
    next_dir = [[BLANK for _ in range(N)] for _ in range(N)]
    
    for i in range(N):
        for j in range(N):
            if curr_dir[i][j] != BLANK:
                move(i,j,curr_dir[i][j])
                
    #print(curr_dir)
    #print(next_dir)
    
    for i in range(N):
        for j in range(N):
            if next_dir[i][j] == BLANK or next_dir[i][j] == COLLIDE:
                curr_dir[i][j] = BLANK
            else:
                curr_dir[i][j] = next_dir[i][j]



for _ in range(T):
    
    N, M = tuple(map(int, input().split()))
    
    # 초기화
    curr_dir = [[BLANK for _ in range(N)] for _ in range(N)]
    
    for _ in range(M):
        x, y, d = tuple(input().split())
        x, y = int(x)-1, int(y)-1
        curr_dir[x][y] = mapper[d]
    
    #print(T)
    #print(curr_dir)
    #print(next_dir)
    
    # 아주 오랜시간이 흐른 후..?
    # 구슬을 2*N번 반복하면 구슬은 다시 초기 위치, 초기 방향을 가지기 때문에
    # 2*N번 이후에는 충돌이 절대 일어날 수 없음
    for _ in range(2*N):
        move_all()
    
    
    ans = sum(curr_dir[x][y] != BLANK for x in range(N) for y in range(N))
    print(ans)






