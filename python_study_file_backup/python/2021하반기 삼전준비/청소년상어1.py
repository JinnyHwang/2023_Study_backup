
# 물고기 이동
# 상어는 bfs로 정보 저장

# arr : 지도 정보
# fish :물고기 순서대로 좌표정보
# 상어의 좌표, 먹은 물고기 크기 d, cnt
# (0,0) 물고기 정보 지운 후 dfs 실행
# 상어가 (0,0) 물고기를 이미 먹은 상태.
# 우선 move_fish 상태 실행해서 물고기 이동

# fish 리스트의 인덱스는 (물고기크기 -1)
# fish 순서대로 불러와서 처리
# 물고기가 이동할 수 없으면 방향 갱신, continue
# 다음칸이 빈칸이 아닌경우엔 다음칸에 있는 물고기의 좌표를 바꿔줌
# 지도에서 물고기 정보를 서로 바꿔주고 이동한 물고기의 좌표를 바꿔줌

# 물고기 이동이 끝나면 상어가 이동
# 상어는 먹은 물고기의 방향성을 가짐
# 만약 다음칸이 범위를 벗어나면, 최댓값을 갱신한 뒤 return
# 다음칸이 빈칸이면 continue

# 재귀를 하기 전 arr, fish, 상어가 먹게될 물고기 정보를 temp에 저장
# 상어의 다음 좌표, 먹은 물고기의 방향, 지금까지 먹은 물고기 크기+먹은물고기크기+1(index값) 입력 후 재귀
# temp의 값을 불러와 변수 다시 리셋
# 모든 탐색을 진행한다

from copy import deepcopy
# 문제에 주어진 방향 index에 맞춰 작성
dx = [-1, -1, 0, 1, 1, 1, 0, -1] 
dy = [0, -1, -1, -1, 0, 1, 1, 1]
result = 0
i = 1

def move_fish(sx, sy):
    # 앞순서 물고기부터 move
    for i in range(16):
        # fish 값이 있을때만
        if fish[i]:
            x, y = fish[i][0], fish[i][1]
            # 모든 방향 확인
            for _ in range(9):
                nx, ny = x + dx[arr[x][y][1]], y + dy[arr[x][y][1]]
                # 좌표가 범위를 벗어나거나, 다시 원점으로 돌아왔을 때
                if not 0<=nx<4 or not 0<=ny<4 or (nx==sx and ny==sy):
                    arr[x][y][1] = (arr[x][y][1]+1)%8
                    continue
                if arr[nx][ny]:
                    fish[ arr[nx][ny][0] ] = [x,y]
                    arr[nx][ny], arr[x][y] = arr[x][y], arr[nx][ny]
                    fish[i] = [nx, ny]
                    break

# 상어가 방문할 수 있는 모든 경로 탐색
# 특정 방향으로 갈 수 있는 만큼 가고
# 그때 잡아먹는 물고기 값
# result가 가장 클 때를 return
def dfs(x, y, d, fcnt):
    # 전역변수 사용
    global result, arr, fish, i
    #print("1 : arr:{} \nfish:{}".format(arr, fish))
    move_fish(x, y)
    print("2 : arr:{} \nfish:{} \nfcnt:{}\n".format(arr, fish, fcnt))
    while True:
        nx, ny = x+dx[d], y+dy[d]
        print("d:{}, nx:{}, ny:{}".format(d, nx, ny))
        if not 0<=nx<4 or not 0<=ny<4 :
            print("result:{}, fcnt:{}".format(result, fcnt))
            result = max(result, fcnt)
            #print("end : arr:{} \nfish:{}\nresult:{} {}\n".format(arr, fish, result, id(result)))
            return
        if not arr[nx][ny]: #빈칸
            x, y = nx, ny
            continue
        
        # deepcopy 기능하네!!!!
        temp_arr, temp_fish = deepcopy(arr), deepcopy(fish)
        #print(id(temp_arr), id(temp_fish), id(arr), id(fish))
        #print(temp_arr[0], arr[0])
        #temp_arr[0] = [999]
        #print(temp_arr[0], arr[0])
        temp1, temp2 = fish[arr[nx][ny][0]], arr[nx][ny]
        fish[arr[nx][ny][0]], arr[nx][ny] = [], []
        
        # 상어를 옯기면 map이 또 바뀌기 때문에
        # 옮기는 동작 전에 상태값 저장 필
        # 현재 방향에서 탐색할 수 있는 모든 경로 탐색
        print("1_{} : arr:{} \nfish:{}\n".format(i, arr, fish))
        dfs(nx, ny, temp2[1], fcnt+temp2[0]+1)
        print("2_{} : arr:{} \nfish:{}\n".format(i, arr, fish))
        i += 1
        
        arr, fish = temp_arr, temp_fish
        fish[arr[nx][ny][0]], arr[nx][ny] = temp1, temp2
        x, y = nx, ny



# 4*4 지도 각 좌표에는 물고기번호와 방향정보가 들어감
arr = [ [] for _ in range(4) ]

# 각 번호 물고기가 갖는 좌표
fish = [ [] for _ in range(16) ]

for i in range(4):
    in1 = list(map(int, input().split()))
    for j in range(0, 7, 2):
        # 물고기 numbering 크기-1, 방향 0부터 시작 -1
        arr[i].append([in1[j]-1, in1[j+1]-1])
        fish[in1[j]-1] = [i, j//2]
        
print("First \n arr:{} \nfish:{}".format(arr, fish))



fish_size, d = arr[0][0][0]+1, arr[0][0][1]
# 먹은 물고기 좌표정보, 지도정보 clear
fish[arr[0][0][0]], arr[0][0] = [], []

dfs(0, 0, d, fish_size)
print(result, id(result))








