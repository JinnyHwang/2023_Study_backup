
# 지금까지 주어진 숫자들 중 최댓값을 출력
# 숫자가 주어질 때 마다 앞 숫자 탐색해서 최댓값을 고르면 O(N^2)
# treeset도 가능하지만
# priority queue를 사용해서 구해보자 최대값 찾기 O(logN)에 끝낼 수 있음. N(logN)

import heapq
'''
hq = []
heapq.heappush(hq,-item)
heapq.heappop(hq)
-hq[0]
'''

pq = []
heapq.heappush(pq,3)
heapq.heappush(pq,5)

# 최솟값 출력
print(pq, pq[0], len(pq))
heapq.heappop(pq)
if pq:
    print(pq, pq[0], len(pq))
heapq.heappop(pq)
if pq:
    print(pq, pq[0], len(pq))
else:
    print('empty')

arr = [3,6,2,6,7,7,2]
pq = []

for elem in arr:
    heapq.heappush(pq, -elem)
    print(-pq[0], end=' ')





