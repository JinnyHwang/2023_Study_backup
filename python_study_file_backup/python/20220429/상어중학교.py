
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

#print(N, M, '\n', block_map, '\n')

# 빈블록 표현
# block_map[r][c] = -2

    
# 그룹 정보: 전체 블록 개수, 무지개 블록 개수, 일반블록좌표(sort()로 기준 찾음)
group_blockpos = []

# group_count[0]: 전체개수
# group_count[1]: 무지개블록 개수
group_count = [0,0]


def search_group(block_map, visited, x, y):
    
    group_visited = deepcopy(visited)
    block_num = block_map[x][y]
    rainbow_block = 0
    block_pos = []
    point = [x,y]
        
    all_block = 0
    q = deque()
    q.append([x,y])
    visited[x][y] = 1
    group_visited[x][y] = 1
    #print('q: ', q)
    
    while q:
        pos = q.popleft()
        #visited[pos[0]][pos[1]] = 1
        #group_visited[pos[0]][pos[1]] = 1
        block_pos.append([pos[0], pos[1]])
        all_block += 1
        #print('q: {} x,y:{}'.format(q, pos))
        
        for di in d:
            nx = pos[0] + di[0]
            ny = pos[1] + di[1]
            #print('pos[0], di[0]: ',pos[0], di[0], '  nx? ',nx)
            #print('pos[1], di[1]: ',pos[1], di[1], '  ny? ',ny)
            if 0 <= nx < N and 0 <= ny < N:
                if group_visited[nx][ny] != 1:
                    if block_map[nx][ny] == block_num:
                        #print('1 in??')
                        #all_block += 1
                        #block_pos.append([nx,ny])
                        point = min(point, [nx,ny])
                        visited[nx][ny] = 1
                        group_visited[nx][ny] = 1
                        q.append([nx,ny])
                    elif block_map[nx][ny] == 0:
                        #print('2 in??')
                        #all_block += 1
                        rainbow_block += 1
                        #block_pos.append([nx,ny])
                        #visited[nx][ny] = 1
                        group_visited[nx][ny] = 1
                        q.append([nx,ny])
                    #else:
                        #print('3 in??')
                        #visited[nx][ny] = 1
                        
    
    # [전체블록개수, 무지개블록개수, (기준좌표), blocks]
    result = [ 0 for _ in range(4)]
    result[0] = all_block
    result[1] = rainbow_block
    result[2] = point
    # 결과 확인용
    block_pos.sort()
    result[3] = block_pos
    
    #print('[search_group] result: ',result)
    
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
                    
    #print('[big_group] group_list: ',group_list)
    
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
        

# 더 쉬운 방법 찾아서 이건 사용 안함
def rotate_1(block_map):
    
    new_block_map = [ [0]*N for _ in range(N) ]
    
    for r in range(N):
        for c in range(N):
            nr = (N-1)-c
            nc = r
            new_block_map[nr][nc] = block_map[r][c]
    
    return new_block_map



score = 0
while True:
    
    #print('1 block_map: ',block_map,'\n')
    
    del_group = big_group(block_map)
    
    #print('2 del_group: ',del_group, '\n')
    
    # 삭제할 수 있는 그룹이 없음
    if not del_group:
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





def gravity_1(block_map):
    
    print('[gravity] block_map: ',block_map)
    temp = []
    last_pos = -1
    for c in range(N):
        # 작은 행 -> 마지막 행 까지 탐색
        for r in range(N):
            print('[gravity] start r, c: ', r, c)
            
            if block_map[r][c] == -1:
                if temp:
                #지금까지 저장한 원소 좌표 옮기기
                    for r2 in range(r-1, -1, -1):
                        #print('# ',r2)
                        if not temp:
                            #print('!! ',temp)
                            break
                        else:
                            #print('!temp: ',temp)
                            #print('? ',temp.pop())
                            block_map[r2][c] = temp.pop()
                            #print('r2, c',r2, c, ' block_map',  block_map[r2][c])
                    print('[gravity] !!! block_map: {}   temp: {}'.format(block_map, temp))
                continue
            
            elif block_map[r][c] == -2:
                #가장 마지막에 비어있는 좌표 기억
                last_pos = r
            else:
                print('[gravity] block_map[r][c]: ', block_map[r][c])
                temp.append(block_map[r][c])
                block_map[r][c] = -2
                print('[gravity] append temp: ',temp)
                
                
            if r == N-1:
                # 저장된 블록이 있는 경우
                # 빈칸이 있는 경우
                if last_pos != -1 and temp:
                    print('[gravity] r == N-1:', r, '  temp: ', temp)
                    #지금까지 저장한 원소 좌표 옮기기
                    for r2 in range(last_pos, -1, -1):
                        if not temp:
                            break
                        else:
                            block_map[r2][c] = temp.pop()
                    print('[gravity] ??? block_map: {}   temp: {}'.format(block_map, temp))
   
   
def gravity_2(block_map):
    
    # 1. 빈공간 확인
    # 2. 옮길 블록 확인
    # 옮기는 시점: -1 블록을 만났을 때, 배열의 끝에 도달했을때
    # 블록이 빈공간 없이 꽉 차이있으면 옮길 필요 없음!
    
    empty_pos = []
    temp = []
    
    # 열 고정, 행 이동
    for r in range(N):
        for c in range(N):
            
            # 빈칸 좌표 다 저장
            if block_map[r][c] == -2:
                empty_pos.append(r)
            
            # 옮기는 시점
            elif block_map[r][c] == -1:
                # 탐색 시작 지점 ~ -1 블록까지 빈칸이 존재
                if temp:
                    # 맨 마지막에 저장된 원소부터 확인하기 위함
                    temp.reverse()
                    for t in temp:
                        # 빈 칸이 없으면 바로 out: 옮길게 없음
                        if not empty_pos:
                            break
                        # 맨 마지막 좌표 값
                        empty_pos.sort(reverse=True)
                        # 저장된 값도 있고, 빈칸도 있는 경우
                        if t[0] < empty_pos:
                            # 빈칸에 값 저장
                            block_map[empty_pos][c] = t[1]
                            
                            
                    
                # 빈칸 없으면 temp 비우고 탐색 넘어감
                else:
                    temp = []
                    continue
                    
            else:
                #저장
                temp.append([r, block_map[r][c]])
                
        if empty_pos != -1 and temp:
            return
            #옮기기



    