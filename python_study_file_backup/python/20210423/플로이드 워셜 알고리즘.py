

# 모든 지점에서 다른 모든 지점까지의 최단 경로를 구해야하는 경우 사용
# 최단 거리를 가지는 노드를 하나씩 반복적으로 선택
# 해당 노드를 거쳐 가는 경로를 확인하며 최단 거리 테이블 갱신
# 각 단계마다 거쳐가는 노드를 기준으로 알고리즘 수행
# (매번 방문하지 않은 노드 중 최단 거리를 갖는 것 판별하지 않아도 됨)
# 4 - > 2 로 가는 최단 경로는?

# p.252 확인
# D42를 구할 때 한 개 node를 거쳐갈 땐 구해지지 않음 
# 그러나 D41 + D12 / D43 + D32 방식으로 계산할 때 이전 step에서 계산 되었던 D32 값이 있기 때문에
# D42 값을 도출할 수 있음
# 한 번에 갈 때, 중간에 한 노드를 거쳐갈 때 탐색하며 이전에 계산된 값을 활용해 계산됨.

# start node 입력받을 필요 없음

import sys
input = sys.stdin.readline
INF = int(1e9)

n = int(input())
m = int(input())

graph = [ [INF]*(n+1) for _ in range(n+1) ]

# 자기 자신으로 가는 경우 0으로 초기화
for i in range(1, n+1) :
    for j in range(1, n+1) :
        if i == j :
            graph[i][j] = 0

# 각 간선에 대한 정보 입력 후 write
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1) : # step(경유 node)
    for a in range(1, n+1) : # start node
        for b in range(1, n+1) : # end node
            graph[a][b] = min( (graph[a][k] + graph[k][b]), graph[a][b] )


for i in range(1, n+1) :
    for j in range(1, n+1) :
        if graph[i][j] == INF :
            print('INF', end=' ')
        else :
            print(graph[i][j], end=' ')
    print()

        









