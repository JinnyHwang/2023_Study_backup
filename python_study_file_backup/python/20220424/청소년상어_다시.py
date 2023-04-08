
from copy import deepcopy

# 백트레킹?
# 상어가 먹을 수 있는 물고기 번호 합의 최댓값
# 끝까지 진행해서 그 결과값을 봐야함

d = [ (-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1) ]
# 45도 반시계는 방향값+1

def shark_move(arr, x, y):
    positions = []
    sd = arr[x][y][1]-1
    for i in range(1, 4):
        nx = x + d[sd][0]*i
        ny = y + d[sd][1]*i
        if 0 <= nx < 4 and 0 <= ny < 4 and arr[nx][ny] != 0:
            positions.append( [nx,ny] )
    return positions


def find_fish(arr, num):
    #print(arr)
    for i in range(4):
        for j in range(4):
            if arr[i][j][0] == num:
                #print(num, arr[i][j][0], i, j)
                return [i, j]
    return None



def fish_move(arr, x, y):
    
    flag = False
    position = []
    
    for num in range(1, 17):
        # 지금 탐색하는 i번 물고기 어디있는지 확인
        position = find_fish(arr, num)
        #print(num, position)
        if position is None:
            continue
        
        i = position[0]
        j = position[1]
        
        nd = arr[i][j][1]-1
        
        for _ in range(8):
            ni = i + d[nd][0]
            nj = j + d[nd][1]
            
            if 0 <= ni < 4 and 0 <= nj < 4:
                if arr[ni][nj][0] != -1:
                    arr[i][j][1] = nd+1
                    arr[i][j], arr[ni][nj] = arr[ni][nj], arr[i][j]
                    break
                
            nd = (nd+1)%8 
        
    
    


def dfs(fish_map, x, y, total):
    global answer
    
    array = deepcopy(fish_map)
    
    # 상어 지금 위치 물고기 먹기, 상어 위치시키기
    number = array[x][y][0]
    array[x][y][0] = -1
    
    # 물고기 이동
    fish_move(array, x, y)
    #print(array)
    
    # 상어 이동할 수 있는 후보 확인
    positions = sh/ark_move(array, x, y)
    
    # 모든 상어 position 탐색
    answer = max(answer, total+number)
    for px, py in positions:
        #print(array, px, py, total+number)
        dfs(array, px, py, total+number)


# 4X4
#fish_map = [ list(map(int, input().split())) for _ in range(4) ]

fish_map = [ [[0,0]]*4 for _ in range(4) ]
#print(fish_map)

l = []

for i in range(4):
    l = list(map(int, input().split()))
    for j in range(0, 8, 2):
        fish_map[i][j//2] = [ l[j], l[j+1] ]
#print(fish_map)

#shark_pos = [0,0]
#fish_map[0][0][0] = -1
#print(fish_map)

# dfs 탐색
answer = 0
dfs(fish_map, 0, 0, 0)
print(answer)


























