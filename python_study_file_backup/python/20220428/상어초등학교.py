
'''
자리정하기

N*N 교실
N^2명 학생

r : 상하
c : 좌우
class[r][c]

인접한 칸은 즉 상하좌우 칸을 의미
d = [(-1,0),(1,0),(0,-1),(0,1)]


학생 순서 정해져있음
각 학생이 좋아하는 학생 4명씩 조사


1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
-> 비어있는 칸의 상하좌우 모두 살핌.
-> 좋아하는 학생 수가 가장 많이 있는 칸 선택

2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
-> 비어있는 칸이 가장 많은 칸 무슨 말?
-> 벽이 있는 경우 칸 수가 다름
-> 인접 공간에 빈 칸이 더 많은 쪽으로

3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
--> [r,c] sort해서 가장 앞순서


=> 학생의 만족도 : 자리배치가 모두 끝난 후 구할 수 있음
한 학생과 인접한 칸에 앉은 좋아하는 학생의 수
각 학생의 만족도를 구해서 더하기


?? 가장 맨 첫번째 학생의 자리는 픽스??
아니면 여러개 가능??
--> 조건보고
-> 3번 조건으로 무조건 (1,1) 이 첫번째 학생 자리
'''

d = [(-1,0),(1,0),(0,-1),(0,1)]

# 교실 크기
N = int(input())

stu_num = N**2

# 확인할 학생 순서
# stu_turn[0 ~ (stu_num-1)] : 탐색해야하는 순서
stu_turn = []

# 학생들의 친한 친구들
# stu_info[num] : num: 학생 번호
# stu_info[num][0~3] : 좋아하는 학생들
stu_info = [ [] for _ in range(stu_num+1) ]

#print('stu_info : ',stu_info)

read = []
# 학생이 좋아하는 학생 정보
for i in range(stu_num):
    read = list( map(int, input().split()) )
    
    # 탐색해야하는 학생 순서대로 input
    # 학생 1~N*N 
    stu_turn.append(read[0])
    
    # 학생 1~N*N 
    stu_info[read[0]] = read[1:]

#print(stu_info)

# 교실 리스트
# class_map[r][c] : 자리에 앉은 학생 번호가 있음
class_map = [ [0]*N for _ in range(N) ]

#print('class_map: ', class_map)

'''
1. 비어있는 칸 중에서 좋아하는 학생이 인접한 칸에 가장 많은 칸으로 자리를 정한다.
-> 비어있는 칸의 상하좌우 모두 살핌.
-> 좋아하는 학생 수가 가장 많이 있는 칸 선택

2. 1을 만족하는 칸이 여러 개이면, 인접한 칸 중에서 비어있는 칸이 가장 많은 칸으로 자리를 정한다.
-> 비어있는 칸이 가장 많은 칸 무슨 말?
-> 벽이 있는 경우 칸 수가 다름
-> 인접 공간에 빈 칸이 더 많은 쪽으로

3. 2를 만족하는 칸도 여러 개인 경우에는 행의 번호가 가장 작은 칸으로,
그러한 칸도 여러 개이면 열의 번호가 가장 작은 칸으로 자리를 정한다.
--> [r,c] sort해서 가장 앞순서
'''
def stu_sit_check(stu_num):
    
    # 조건 확인
    # 비어있는 칸 확인
    # 빈 칸의 정보 append
    # 좋아하는 학생 수 cnt 정보, 주변에 비어있는 칸 개수, 비어있는 칸의 좌표 확인
    # append([(4-좋아하는 학생 수 cnt 정보), (4-비어있는 칸 개수), r, c])
    # 오름차순으로 sort()
    # 무조건 맨 앞에 는 좌표!
    # return [ list[0][2], list[0][3] ]
    
    # stu_num가 들어갈 수 있는 모든 칸 정보
    stu_pos_list = []
    
    for r in range(N):
        for c in range(N):
            # 비어있다?
            if class_map[r][c] == 0:
                like = 0 # 좋아하는 학생 수
                empty = 0 # 비어있는 칸 개수
                
                # 비어있는 칸의 상하좌우 다 살피기
                for di in d:
                    nr = r+di[0]
                    nc = c+di[1]
                    
                    if 0 <= nr < N and 0 <= nc < N:
                        # 상하좌우에 좋아하는 학생 있는가
                        #print('!! stu_num: ',stu_num,'\n ',stu_info[stu_num])
                        #print('??? ', class_map[nr][nc] in stu_info[stu_num],'\n')
                        if class_map[nr][nc] in stu_info[stu_num]:
                            like += 1
                        # 빈칸이 있는가
                        elif class_map[nr][nc] == 0:
                            empty += 1
                            
                stu_pos_list.append([(4-like), (4-empty), r, c])
                
    #print('stu_num: ',stu_num)
    #print('stu_info: ',stu_info[stu_num])
    #print('탐색: ',stu_pos_list)
    stu_pos_list.sort()
    #print('정렬: ',stu_pos_list)
    #print(stu_pos_list[0])
    #print(stu_pos_list[0][2:])
        
    # 맨 앞 원소의 [r,c] return 
    return stu_pos_list[0][2:]
                            
                            
                            
                            
def stu_survey():
    
    satisfy = 0
    
    # 만족도 조사
    for r in range(N):
        for c in range(N):
            # 학생 번호 : class_map[r][c]
            
            # 현재 위치에서 상하좌우에 있는 학생 번호 확인
            # 그 학생 번호가 친한학생 리스트에 있으면 만족도 +1
            
            #print('stu_num: ',class_map[r][c])
            #print('stu_info: ',stu_info[class_map[r][c]])
            
            cnt = -1
            for di in d:
                nr = r+di[0]
                nc = c+di[1]
                
                if 0 <= nr < N and 0 <= nc < N:
                    #print('누구? ',class_map[nr][nc])
                    if class_map[nr][nc] in stu_info[class_map[r][c]]:
                        cnt += 1
            #print('cnt: ',cnt)
            if cnt != -1:
                satisfy += 10**cnt
            #print(satisfy,'\n')
    
            
    return satisfy
                



# i는 탐색 횟수
# stu[0] : 학생 번호
# stu[1:] : 학생이 좋아하는 친구들 번호
for i in stu_turn:
    
    # i: 확인할 학생 번호
    # stu_info[i] : i학생이 친한 학생들
    
    # 학생 자리 배치 시작
    stu_pos = stu_sit_check(i)

    class_map[stu_pos[0]][stu_pos[1]] = i
    #print('class_map: ',class_map)



# 만족도 조사
print(stu_survey())

