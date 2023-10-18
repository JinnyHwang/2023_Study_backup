from collections import deque

# 빙하로 둘러싸여있는 물 구하기
# 시작점으로부터 0의 영역을 구하는데
# 1이여서 못가는 경우 기록

# 빙하는 녹일 수 있는 물인가?
# 영역의 가장 바깥쪽 좌표를 보고
# 주변에 빙하인지 물인지 확인

# if x or y == 0 바깥쪽

# 빙하가 전부 녹는데 걸리는 시간과
# 마지막으로 녹은 빙하의 크기(1의 개수) => 1개수 항상 기록 맨 마지막에 기록된 값 return
n, m = tuple(map(int, input().split()))
a = [list(map(int, input().split())) for _ in range(n)]
dxs, dys = [-1,0,0,1],[0,-1,1,0]

def grid_print(grid):
    for g in grid:
        for gg in g:
            print(gg,end=' ')
        print()

in_water_pos = []
visited = [[False for _ in range(m)] for _ in range(n)]
'''
# 안쪽 물 확인
in_water_pos = []
for i in range(1,n):
    for j in range(1,m):
        if a[i][j] == 0:
            in_water_pos.apprnd((i,j))
'''

# in_water_pos 안에 들어갈 수 있는 0은
# SIDE_X, SIDE_Y 영역 안쪽!
def fill_in_water_pos():
    global in_water_pos
    
    in_water_pos = []
    for i in range(SIDE_X+2, n-SIDE_X-2):
        for j in range(SIDE_Y+2, m-SIDE_Y-2):
            if a[i][j] == 0:
                in_water_pos.append((i,j))
# n,m 3이상
def in_range(x,y):
    #print(SIDE_X, n-SIDE_X-1, SIDE_Y,  m-SIDE_Y-1)
    return SIDE_X < x and x < n-SIDE_X-1 and SIDE_Y < y and y < m-SIDE_Y-1


def water_can_melt():
    global q, outsied, melt_chk, visited
    
    while q:
        cx, cy = q.pop()
        outsied.add((cx,cy))
        for dx,dy in zip(dxs,dys):
            nx, ny = cx+dx, cy+dy
            if in_range(nx,ny):
                if not visited[nx][ny]:
                    if not a[nx][ny]:
                        q.append((nx,ny))
                        visited[nx][ny] = True
            else:
                # 바깥쪽 물과 맞닿아있음 빙하 녹임
                melt_chk = True




q = deque()
melt_chk = False
outsied = set()
# 빙하 영역 확인
def chk_in_water_pos():
    global q, visited, outsied, melt_chk, a
    
    q = deque()
    visited = [[False for _ in range(m)] for _ in range(n)]
    print('?', in_water_pos)
    # 물 확인
    fill_in_water_pos()
    print('!', in_water_pos)
    for sx,sy in in_water_pos:
        if not visited[sx][sy]:
            q.append((sx,sy))
            visited[sx][sy] = True
            # 탐색 시작
            outsied = set()
            melt_chk = False
            # 0의 영역 확인
            water_can_melt()
            print(outsied, melt_chk)
            
            if melt_chk:
                # 주변 빙하 녹이기
                for ox,oy in outsied:
                    for dx,dy in zip(dxs,dys):
                        nx, ny = ox+dx, oy+dy
                        if in_range(nx, ny) and a[nx][ny] == 1:
                            a[nx][ny] = 0
            else: # 빙하 못녹임
                continue
            
            
            
            
SIDE_X = 0
SIDE_Y = 0
# 시간이 지날 때 마다
last_a_cnt = sum([a[i][j] for i in range(n) for j in range(n) if a[i][j] == 1])
for t in range(1, n*m):
    
    print('! time:',t)
    grid_print(a)
    
    # 안쪽 물의 영역 확인
    chk_in_water_pos()
    
    print('step1 : ', t)
    grid_print(a)
    
    # 사이드에서 빙하 녹이기
    SIDE_X += 1
    SIDE_Y += 1
    #print(SIDE_X, (n-SIDE_X-1), SIDE_Y, (m-SIDE_Y-1))
    for i in range(n):
        for j in range(m):
            if i == SIDE_X or i == (n-SIDE_X-1) or j == SIDE_Y or j == (m-SIDE_Y-1):
                a[i][j] = 0           
    print('step2 : ', t)
    grid_print(a)

    # 바깥쪽 물로 인해 빙하 다 녹음
    if SIDE_X >= (n-SIDE_X-1) or SIDE_Y >= (m-SIDE_Y-1):
        #print(SIDE_X, (n-SIDE_X-1), SIDE_Y, (m-SIDE_Y-1))
        break
    
    # 남아있는 빙하 개수 기록
    curr_a_cnt = sum([a[i][j] for i in range(n) for j in range(n) if a[i][j] == 1])

    #curr_a_cnt = 1
    if curr_a_cnt == 0:
        break
    else:
        last_a_cnt = curr_a_cnt
    

print(t, last_a_cnt)




