
'''
상어에는 1 이상 M 이하의 자연수 번호가 붙어 있고, 모든 번호는 서로 다르다.
상어들은 영역을 사수하기 위해 다른 상어들을 쫓아내려고 하는데,
1의 번호를 가진 어른 상어는 가장 강력해서 나머지 모두를 쫓아낼 수 있다.

N×N 크기의 격자 중 M개의 칸에 상어가 한 마리씩 들어 있다.



1. 맨 처음에는 모든 상어가 자신의 위치에 자신의 냄새를 뿌린다.
2. 그 후 1초마다 모든 상어가 동시에 상하좌우로 인접한 칸 중 하나로 이동하고,
3. 자신의 냄새를 그 칸에 뿌린다.
4. 냄새는 상어가 k번 이동하고 나면 사라진다.

**반복**
 1. 상어들 위치에서 냄새 뿌리기
    -> 상어번호, k
 
 2. 상어 이동시키기
    -> 상어 이동시키고 position을 확인
    -> 중복 position이 있는가?
    -> 값이 가장 같은 상어 1개만 남고 나머지 다 ㅂㅇㅂㅇ
    ==> 1번 상어 하나만 남으면 반복 end처리
    -> 각 상어 이동 position 먼저 파악, 중복 확인, 이동시킴
 
 3. 반복횟수 누적하기
    -> 1000번째 반복이면 반복 멈추고 return -1
 4. 시간에 따라 냄새 없애기 -> 냄새값을 k로 주자 한 번 반복할 때마다 -1씩

 

각 상어가 이동 방향을 결정할 때는,

1. 먼저 인접한 칸 중 아무 냄새가 없는 칸의 방향으로 잡는다.
2. 그런 칸이 없으면 자신의 냄새가 있는 칸의 방향으로 잡는다.
3. 이때 가능한 칸이 여러 개일 수 있는데, 그 경우에는 특정한 우선순위를 따른다.
3-1. 우선순위는 상어마다 다를 수 있고,
3-2. 같은 상어라도 현재 상어가 보고 있는 방향에 따라 또 다를 수 있다.
--> 모든 상어는 보고있는 방향에 따른 이동 우선순위가 있음
--> 방향 d[보는방향][0~3우선순위에 따라]


상어 좌표, 상어 방향(마지막 이동 방향으로 변경됨)
상어가 맨 처음에 보고 있는 방향은 입력으로 주어지고,
그 후에는 방금 이동한 방향이 보고 있는 방향이 된다.


모든 상어가 이동한 후
한 칸에 여러 마리의 상어가 남아 있으면,
-> 상어 이동시키고 position을 확인
-> 중복 position이 있는가?

가장 작은 번호를 가진 상어를 제외하고
모두 격자 밖으로 쫓겨난다.
-> 값이 가장 같은 상어 1개만 남고 나머지 다 ㅂㅇㅂㅇ


--> 이렇게해서 가장 강한 1번 상어만 남을 때 까지 걸리는 시간은?
반복 횟수가 누적 값
---> 그런데 1000초가 넘어도 다른 상어가 있다? -1 return

'''

#from copy import deepcopy
import sys
sys.setrecursionlimit(10000)

# map[N][N]
# N:격자크기 / M:상어마리수 / k:냄새유지시간
N, M, k = map(int, input().split())

# shark_map[i][j] 는 [상어번호, 냄새]
# 정보를 가지고 있다
# 상어 번호 : shark_map[i][j][0]
# 상어 냄새 : shark_map[i][j][1]
shark_map = [ [] for _ in range(N) ]

# 상어 정보 [n, m, 상어방향]
# shark_info[num] : num 1~M : 상어 번호
# n,m,방향 : shark_info[][0] / shark_info[][1] / shark_info[][2]
shark_info = [ [] for _ in range(M+1) ]

