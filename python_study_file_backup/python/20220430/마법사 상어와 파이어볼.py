
'''
N*N 격자
이어져있다
nx = (x + d[][0])%N
ny = (y + d[][1])%N


파이어볼 M개

맨 처음 파이어볼은 각자 위치에서 이동을 대기함

파이어볼은
위치 (r,c) / 질량 m / 방향 d / 속력 s

방향    ↑,      ↗,   →,   ↘,   ↓,     ↙,    ←,    ↖
d = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]


1. 모든 파이어볼은 d방향으로 s칸 만큼 이동한다
- 이동하는 중 같은 칸에 여러개 파이어볼이 있을 수 있다
=> 이게 무슨말? 이동 중은 신경쓰지 말고 결과값만 보라는 뜻이겠지?

2. 이동이 끝난 뒤 파이어볼이 2개 이상이면?
    (1) 같은 칸에 있는 파이어볼은 하나로 합쳐짐
    (2) 파이어볼은 4개로 나눠짐. 나눠진 파이어볼은 정보는?
    - 질량: (합쳐진 파이어볼 질량 합)//5
    - 속력: (합쳐진 파이어볼 속력 합)//(개수)
    - 방향: if 합쳐진 파이어볼이 모두 홀수or짝수 : 0,2,4,6(상하좌우)
            아니면 1,3,5,7(대각선)
    (3) 질량이 0이면 소멸


이동명령 K번 후 남은 파이어볼의 질량은?

'''

from copy import deepcopy

#방향    ↑,      ↗,   →,   ↘,   ↓,     ↙,    ←,    ↖
di = [(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1),(0,-1),(-1,-1)]


# 격자N*N / 파이어볼 개수 M / 명령횟수 K
N, M, K = map(int, input().split())
#print(N, M, K)

fire = []
l = []
for _ in range(M):
    l = list(map(int, input().split()))
    l[0] -= 1
    l[1] -= 1
    fire.append(l)
        
#fire = [ list(map(int, input().split())) for _ in range(M) ]
#print(fire)

new_fire = []

for _ in range(K):
    
    #print('1 fire: ',fire)
    # 현재 fire의 좌표를 이동
    for i, f in enumerate(fire):
        # 파이어볼이 이동한 좌표
        nx = (f[0] + di[f[4]][0]*f[3])%N
        ny = (f[1] + di[f[4]][1]*f[3])%N
        #print('? f: ',f, '  nx,ny? ', nx,ny,'  f[3],f[4]? ', f[3],f[4], '  di[f[4]]? ',di[f[4]])
        fire[i][0:2] = [nx,ny]
    
    #print('2 fire: ',fire)
    # 좌표 순으로 정렬됨
    fire.sort()
    #print('3 fire: ',fire)
    
    visited = [ [0] for _ in range(len(fire)) ]
    for i in range(len(fire)):
        tmp = []
        
        if visited[i] == 1:
            continue
        
        i2 = i+1
        
        #print(' i, i2?', i,i2)
        while 0 <= i2 < len(fire):
            if fire[i][0:2] == fire[i2][0:2]:
                # 만약 중복된거 맨 처음 찾은거면 현재 fire도 tmp에 넣는다
                if not tmp :
                    tmp.append(fire[i])
                    visited[i] = 1
                    
                tmp.append(fire[i2])
                visited[i2] = 1
                i2 += 1
            else:
                break
        # 같은 좌표 fire가 존재할 때
        if tmp:
            # 조건에 맞게 new_fire 채우기
            tm = 0
            ts = 0
            td1 = 0 # 짝수
            td2 = 0 # 홀수
            for t in tmp:
                tm += t[2]
                ts += t[3]
                if t[4]%2 == 0:
                    td1 += 1
                else:
                    td2 += 1
                
            ntm = tm//5
            nts = ts//len(tmp)
            
            # 파이어볼 사라짐
            if ntm == 0:
                continue
            
            # 파이어볼 4개로 나눠짐
            # 모두 홀수이거나 짝수인 경우 0,2,4,6(상하좌우)
            if td1 == 0 or td2 == 0:
                for dd in range(0,8,2):
                    new_fire.append( [fire[i][0], fire[i][1], ntm, nts, dd] )
            # 1,3,5,7(대각선)
            else:
                for dd in range(1,8,2):
                    new_fire.append( [fire[i][0], fire[i][1], ntm, nts, dd] )
                   
        else:
            # 같은 위치에 없으면 
            new_fire.append(fire[i])
    
    #print('1 new_fire: ',new_fire)
    fire = deepcopy(new_fire)
    new_fire = []
    


result = 0
for f in fire:
    result += f[2]
print(result)

