
from collections import deque

N, M = map(int, input().split())
shark_map = []
shark = deque()

for n in range(N):
    #shark_map[n] = list( map(int, input().split()) )
    shark_map.append( list( map(int, input().split()) ) )
    for m in range(M):
        if shark_map[n][m] == 1:
            # 변하지 않는 값 튜플
            shark.append( (n, m) )
    
#print(shark_map)
#print(shark)

# 대각선까지 포함한 8개 direction
d = [ (-1, -1),(-1, 0),(-1, 1),(0,1),(1, 1),(1,0),(1,-1),(0,-1) ]

result = 0

# queue를 사용해서
# 상어와 가장 가까운 지점 먼저 값이 채워짐
# 가장 작은 값 먼저 채워지고
# 빈 공간에 다음 값들이 채워짐
# 가질 수 있는 가장 작은 값이 먼저 채워지고
# 남은 빈공간을 채우는 방식이므로
# 별도의 조건처리 필요하지 않음
# 이렇게 심플한 구조는.. 어떻게 생각하는걸까?
while shark:
    # 상어를 기준점으로 모든 좌표의 거리값을 구한다
    # 상어있는 점을 먼저 확인
    n, m = shark.popleft()
    #print('??',n, m, shark_map[n][m])
    for dn, dm in d:
        nn = n + dn
        nm = m + dm
            
        if 0 <= nn < N and 0 <= nm < M:
            # 상어 없는 칸 모두 check
            # 상어가 있는 칸이 1 값이므로
            # 결과값은 -1을 해주어야한다
            if shark_map[nn][nm] == 0:
                shark.append( (nn, nm) )
                shark_map[nn][nm] = shark_map[n][m]+1
                result = max(result, shark_map[n][m]+1)
                
                for i in range(N):
                    for j in range(M):
                        print(shark_map[i][j],end=' ')
                    print('\n')
                
                print('n:{} m:{} shark_map[n][m]:{} shark_map[nn][nm]:{}'.format(n, m,shark_map[n][m],shark_map[nn][nm]))

print(shark_map)
print(result-1)




















