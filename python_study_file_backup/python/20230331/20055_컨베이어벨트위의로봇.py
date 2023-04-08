
'''
0 ~ N-1 : 로봇을 올릴 수 있는 index
N ~ 2N-1



'''
N, K = map(int, input().split())

# 컨베이어 내구도 리스트
con = list(map(int, input().split()))

# 로봇은 최대 N개 올라갈 수 있음
# 0은 로봇 없음
# 1은 로봇 있음
# N-1 ~ 0으로 역순으로 로봇 보면서 이동시킴
robot = [0 for _ in range(N)]
'''
robot = [1, 2, 3, 4, 0]
robot = [0] + robot[:N-2] + [0]
print(robot)

robot = [0] + robot[:N-2] + [0]
print(robot)
'''

cnt = 0

while(True):
    '''
    print(cnt)
    print('\n1번')
    print(con)
    print(robot)
    '''
    cnt += 1

    # 컨베이어 밸트 회전
    con = [con[-1]] + con[:-1]
    # 로봇 회전. 로봇 내리는 위치 즉시 내림
    robot = [0] + robot[:N-1]
    '''
    print('\n2번')
    print(con)
    print(robot)
    '''
    for i in range(N-1, 0, -1):
        if robot[i] == 1:
            # 내리는 위치면 내구도 차감 없이 로봇 이동
            if i+1 == N:
                robot[i] = 0
            
            # 내리는 위치 아니고, 내구도 남아있으면 이동
            elif con[i+1] >= 1 and robot[i+1] == 0: 
                con[i+1] -= 1
                robot[i:i+2] = [0,1]
    '''            
    print('\n3번')
    print(con)
    print(robot)
    '''            
    # 올리는 위치 내구도 0 아니면 로봇 올리기
    if con[0] != 0:
        con[0] -= 1
        robot[0] = 1
    '''    
    print('\n4번')
    print(con)
    print(robot)
    '''
    # 내구도 0 개수가 K개 이상
    if con.count(0) >= K:
        break

print(cnt)

