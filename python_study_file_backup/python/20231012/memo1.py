
from collections import deque

n, k, m = tuple(map(int, input().split()))
#rock_map = [list(map(int, input().split())) for _ in range(n)]
rock_map = [[0 for _ in range(n)] for _ in range(n)]
rocks_pos = []
rl = []
for i in range(n):
    rl = list(map(int, input().split()))
    for j in range(n):
        if rl[j] == 1:
            rocks_pos.append((i,j))
        rock_map[i][j] = rl[j]

start_pos = [tuple(map(int, input().split())) for _ in range(k)]
#start_pos = [(sx-1,sy-1) for sx,sy in start_pos]

#print(rock_map)
#print(rocks_pos)
#print(start_pos)

rock_index = []
rock_index_list = []
# rocks_pos 중 m개를 뽑아서 만들 수 있는 조합
def remove_rock(idx,cnt):
    global remove_rocks
    
    if cnt == m:
        #print('?', rock_index, type(rock_index))
        l = rock_index[:]
        #print(l == rock_index)
        #remove_rocks.append(rock_index)
        rock_index_list.append(l)
        #print(remove_rocks, type(rock_index))
        return
    
    if idx == len(rocks_pos):
        return

    # 포함
    rock_index.append(idx)
    remove_rock(idx+1, cnt+1)
    rock_index.pop()
    
    # 미포함
    remove_rock(idx+1, cnt)
    
remove_rock(0,0)
#print(rock_index_list)

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

def can_go(x,y):
    if not in_range(x,y):
        return False
    
    if visited[x][y] or rock_map[x][y]:
        return False
    
    return True

def move():
    dxs, dys = [-1,0,0,1], [0,-1,1,0]
    
    while q:
        cx, cy = q.popleft()
        
        for dx,dy in zip(dxs,dys):
            nx, ny = cx+dx, cy+dy
            if can_go(nx,ny):
                visited[nx][ny] = 1
                q.append((nx,ny))
            



visited = []
max_visit = -1

for ril in rock_index_list:
    #print('before', rock_map)  
    # 돌 없애기
    for idx in ril:
        rx,ry = rocks_pos[idx]
        rock_map[rx][ry] = 0
    #print('after', rock_map)    
    
    
    visited = [[0 for _ in range(n)] for _ in range(n)]
    # 탐색 start poiont queue에 input
    q = deque()
    for sx,sy in start_pos:
        sx,sy = sx-1,sy-1
        q.append((sx,sy))
        visited[sx][sy] = 1
    
    # 영역 확인
    move()
    #print('v?', visited)
    
    # visited
    curr_visit = sum([vv for v in visited for vv in v if vv == 1])
    #print('curr_visit?', curr_visit)
    max_visit = max(max_visit, curr_visit)
    
    # 돌 없애기
    for idx in ril:
        rx,ry = rocks_pos[idx]
        rock_map[rx][ry] = 1
    #print('end', rock_map)


print(max_visit)





