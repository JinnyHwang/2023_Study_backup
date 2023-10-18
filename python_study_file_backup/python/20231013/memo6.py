import heapq

points = [(1,7),(3,2),(3,1),(6,2)]

pq = []
for x,y in points:
    heapq.heappush(pq,(-(x*y), x,y))
    
    print(pq[0][1], pq[0][2])


n,m = tuple(map(int, input().split()))
points = [ tuple(map(int, input().split())) for _ in range(n)]
pq = []
for x,y in points:
    heapq.heappush(pq,((abs(x)+abs(y)),x,y))

for _ in range(m):
    _,x,y = heapq.heappop(pq)
    x,y = x+2,y+2
    heapq.heappush(pq,((abs(x)+abs(y)),x,y))

_,x,y = heapq.heappop(pq)
print(x,y)





