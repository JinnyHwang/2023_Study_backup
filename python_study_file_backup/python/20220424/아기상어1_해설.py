
# 아 머리아포
# 바로바로 변경하고, visited해서 변경하지 말고
# queue에 담아서 한 번에 처리하고 보기
# 그러면 visited 가장 작은 수 처리 하지 않아도 되고!
# 자 다시 한 번 봐보자구

from collections import deque



shark_y = -1
shark_x = -1
shark_size = 2
result = 0

N = int(input())
fish = []

for y in range(N):
    fish.append( list(map(int, input().split())) )
    if 9 in fish[y]:
        for x, v in enumerate(fish[y]):
            if v == 9:
                shark_y = y
                shark_x = x
                fish[y][x] = 0

# 현재 사이즈에서 먹을 수 있는 물고기 확인
def bfs(sy, sx, shark_size):
    # 상하좌우
    d = [ (-1,0), (1,0), (0,-1), (0,1) ]
    
    q = deque()
    # 맨 마지막 원소에는 이동 횟수
    q.append( (sy, sx, 0) )
    visited = [ [0]*N for _ in range(N) ]
    eat = []
    
    while q:
        
        y, x, time = q.popleft()
        
        # 이미 방문
        if visited[y][x] != 0:
            continue
        
        # 이 물고기를 언제 먹었는지 기록
        visited[y][x] = time
        
        # 먹을 수 있는 물고기 eat에 모조리 저장
        if fish[y][x] != 0 and fish[y][x] < shark_size:
            # eat queue는 time이 맨 앞
            eat.append( (time, y, x) )
            
        # fish 전체를 탐색
        for dy, dx in d:
            ny = y + dy
            nx = x + dx
            if 0 <= ny < N and 0 <= nx < N and fish[ny][nx] <= shark_size :
                q.append( (ny, nx, time+1) )
    
    # 먹을 수 있는 물고기 0
    if not eat:
        return (-1, -1, -1)
    
    # time이 가장 짧은 좌표 확인.
    # 값이 같을 경우 y, x 순으로 정렬
    # 더 위에 있는 것, 더 왼쪽에 있는 것
    # y, x 값이 더 작은 순서대로 정렬되어 있음
    eat.sort()
    fish[ eat[0][1] ][ eat[0][2] ] = 0
    return eat[0]



isContinue = True
while isContinue:
    # 상어 사이즈 늘리기
    # 상어 크기 만큼 bfs 돌림
    # -1은 더이상 먹을 물고기 없음
    for i in range(shark_size):
        # 먹을 물고기 return
        time, y, x = bfs(shark_y, shark_x, shark_size)
        #print(shark_size, time, y, x)
        
        if time == -1:
            isContinue = False
            break
        
        shark_y = y
        shark_x = x
        result += time
    else:
        shark_size += 1

print(result)

    
#fish = [ [0]*N for _ in range(N) ]
#for y in range(N):
#    fish[y] = list( map(int, input().split()) )
#    for x in range(N):
#        if fish[y][x] == 9:
#            shark_pos = [y, x]
#            fish[y][x] = 0











