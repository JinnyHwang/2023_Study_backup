
from copy import deepcopy
from collections import deque

d = [(-1,0),(1,0),(0,-1),(0,1)]

N, M = map(int, input().split())

block_map = []

for _ in range(N):
    block_map.append( list( map(int, input().split()) ) )
    
def search_group(block_map, visited, x, y):
    
    group_visited = deepcopy(visited)
    block_num = block_map[x][y]
    rainbow_block = 0
    all_block = 0
    block_pos = []
    point = [x,y]
        
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    group_visited[x][y] = 1
    
    while q:
        pos = q.popleft()
        block_pos.append([pos[0], pos[1]])
        all_block += 1
        
        for di in d:
            nx = pos[0] + di[0]
            ny = pos[1] + di[1]
            if 0 <= nx < N and 0 <= ny < N:
                if group_visited[nx][ny] != 1:
                    if block_map[nx][ny] == block_num:
                        point = min(point, [nx,ny])
                        visited[nx][ny] = 1
                        group_visited[nx][ny] = 1
                        q.append([nx,ny])
                    elif block_map[nx][ny] == 0:
                        rainbow_block += 1
                        group_visited[nx][ny] = 1
                        q.append([nx,ny])
                        
    
    # [전체블록개수, 무지개블록개수, (기준좌표), blocks]
    result = [ 0 for _ in range(4)]
    result[0] = all_block
    result[1] = rainbow_block
    result[2] = point
    result[3] = block_pos
    
    return result


def big_group(block_map):
    
    # group_list[n] = [전체블록개수, 무지개블록개수, (기준좌표), blocks]
    group_list = []
    del_group = [ 0 for _ in range(2)]
    visited = [ [0]*N for _ in range(N) ]
    
    for r in range(N):
        for c in range(N):
            # 일반블록인 경우 탐색 시작
            if block_map[r][c] > 0:
                if visited[r][c] != 1:
                    #print('어디? ',r,c,' 값은? ', block_map[r][c])
                    group_info = search_group(block_map, visited, r, c)
                    #print('[big_group] group_info: ',group_info)
                    # 일반 블록 개수가 2개 이상인 경우
                    # 그룹에는 일반 블록이 적어도 하나 있어야 하며: 일반블록 1개 포함
                    # 룹에 속한 블록의 개수는 2보다 크거나 같아야 하며: 2개 이상
                    if group_info[0] >= 2 :
                        group_list.append(group_info)
                        
    if group_list:
        
        # 아.. 지문을 잘못 이해했네....
        # 기준 블록을 정하는 기준
        # 기준 블록 중 행열이 큰게 고르는 기준
        #group_list.sort( key = lambda x : (-x[0], -x[1], x[2][0])   )
        group_list.sort(reverse=True)
        #print('[big_group] group_list sort: ',group_list)
        
        del_group[0] = group_list[0][0]
        del_group[1] = group_list[0][3]
        #print('del_group: ',del_group)
        return del_group
    else:
        return []
    
    

def gravity(block_map):
    
    # 배열 아래서부터 확인
    # N-2~0
    # 맨 아래칸은 탐색하지 않음
    for i in range(N-2, -1, -1):
        # 0~N-1
        for j in range(N):
            # 옮길 수 있는 블록 확인.
            # 옮길 수 없는 블록, 빈칸 쓰루
            if block_map[i][j] > -1:
                # r: 옮길 블록의 행번호
                r = i
                # 블록의 아래 좌표를 한 칸씩 탐색
                while True:
                    # 옮기려는 좌표가 배열 범위인지, 빈칸인지 확인
                    if 0 <= r+1 < N and block_map[r+1][j] == -2:
                        # 한 칸씩 이동
                        block_map[r][j], block_map[r+1][j] = block_map[r+1][j], block_map[r][j]
                        r += 1
                    # 배열 범위를 넘거나, 빈칸이 아니면(-1블록도 자연스럽게 쓰루) 옮기기 종료
                    else:
                        break


def rotate(block_map):
    
    new_block_map = []
    
    for z in zip(*block_map):
        new_block_map.append(list(z))
        
    new_block_map.reverse()
    
    return new_block_map   


score = 0
game_play = True
while(game_play):
    
    #print('1 block_map: ',block_map,'\n')
    
    del_group = big_group(block_map)
    
    #print('2 del_group: ',del_group, '\n')
    
    # 삭제할 수 있는 그룹이 없음
    if not del_group:
        game_play = False
        break
    
    score += del_group[0]**2
    
    #print('3 score: ',score, '\n')
    
    # 블록 삭제
    for pos in del_group[1]:
            block_map[pos[0]][pos[1]] = -2
            
    #print('4 블록 삭제: ',block_map, '\n')
            
    # 블록 아래로 땡기기
    gravity(block_map)
    #print('5 중력1: ',block_map, '\n')
    
    # 반시계 90도 회전
    block_map = rotate(block_map)
    #print('6 회전: ',block_map, '\n')
    
    # 블록 아래로 땡기기
    gravity(block_map)
    #print('7 중력2: ',block_map, '\n')

print(score)


        


def rotate_1(block_map):
    
    new_block_map = [ [0]*N for _ in range(N) ]
    
    for r in range(N):
        for c in range(N):
            nr = (N-1)-c
            nc = r
            new_block_map[nr][nc] = block_map[r][c]
    
    return new_block_map



# 더 쉬운 방법 찾아서 이건 사용 안함
