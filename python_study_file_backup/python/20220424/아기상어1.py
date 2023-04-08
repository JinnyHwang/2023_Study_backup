
# N*N 공간
# M마리 물고기

# 상어 초기값 2
# 물고기크기 < 상어 먹을 수 있음, 지나갈 수 있음
# 물고기크기 == 상어 먹을 수 없음, 지나갈 수 있음
# 물고기크기 > 상어 먹을 수 없음, 지나갈 수 없음

# 먹을 수 있는 물고기가 1개 이상 : 가장 가까운 물고기
# 지나야하는 칸의 개수 최솟값
# 만약 가까운 물고기가 여러개면, 가장 왼쪽에 있는 물고기를 먹는다

# 자신의 크기과 같은 크기 물고기를 크기값 만큼 먹으면 크기 1 증가
# (상어크기, 먹은 물고기 수)

# 끝나는 조건
# 더이상 먹을 수 있는 물고기가 없음
# -> 몇 초 동안 물고기 먹으면서 다닐 수 있는가?
# 즉 이동 칸 개수



# 변하지 않는 값 튜플
# 상하좌우
# d[0], d[1], d[2], d[3]
# d[a][0] : y / d[a][1] : x
d = [ (1, 0), (-1, 0), (0, -1), (0, 1) ]

N = int(input())
fish = [ [0]*N for _ in range(N) ]

# shark_pos : 위치좌표 y,x
# shark_info : 상어크기, 먹은물고기
shark_pos = [0, 0]
shark_info = [2, 0]

#print(N, fish, shark)

def check_fish(fish, shark_size):
    
    for y in range(N):
        for x in range(N):
            if fish[y][x] < shark_size:
                return 1
    else:
        return 0
    



def eat_fish(fish, shark_pos, shark_info):
    
    result = 0
    
    while True:
        # 물고기 찾는 최대 시간으로 초기화
        time = N*N
        # 가상의 좌표로 초기화
        shark_pos_min = [-1,-1]
        
        # 가장 가까운 물고기까지 걸리는 시간, 물고기 좌표를
        # time, shark_pos_min에 저장
        find_fish(fish, shark_pos[0], shark_pos[1], shark_pos, shark_info[0])
        print(time, shark_pos_min)
        
        # 먹을 수 있는 물고기 있음!
        if shark_pos_min[0] != -1:
            result += shark_pos_min
            shark_pos = shark_pos_min
            shark_info[1] += 1
            fish[shark_pos[0]][shark_pos[1]] = 0
            # 상어 크기 늘려주기
            if shark_info[0] == shark_info[1]:
                shark_info = [ shark_info[0]+1, 0]
        #물고기없는디
        else:
            break
    
    return result






# 현 위치에서부터 상하좌우로 만날 수 있는 물고기를 찾음
# 가장 빨리 찾는 
def find_fish(fish, fish_visited, y, x, shark_pos, shark_size):
    
    global time, shark_pos_min
    
    # 끝까지 탐색했지만 먹을 수 있는 물고기가 없음 -> 1턴 끝
    if y < 0 or y >= N or x < 0 or x >= N:
        return
    
    if fish_visited[y][x] == 1:
        return
    
    #print('!!',y, x, fish[y][x], shark_size, fish_visited)
    # 0이거나 같은 크기 지나감
    if fish[y][x] == 0 or fish[y][x] == shark_size:
        fish_visited[y][x] = 1
        # 다음을 찾음
        for n in range(4):
            find_fish(fish, fish_visited, y+d[n][0], x+d[n][1], shark_pos, shark_size)
    # 물고기 먹음 -> 1턴 끝
    elif fish[y][x] < shark_size:
        fish_visited[y][x] = 1
        tack_time = abs(shark_pos[0]-y)+abs(shark_pos[1]-x)
        # 더 왼쪽에 있는거 먹음
        if tack_time == time:
            if (y < shark_pos_min[0]) or (y == shark_pos_min[0] and x < shark_pos_min[1]) :
                shark_pos_min = [y,x]
                time = tack_time
        elif tack_time < time:
            shark_pos_min = [y,x]
            time = tack_time
        return
    # 큰 물고기여서 못 지나감
    else:
        fish_visited[y][x] = 1
        return




for y in range(N):
    fish[y] = list(map(int, input().split()))
    for x in range(N):
        if fish[y][x] == 9:
            shark_pos = [y, x]
            fish[y][x] = 0
            
#print(fish, shark_pos)

result = 0
    
while True:
    # 물고기 찾는 최대 시간으로 초기화
    time = N*N
    # 가상의 좌표로 초기화
    shark_pos_min = [-1,-1]
    
    # 방문했는지 확인
    fish_visited = [ [0]*N for _ in range(N) ]
    
    #print('먹기 전: ', shark_pos, shark_info)
    #print(fish)
    
    # 먹을 수 있는 물고기 확인
    # 상어 사이즈보다 작은 물고기가 있는지 확인
    if check_fish(fish, shark_info[0]) == 0:
        break
        
    # 가장 가까운 물고기까지 걸리는 시간, 물고기 좌표를
    # time, shark_pos_min에 저장
    find_fish(fish, fish_visited, shark_pos[0], shark_pos[1], shark_pos, shark_info[0])
    
        
    # 먹을 수 있는 물고기 있음!
    if shark_pos_min[0] != -1:
        result += time
        shark_pos = shark_pos_min
        shark_info[1] += 1
        fish[shark_pos[0]][shark_pos[1]] = 0
        
        #print('먹음: ',time, result, shark_pos_min, shark_info)
        
        # 상어 크기 늘려주기
        if shark_info[0] == shark_info[1]:
            shark_info = [ shark_info[0]+1, 0]
        
    #물고기없는디
    else:
        #print('못먹음: ',time, result, shark_pos_min, shark_info)
        break

print(result)
        
# 가장 가까운 거리에 있는 물고기 찾기
# 물고기 먹고 난 후 남은 물고기
# 상어의 위치와 크기, 먹은 같은 크기 물고기수
#print(eat_fish(fish, shark_pos, shark_info))

## 예외상황 확인해보