l = []
# 상어 map
# 맨 처음 상어 위치. 상어가 맨 처음 냄새 뿌린거 기억하고 있음
for i in range(N):
    l = list(map(int, input().split()))
    #print(l)
    #shark_map.append(list(map(int, input().split())))
    for j in range(N):
        shark_map[i].append( [ l[j], 0 ] )
        if shark_map[i][j][0] != 0:
            shark_info[shark_map[i][j][0]] = [ i, j ]
            
#print(shark_map)
#print(shark_info)
            
# 각 상어 방향
sd = list( map(int, input().split()) )
for i, s in enumerate(shark_info):
    if i == 0:
        continue
    s.append(sd[i-1]-1)

#print(shark_info)
#shark_info.pop(1)
#print(shark_info)

# 1:위 , 2:아래 , 3:왼쪽 , 4:오른쪽
di = [(-1,0), (1,0), (0,-1), (0,1)]

# d[m][sd][0~3 순서대로 탐색]
# m:상어번호 / sd:현재상어방향
# di[ d[m][sd][0~3] ] : 상어가 가고자 하는 방향
d = [ [] for _ in range(M) ]


#print(d)
for m in range(M):
    for i in range(4):
        d[m].append(list(map(int, input().split())))
        for j in range(4):
            d[m][i][j] -= 1
#print(d)    


# 새로 구성한 map에서 0이 아닌 값 -1
# new_shark_map[][][1] 값을 -1
# 만약 냄새값이 0이되면 new_shark_map[][][0] 값도 함께 0
def remove_smell(shark_map):
    for i in range(N):
        for j in range(N):
            # 0이 아닌 값(냄새가 남아있는 칸) -1
            if shark_map[i][j][1] != 0:
                shark_map[i][j][1] -= 1
                # 만약 해당 칸 냄새가 0이 됐으면? 상어 번호도 초기화
                if shark_map[i][j][1] == 0:
                    shark_map[i][j][0] = 0


def fill_smell(shark_map, shark_info):
    
    for i, s in enumerate(shark_info):
        if i == 0:
            continue
        if not s:
            continue
        # i번 상어가 현재 위치한 곳을 확인
        # 상어 냄새 정보에 i값을 채움
        shark_map[s[0]][s[1]] = [i,k]
        
        
def shark_check(shark_info):
    MM = len(shark_info)
    pop_list = []
    #print(shark_info)
    
    # 강한 상어 먼저 탐색
    for m in range(1,MM):
        if not shark_info[m]:
            continue
        # 보다 작은 상어가 같은 좌표에 있다? 상어 정보 날림
        for mm in range(m+1, MM):
            # index 0,1 즉 x,y 좌표가 같은 경우 확인
            #print(m, mm)
            if shark_info[m][:2] == shark_info[mm][:2]:
                # 같은 위치정보 가진 약한 상어 날리기
                #shark_info.pop(mm)
                pop_list.append(mm)
    
    if not pop_list:
        return
    
    # 위치 좌표 동일한 상어 존재하면 pop()으로 원소 삭제
    # shark_info index 값이 상어 정보
    # pop으로 아예 날리지 말고 빈리스트로
    for p in pop_list:
        shark_info[p] = []
    
    

def shark_move_shell(shark_map, shark, num, next_pos_check):
    
    for i in range(4):
        ni = shark[0] + di[i][0]
        nj = shark[1] + di[i][1]
        
        if ni < 0 or ni >= N or nj < 0 or nj >= N:
            continue
        
        if shark_map[ni][nj][0] == num:
            next_pos_check.append( [ni,nj,i] )


