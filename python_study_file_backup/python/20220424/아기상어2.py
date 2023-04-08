
# 모든 칸 탐색
# 해당 칸에서 상어까지 거리를 확인
# 안전거리가 가장 짧은 칸을 저장

N, M = map(int, input().split())
shark_map = []
shark = []

for n in range(N):
    #shark_map[n] = list( map(int, input().split()) )
    shark_map.append( list( map(int, input().split()) ) )
    for m in range(M):
        if shark_map[n][m] == 1:
            # 변하지 않는 값 튜플
            shark.append( (n, m) )
    
print(shark_map)
print(shark)

# 대각선까지 포함한 8개 direction
d = [ (-1, -1),(-1, 0),(-1, 1),(0,1),(1, 1),(1,0),(1,-1),(0,-1) ]

# 모든 아기 상어 확인

from collections import deque

# 해당 좌표에서 상어까지 얼마나 걸리는가?
def bfs(n, m, shark):
    
    q = deque()
    q.append( (n, m, 0) )
    
    time = 0
    roots = []
    visited = [ [0]*M for _ in range(N) ]
    
    while q:
        cn, cm, c = q.popleft()
        #print('?',cn, cm, c)
        
        if visited[cn][cm] != 0:
            continue
        
        visited[cn][cm] = c
        
        #if n == shark[0] and m == shark[1]:
            #print('??')
        roots.append((c, n, m))
        
        for dn, dm in d:
            nn = n + dn
            nm = m + dm
            
            if 0 <= nn < N and 0 <= nm < M:
                q.append( (nn, nm, c+1) )
                #print('????')
                #print('!',nn, nm, c+1
    
    print('roots',roots)
    print('visited',visited)
    #print(n, m, time)
    #if map_check[n][m] == 0 or map_check[n][m] > time:
    #    map_check[n][m] = time
    
    #return map_check
   

map_check = [ [0]*M for _ in range(N) ]
roots = []

for s in shark:
    print('shark',s)
    bfs(0, 0, s)
    
    #for n in range(N):
    #    for m in range(M):
            #root = bfs(n, m, s)
     #       roots.append(bfs(n, m, s))
            
    #print('roots',roots)
    
print(map_check)






















