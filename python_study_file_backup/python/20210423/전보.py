
# 모든 노드가 아닌 한 도시에서 다른 도시까지의 최단거리 문제 : 다익스트라 사용해야함

import heapq
import sys
input = sys.stdin.readline

INF = int(1e9)

n, m, c = map(int, input().split())

graph = [ []*(n+1) for _ in range(n+1) ]

for _ in range(m) :
    x, y, z = map(int, input().split())
    graph[x].append((y, z))

# 최단 거리 table
distance = [INF]*(n+1)

# q에서 탐색 노드 저장
def dijkstra(start) :
    q = []
    
    # 시작 노드가 시작노드로 가기 위한 거리 0
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q :
        dist, now = heapq.heappop(q)

        # 더 작은 거리값으로 now node 탐색 완료 했기 때문에 continue
        if distance[now] < dist :
            continue

        # 현재 노드와 인접한 node 확인
        for i in graph[now] :
            cost = i[1] + dist
            if distance[i[0]] > cost :
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

dijkstra(c)

# 도달할 수 있는 노드의 개수
count = 0

# 도달할 수 있는 노드 중 가장 멀리 있는 노드와의 최단 거리
max_distance = 0

for d in distance :
    if d != INF :
        count += 1
        max_distance = max( d, max_distance )

# 시작 노드는 제외하기 위해 -1
print(count-1, max_distance)






