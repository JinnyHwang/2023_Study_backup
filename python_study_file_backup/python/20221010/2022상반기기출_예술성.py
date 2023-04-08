
'''
https://www.codetree.ai/frequent-problems/artistry/description

예술성

1. 그룹 나누기 bfs
그룹을 이루고 있는 숫자 정보
그룹 크기
그룹의 맨 끝좌표 (맞닿아있는 변의 수를 구하기 위함)

2. 그룹으로 만들 수 있는 모든 조합 확인
한 조합에 대해 조화로움 계산
값을 모두 더하기
-> 더해진 값이 해당 turn의 예술성

3. 예술성 계산 후 회전 진행
3-1. 정중앙의 십자가 반시계로 90도 회전
3-2. 십자가를 제외한 나머지 사각현 영역 시계방향으로 90도 회전

3번 진행 후 모든 예술정의 합을 구하시오
'''
def show(l):
    for l1 in l:
        print(l1)
    print('\n')



from collections import deque
import copy

N = int(input())
pic_map = [ list(map(int, input().split())) for _ in range(N) ]

# 상 하 좌 우
d = [(-1,0),(1,0),(0,-1),(0,1)]

def cal_side(pic_pos1, pic_pos2, pic2_num):
    
    answer = 0
    for pic1 in pic_pos1:
        for di in d:
            ny = pic1[0] + di[0]
            nx = pic1[1] + di[1]
            # 인접 블록인데 pic2 블록과 값이 같은 경우만 확인
            if (ny>=0 and ny<N and nx>=0 and nx<N) and (pic_map[ny][nx] == pic2_num):
                # pic_pos2 그룹 안에 해당 좌표가 있으면 변의 개수 추가
                if [ny, nx] in pic_pos2:
                    answer += 1
    return answer

def find_pic_group(y, x, pic_group, pic_group_pos, visited):
    
    group_size = 0
    
    pic_q = deque()
    pic_q.append([y,x])
    
    while pic_q:
        
        q_data = pic_q.pop()
        if group_size != 0:
            pic_group_pos.append([q_data[0], q_data[1]])
        group_size += 1
        
        for di in d:
            ny = q_data[0] + di[0]
            nx = q_data[1] + di[1]
            if (ny>=0 and ny<N and nx>=0 and nx<N) and visited[ny][nx] == 0:
                if pic_map[ny][nx] == pic_group[0]:
                    pic_q.append([ny,nx])
                    visited[ny][nx] = 1
    
    pic_group[1] = group_size
    return


# 반시계 회전
def turn_cross(pic_map, pic_map_copy):
    
    # pic_map_copy로 값 확인하고
    # pic_map 값 초기화하기
    
    # 십자의 좌표는?
    for y in range(N):
        for x in range(N):
            if y == (N//2) or x == (N//2):
                pic_map[(N-1)-x][y] = pic_map_copy[y][x]
                
    
range_set = [(0, 0),(0, N//2+1),(N//2+1, 0),(N//2+1, N//2+1)]
square_len = N//2
# N//2 square의 한 변의 길이

# 시계 회전
def turn_square(pic_map, pic_map_copy):
    
    for i in range(4):
        sy = range_set[i][0]
        sx = range_set[i][1]
        for y in range(0,square_len):
            for x in range(0,square_len):
                pic_map[x+sy][(square_len-1)-y+sx] = pic_map_copy[y+sy][x+sx]
        
            

art_sum = 0
art_turn = 0
while True:
    
    # 매 turn 마다 초기화
    visited = [ [0 for _ in range(N)] for _ in range(N) ]
    
    # pic list의 index는 그룹 정보 추가 순서
    # pic_group[index][0]: 그룹을 이루고 있는 숫자 값  /  pic_group[index][1]: 그룹에 속한 칸 개수
    pic_group = []
    # pic_group_pos[index]: 그룹을 이루는 좌표 값
    pic_group_pos = []
    
    # 각 그룹 탐색하기
    for y in range(N):
        for x in range(N):
            # 방문한 적 없는 좌표인 경우에만 처음부터 탐색
            if visited[y][x] == 0:
                visited[y][x] = 1
                pic_group.append([pic_map[y][x], 1])
                pic_group_pos.append([[y,x]])
                find_pic_group(y, x, pic_group[-1], pic_group_pos[-1], visited)
    
    #print('pic_group ',pic_group)
    #print('pic_group_pos')
    #show(pic_group_pos)
    
    
    # 그룹 정보를 보고 combinate 하기
    com_sum = 0
    side_count = 0
    for pi1, p1 in enumerate(pic_group[:-1]):
        for pi2, p2 in enumerate(pic_group[pi1+1:], start=pi1+1):
            # 맞닿아 있는 변의 수 구하기
            side_count = cal_side(pic_group_pos[pi1],pic_group_pos[pi2], p2[0])
            # 맞닿아있는 경우만 구하기
            if side_count != 0:
                com_sum = (p1[1] + p2[1]) * p1[0] * p2[0] * side_count
                art_sum += com_sum
                #print('\nok near side group{}번 {} / group{}번 {}'.format(pi1,p1[0],pi2,p2[0]))
                #print('p1[1]:{}, p2[1]:{}, p1[0]:{}, p2[0]:{}, side_count:{}, com_sum:{})'.format(p1[1], p2[1], p1[0], p2[0], side_count, com_sum))
            #else:
                #print('\nno near side group{}번 {} / group{}번 {}'.format(pi1,p1[0],pi2,p2[0]))
            
    
    # 3회전 진행완료했으면 turn 종료
    if art_turn == 3:
        break


    # 회전 진행
    pic_map_copy = copy.deepcopy(pic_map)
    # 십자 회전
    turn_cross(pic_map, pic_map_copy)
    #print('\n turn_cross')
    #show(pic_map)
    
    # 사각 회전
    turn_square(pic_map, pic_map_copy)
    #print('\n turn_square')
    #show(pic_map)
    
    # 회전 진행함 표시
    art_turn += 1


print(art_sum)

