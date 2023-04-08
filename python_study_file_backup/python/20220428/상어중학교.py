
'''
N*N 격자
블록정보 입력

블록
검정: -1 : 그룹에 포함될 수 없음, 중력 적용 안됨
무지개: 0 : 어디든 포함될 수 있음
일반블록: 1~M 값을 가지고 있음

인접 기준: 상하좌우

그룹 조건
1. 일반 블록이 하나 이상 포함되어야 함
2. 한 그룹에 일반 블록 색은 모두 같아야 한다
3. 검은블록은 포함될 수 없음
4. 무지개블록은 개수 상관 없이 포함될 수 있음
5. 한 그룹은 2개 이상 블록을 가져야함 (블록개수 < 2 면 brek)
6. 그룹의 기준 번호는 일반블록 중 행, 열이 가장 작은 블록.


[1] 그룹 탐색
1. 포함된 블록 개수가 가장 큰 그룹 탐색
2. 무지개 블록 개수가 가장 많은 그룹
3. 기준블록 좌표가 가장 작은 것
=> 그룹 정보: 전체 블록 개수, 무지개 블록 개수, 일반블록좌표(sort()로 기준 찾음)


[2] 해당 그룹 블록 삭제
점수는 (그룹 내 블록 개수)^2
=> 누적함 


[3] 격자에 중력 작용
=> 이거 외워가자


[4] 격자 90도 반시계방향으로 회전
=> 구상해보자
==> 다른 방향으로 돌리기도 생각하기

[5] 다시 중력 작용


--> 획득한 점수 합 구하기
'''

from copy import deepcopy
from collections import deque


# 인접블록 상하좌우
d = [(-1,0),(1,0),(0,-1),(0,1)]


N, M = map(int, input().split())

block_map = []

for _ in range(N):
    block_map.append( list( map(int, input().split()) ) )

print(N, M, '\n', block_map, '\n')

# 빈블록 표현
# block_map[r][c] = -2

    
# 그룹 정보: 전체 블록 개수, 무지개 블록 개수, 일반블록좌표(sort()로 기준 찾음)
group_blockpos = []

# group_count[0]: 전체개수
# group_count[1]: 무지개블록 개수
group_count = [0,0]


def search_group(block_map, x, y):
    
    q = deque()
    q.append([x,y])
    block_num = block_map[x][y]
    
    blocknum = 0
    rainbow_block = 0
    block_pos = []
    point = [N,N]
    
    visited = [ [0]*N for _ in range(N) ]
    
    #print('q: ', q)
    
    while q:
        pos = q.popleft()
        visited[pos[0]][pos[1]] = 1
        
        for di in d:
            nx = pos[0] + di[0]
            ny = pos[1] + di[1]
            #print('pos[0], di[0]: ',pos[0], di[0], '  nx? ',nx)
            #print('pos[1], di[1]: ',pos[1], di[1], '  ny? ',ny)
            if 0 <= nx < N and 0 <= ny < N:
                if visited[nx][ny] != 1:
                    if block_map[nx][ny] == block_num:
                        #print('1 in??')
                        blocknum += 1
                        block_pos.append([nx,ny])
                        point = min(point, [nx,ny])
                        q.append([nx,ny])
                    elif block_map[nx][ny] == 0:
                        #print('2 in??')
                        blocknum += 1
                        rainbow_block += 1
                        block_pos.append([nx,ny])
                        q.append([nx,ny])
                    #else:
                        #print('3 in??')
    
    # [전체블록개수, 무지개블록개수, (기준좌표), blocks]
    result = [ 0 for _ in range(4)]
    result[0] = blocknum
    result[1] = rainbow_block
    result[2] = point
    result[3] = block_pos
    
    #print('result: ',result)
    
    return result


def big_group(block_map):
    
    # group_list[n] = [전체블록개수, 무지개블록개수, (기준좌표), blocks]
    group_list = []
    del_group = []
    
    for r in range(N):
        for c in range(N):
            # 일반블록인 경우 탐색 시작
            #print('어디? ',r,c,' 값은? ', block_map[r][c])
            if block_map[r][c] != -1 and block_map[r][c] != 0:
                group_info = search_group(block_map, r, c)
                # 일반 블록 개수가 2개 이상인 경우 
                if (group_info[0]-group_info[1]) > 2:
                    group_list.append(group_info)
                    
    #print('group_list: ',group_list)
    
    if group_list:
        group_list.sort()
        del_group.append(group_list[0][0])
        del_group.append(group_list[0][3])
        return del_group
    else:
        return []
    
    
    
def gravity(block_map):
    
    for c in range(N):
        temp = []
        # 작은 행 -> 마지막 행 까지 탐색
        for r in range(N):
            if r == N-1:
                # 저장된 블록이 있는 경우
                if temp:
                    #지금까지 저장한 원소 좌표 옮기기
                    for r2 in range(r, -1, -1):
                        block_map[r2][c] = temp.pop()
            
            if block_map[r][c] == -1:
                if temp:
                #지금까지 저장한 원소 좌표 옮기기
                    for r2 in range(r, -1, -1):
                        if not temp:
                            break
                        else:
                            block_map[r2][c] = temp.pop()
                continue
            
            elif block_map[r][c] != -2:
                temp.append(block_map[r][c])
            
            else:
                continue
           
    
    
def rotate(block_map):
    
    new_block_map = deepcopy(block_map)
    
    for r in range(N):
        for c in range(N):
            nr = (N-1)-c
            nc = r
            new_block_map[nr][nc] = block_map[r][c]
    
    return new_block_map
    
  

score = 0
game_play = True
while(game_play):
    
    del_group = big_group(block_map)
    #print('del_group: ',del_group)
    
    # 삭제할 수 있는 그룹이 없음
    if not del_group:
        game_play = Flase
        break
    
    score += del_group[0]**2
    
    # 블록 삭제
    for pos in del_group[1]:
            block_map[pos[0]][pos[1]] = -2
            
    # 블록 아래로 땡기기
    gravity(block_map)
    
    # 반시계 90도 회전
    rotate(block_map)
    
    # 블록 아래로 땡기기
    gravity(block_map)



print(score)


