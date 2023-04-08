
# 시간 복잡도가 O(ElogV) (E 간선 개수 , V 노드 개수 ) : 개선된 다익스트라 알고리즘(dijkstra) - 힙 자료구조 이용

# 힙(heap) : 우선순위 큐 : 우선순위가 가장 높은 데이터를 먼저 삭제
# 힙을 따로 구현하지 않아도 기본 라이브러리에서 제공함!
# PriorityQueue / heapq
# heapq 속도가 더 빠름
# 우선순위 큐는 최소 힙(min heqap), 최대 힙(max heap)
# 다익스트라(dijkstra)는 비용이 적은 노드 우선 방문하므로 최소 힙(min heap) : 기본 우선순위 큐 라이브러리 그대로 사용

# 또한 최소 힙을 최대 힙처럼 사용하기 위해 일부러 우선순위에 해당하는 값이 음수 붙여 넣었다가,
# 큐에서 꺼낼 때 다시 음수를 붙혀 원래 값으로 사용 -> 기억하기!

# 우선순위 큐로 탐색 노드를 확인하기 때문에, get_smallest_mode()를 따로 구현할 필요가 없다

# heapq
# heapq.heappush(heap, data)
# heapq.heappop(heap)

# 기존 리스트를 힙으로 변경
# heapq.heapify(heap)

# max heap 구현
# heapq.heappush(heap, (-priority, data)) #우선순위에 음수값
# heapq.heappop(heap)[1] # 우선 순위가 큰 data부터 pop


import sys
input = sys.stdin.readline
INF = int(1e9)

import heapq

n, m = map(int, input().split())

start = int(input())

graph = [ [] for i in range(n+1) ]

for _ in range(m) :
    s, e, d = map(int, input().split())
    graph[s].append((e, d))

distance = [INF]*(n+1)

def dijkstra(start) :
    
    # queue에 push할 때 distance, node number 순으로. distance로 min heap 판별하기 때문
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q :

        dist, now = heapq.heappop(q)

        # 이전에 방문했던 node면 pass
        # 우선순위 queue이므로 distance[now] < dist 의미는,
        # 이미 now node에 더 작은 dist 값을 가진 data가 방문했었다는 의미
        # 해당 queue data는 더이상 탐색 없이 pass
        if distance[now] < dist :
            continue

        for i in graph[now] :
            cost = i[1]+dist

            # 더 짧은 간선 길이 확인
            if cost < distance[i[0]] :
                distance[i[0]] = cost
                # 탐색할 node까지 도달하는데 간선길이, node 번호 push
                heapq.heappush(q, (cost, i[0]))
        
        
dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print('infinity')
    else :
        print(distance[i])















    



