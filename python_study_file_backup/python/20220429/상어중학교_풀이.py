
# 자매품 : 시계방향
def rotate_2(arr):
    new_arr = []
    
    #리스트, 튜플 해제해서 새로 묶음 zip(*arr)
    for z in zip(*arr):
        new_arr.append(reverse(list(z)))
    return new_arr


from collections import deque


# 인접블록 상하좌우
d = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(x, y, color):
    q = deque()
    q.append([x,y])
    
    total_block, rainbow_block = 1, 0
    normal, rainbow = [[x,y]], []
    
    while q:
        x,y = q.popleft()
        
        for di in d:
            nx = x + di[0]
            ny = y + di[1]
            
            if 0 <= nx < N and 0 <= ny < N:
                if not visited[nx][ny] and block_map[nx][ny] == color:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    total_block += 1
                    normal.append([nx,ny])
                    
                elif not visited[nx][ny] and block_map[nx][ny] == 0:
                    visited[nx][ny] = 1
                    q.append([nx,ny])
                    total_block += 1
                    rainbow_block += 1
                    rainbow.append([nx,ny])
        
    for pos in rainbow:
        visited[pos[0]][pos[1]] = 0
    
    #print('normal: ',normal)
    #print('rainbow: ',rainbow)
    # normal+rainbow에서 맨 앞에 있는 원소가 기준 블럭
    return [total_block, rainbow_block, normal+rainbow]
            

# 중력
def gravity(arr):
    
    # 바닥으로 떨궈야하기 때문에 밑에서부터 탐색
    # 옮겨야하는 원소 찾기
    # N이 배열의 크기
    # 맨 아래 원소를 옮길 공간이 없기 때문에 확인하지 않음
    for i in range(N-2, -1, -1):
        for j in range(N):
            # 움직일 수 없는 블록도 아니고
            # 빈칸도 아닐 때
            # 일반블록 or 무지개 블록
            if arr[i][j] > -1:
                # 변수에 탐색할 행 저장
                i2 = i
                #아래로 한 칸씩 움직이면서 끝까지 이동시키기
                while True:
                    if 0 <= i2+1 < N and arr[i2+1][j] == -2:
                        arr[i2][j], arr[i2+1][j] = arr[i2+1][j], arr[i2][j]
                        i2 += 1
                    else:
                        break
            
# 반시계방향
def rotate(arr):
    new_arr = []
    
    #리스트, 튜플 해제해서 새로 묶음 zip(*arr)
    for z in zip(*arr):
        new_arr.append(list(z))
    new_arr.reverse()
    return new_arr


N, M = map(int, input().split())

block_map = []
for _ in range(N):
    block_map.append( list( map(int, input().split()) ) )


score = 0

while True:
    visited = [ [0]*N for _ in range(N) ]
    groups = []
    
    #print('block_map\n',block_map)
    for i in range(N):
        for j in range(N):
            # 방문 안해본 일반 블록
            if block_map[i][j] > 0 and visited[i][j] != 1:
                visited[i][j] = 1
                group_info = bfs(i, j, block_map[i][j])
                if group_info[0] >= 2:
                    groups.append(group_info)
    
    #print('1 groups: ', groups)
    groups.sort(reverse=True)
    #print('2 groups: ', groups)
    
    if not groups:
        break
    
    score += groups[0][0]**2
    
    for pos in groups[0][2]:
        block_map[pos[0]][pos[1]] = -2
        
    gravity(block_map)
    
    block_map = rotate(block_map)
    
    gravity(block_map)

print(score)
