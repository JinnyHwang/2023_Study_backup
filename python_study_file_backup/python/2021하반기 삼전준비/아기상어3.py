
# 매번 모든 물고기까지의 거리 구하지 말아라! -> 내가 쓴 방법....
# BFS 탐색으로 가장 먼저 만나는 물고기
# 최단거리 탐색으로 가장 먼저 만나는 물고기를 찾아라!!

from collections import deque
# x, y
shark_x = 0
shark_y = 0
shark_size = 2
time = 0

n = int(input())
mat = []

for x in range(n):
    mat.append( list(map(int, input().split())) )
    if 9 in mat[x]:
        for y, m in enumerate(mat[x]):
            if m == 9:
                shark_x = x
                shark_y = y
                mat[x][y] = 0
                
#print(mat, shark_x, shark_y, mat[shark_x][shark_y])


def bfs(startX, startY, shark):
    move = [(-1, 0), (0, -1), (0, 1), (1, 0)]
    q = deque()
    q.append((startX, startY, 0))
    dist = [[0]*n for _ in range(n)]
    eat = []
    
    while q:
        #print("start q:",q)
        x, y, c = q.popleft()
        #print(x, y, c)
        #print("q2:",q)
        # 이미 먹은 물고기면 pass
        if dist[x][y] != 0:
            continue
        # 해당 물고기를 언제 먹었는지 time 기록
        dist[x][y] = c
        
        if mat[x][y] != 0 and mat[x][y] < shark:
            # 가장 가까운 물고기 정렬을 위해 c(걸린시간)를 맨 앞 원소로
            eat.append((c, x, y))
        #print("q3:",q)
        
        # 지금 위치 상하좌우에서 먹을 수 있는 물고기 확인
        for i, j in move:
            cx = x+i
            cy = y+j
            if 0<=cx<n and 0<=cy<n and mat[cx][cy] <= shark:
                q.append((cx, cy, c+1))
        
        #print("end q:",q)
    
    #print('can eat fish:', eat)
                
    # 먹을 수 있는 물고기 없으면 없는 좌표 return
    if not eat:
        return (-1, -1, -1)
        
    # 먹을 수 있는 물고기 중 가장 가까운 물고기로 정렬
    eat.sort()
    mat[eat[0][1]][eat[0][2]] = 0
    # (time, x, y)
    return eat[0]

isContinue = True
while isContinue:
    # 상어 크기 키우기 위함
    for i in range(shark_size):
        c, x, y = bfs(shark_x, shark_y, shark_size)
        
        if c == -1:
            isContinue = False
            break
        shark_x = x
        shark_y = y
        time += c
    else:
        shark_size += 1

print(time)

