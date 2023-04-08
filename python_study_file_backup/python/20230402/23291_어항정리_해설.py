
# https://velog.io/@heyksw/Python-%EB%B0%B1%EC%A4%80-platinum-23291-%EC%96%B4%ED%95%AD-%EC%A0%95%EB%A6%AC

from collections import deque
import sys

def map_print(m):
    for i in range(len(m)-1, -1, -1):
        print(m[i])
        
    print()

# 그래프 변형이 자주 일어남
# deque를 사용해서 해결

# 배열 여러개 생성하지 말고 deque 사용
N, K = map(int, sys.stdin.readline().split())
d = [(0,1),(0,-1),(-1,0),(1,0)]
bowl = list()
# deque를 원소로 갖는 리스트 쌓기. 원소 popleft() 시 부하를 줄이기 위함
# 리스트의 앞쪽을 잘라서 새로운 리스트를 만드는 방식 사용
bowl.append( deque(list(map(int, sys.stdin.readline().split()))) )

# 전치행렬 후 reverse
def rotate_90_clockwise2(bowl):
    # 행렬 뒤바뀜
    ro_bowl = [[0 for _ in range(bowl)] for _ in range(len(bowl[0]))]
    
    for i in range(len(bowl)):
        for j in range(len(bolw[0])):
            ro_bowl[j][i] = bowl[i][j]
    
    for ri, r in ro_bowl:
        ro_bowl[ri] = r[-1::-1]
        
    return ro_bowl


def rotate_90_clockwise(bowl):
    # 행렬길이 뒤바뀜
    ro_bowl = [[0 for _ in range(len(bowl))] for _ in range(len(bowl[0]))]
    
    for i in range(len(bowl)):
        for j in range(len(bowl[0])):
            ro_bowl[j][i] = bowl[i][len(bowl[0])-j-1]
        
    return ro_bowl


def fly_bowl(bowl):
    while(True):
        # 맨 끝에 한 줄 남은 길이보다 row 길이가 길면 다음 진행 불가능
        if len(bowl) > len(bowl[0]) - len(bowl[-1]):
            break
        
        new_bowl = []
        new_bowl_row = len(bowl)
        new_bowl_col = len(bowl[-1])
        
        for r in range(new_bowl_row):
            new_q = deque()
            for c in range(new_bowl_col):
                new_q.append(bowl[r].popleft())
            new_bowl.append(new_q)
        
        bowl = [bowl[0]]
        new_bowl = rotate_90_clockwise(new_bowl)
        for n in new_bowl:
            bowl.append(deque(n))
    
    return bowl


def bowl_in_a_row(bowl):
    new_bowl = deque()
    
    # 쌓은 블록 먼저 확인
    for c in range(len(bowl[-1])):
        for r in range(len(bowl)):
            new_bowl.append(bowl[r][c])
            
    #new_bowl.extend(list(bowl[0])[len(bowl[0])-len(bowl[-1]):])
    
    for c in range(len(bowl[-1]), len(bowl[0])):
        new_bowl.append(bowl[0][c])
    
    return list([new_bowl])
    
    
def rotate_180_clockwise(bowl):
    # 행렬길이 동일
    # 맨 아래줄 먼저 탐색해서 뒤집기
    new_bowl = []
    for r in range(len(bowl)-1, -1, -1):
        new_bowl.append(deque(bowl[r][-1::-1]))
        #print('///',bowl[r])
        #new_bowl.append(bowl[r].reverse())
    #print('//',new_bowl)
    return new_bowl


def fly_bow2(bowl):
    step1 = []
    tmp_l = []
    for _ in range(N//2):
        tmp_l.append(bowl[0].popleft())
    step1.append(tmp_l)
    #step1.append([1,2,3,4])
    #print('?',step1)
    step1 = rotate_180_clockwise(step1)
    #print('?',step1)
    #bowl.append(deque(step1))
    bowl += step1
    #print('!', bowl)
    
    step2 = []
    for r in range(2):
        tmp_2 = []
        for c in range(N//4):
            tmp_2.append(bowl[r].popleft())
        step2.append(tmp_2)
    
    #print(step2)
    step2 = rotate_180_clockwise(step2)
    bowl += step2
    #print('!', bowl)
    
def move_fish(bowl):
    bowl_cal = [[0 for _ in range(len(bowl[r]))] for r in range(len(bowl))]
    for r in range(len(bowl)):
        for c in range(len(bowl[r])):
            for di in d:
                nr = r+di[0]
                nc = c+di[1]
                if 0 <= nr < len(bowl) and 0 <= nc < len(bowl[nr]):
                    mok = abs(bowl[r][c] - bowl[nr][nc])//5
                    if mok > 0:
                        if bowl[r][c] > bowl[nr][nc]:
                            bowl_cal[r][c] -= mok
                            #bowl_cal[nr][nc] += mok
                        else:
                            bowl_cal[r][c] += mok
                            #bowl_cal[nr][nc] -= mok
                                
    for r in range(len(bowl)):
        for c in range(len(bowl[r])):
            bowl[r][c] += bowl_cal[r][c]
    return bowl


cnt = 0
while(True):
    
    cnt += 1
    #map_print(bowl)

    # 물고기 추가
    min_fish = min(bowl[0])
    for i in range(N):
        if bowl[0][i] == min_fish:
            bowl[0][i] += 1
    #map_print(bowl)


    # 어항 쌓기
    # 맨 첫번째 원소 하나 빼서 다음 row에 추가(위에 올리기)
    b1 = bowl[0].popleft()
    bowl.append(deque([b1]))
    #map_print(bowl)


    # 맨 끝 줄 90도 돌려서 row에 올리기
    bowl = fly_bowl(bowl)
    #map_print(bowl)

    
    # 인접어항 물고기 비교해서 재분배
    #d = [(0,1),(0,-1),(-1,0),(1,0)] # 동 서 남 북
    bowl = move_fish(bowl)
    #map_print(bowl)


    # 어항 해체
    # 열을 고정 행을 N-1부터 0까지 확인해서 재배열
    bowl = bowl_in_a_row(bowl)
    #map_print(bowl)


    # 어항 접기1
    fly_bow2(bowl)
    #map_print(bowl)
    
    # 인접어항 물고기 비교해서 재분배
    bowl = move_fish(bowl)
    #map_print(bowl)


    # 어항 해체: 위랑 규칙 똑같음
    bowl = bowl_in_a_row(bowl)
    #map_print(bowl)
    
            
    # 어항 정리 끝 확인
    if (max(bowl[0]) - min(bowl[0])) <= K:
        #print(max(bowl[0]) - min(bowl[0]))
        break


print(cnt)