# 변경된 pos는 shark[:2]에 저장
# 변경된 방향은 shark[2]에 저장
def shark_move_direct(shark_map, shark, shark_num, num):
    
    # 방향 개수 4가지
    for c in range(4):
        nd = d[shark_num-1][shark[2]][c]
        # 우선순위 돌려봄
        nx = shark[0] + di[nd][0]
        ny = shark[1] + di[nd][1]
        
        if nx < 0 or nx >= N or ny < 0 or ny >= N:
            continue
        
        # 해당 칸 값이 원하는 num와 일치하면 좌표값 return
        if shark_map[nx][ny][0] == num:
            shark[:2] = [nx,ny]
            shark[2] = nd
            return
        
    # 이 경우는 정말 코드 이상하게 짠거
    return -1
        

 # 상어의 다음 위치는? next_pos
# 1. 아무 냄새가 없는 칸 확인
# 0인 칸 확인
        
# -> 이런 칸이 여러개면? 우선순위 확인
# 상어 number, 방향을 알면 고를 수 있다
# shark_move_direct(s)
def shark_move(shark_map, shark_info):
    
    
    
    # shark_info만큼 반복
    # 정보를 토대로 shark_info 바꿈
    # shark[0] / shark[1] / shark[2]
    for i, shark in enumerate(shark_info):
        if i == 0:
            continue
        
        if not shark:
            continue
        
        next_pos_check = []
        next_pos = []
        
        # 칸 값이 0일 때 갈 수 있는 경우의 수 next_pos_check에 저장
        shark_move_shell(shark_map, shark, 0, next_pos_check)
        #print('next_pos_check: ',next_pos_check)
        if len(next_pos_check) > 1:
            #print('i: ',i,'\t next_pos_check: ', next_pos_check)
            # 우선순위 확인
            # next_dir에 변경된 방향 저장
            if shark_move_direct(shark_map, shark, i, 0) == -1:
                print('1 코드 이상해')
            
        elif len(next_pos_check)  == 1:
            shark_info[i] = next_pos_check.pop()
            #print('shark: ',shark)
            #print('shark_info: ',shark_info)
            
        # 2. 빈 칸이 없으면 자신의 냄새가 있는 칸으로
        # -> 여러개면? 우선순위 확인
        else:
            shark_move_shell(shark_map, shark, i, next_pos_check)
            if len(next_pos_check) > 1:
                # 우선순위 확인
                # next_dir에 변경된 방향 저장
                if shark_move_direct(shark_map, shark, i, i) == -1:
                    print('2 코드 이상해')
                    
            elif len(next_pos_check)  == 1:
                shark_info[i] = next_pos_check.pop()
            
            # 끝까지 이동할 공간이 없는 경우는 없음
            else:
                print('너 뭔가 코드 잘못 세웠다')
       
    
    


def bfs(shark_map, shark_info, time):
    
    global result
    
    #if time == 5:
    if time > 1000:
        result = -1
        return
    #else:
        #print('time: ',time)
    
    #new_shark_map = deepcopy(shark_map)
    #print('1: Start\n',shark_map, '\n',shark_info)
    
    # 상어 냄새 뿌리기
    fill_smell(shark_map, shark_info)
    #print('2: 상어 냄새 뿌리기\n',shark_map, '\n',shark_info)
    
    # 상어 이동시키기
    shark_move(shark_map, shark_info)
    #print('3: 상어 이동시키기\n',shark_map, '\n',shark_info)
    
    # 중복 상어 확인
    shark_check(shark_info)
    #print('4: 중복 상어 확인\n',shark_map, '\n',shark_info)
    
    
    # 2 ~ 4 상어 정보가 빈 리스트면 끝
    cnt = 0
    for s in shark_info:
        if s:
            cnt += 1
    if cnt == 1:
        #print('한 마리 남은 상어',time)
        result = time
        return
    
    # 냄새 제거
    remove_smell(shark_map)
    #print('5: 냄새 제거\n',shark_map, '\n',shark_info)
    
    #print('time: ',time,'\nshark_map\n',shark_map,'\nshark_info\n',shark_info,'\n')
    
    #try:
    # 횟수 누적
    bfs(shark_map, shark_info, time+1)
    #except:
        #result = -1
        


result = 0
bfs(shark_map, shark_info, 1)
print(result)

