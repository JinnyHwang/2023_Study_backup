import heapq

pq = []
n = int(input())
for _ in range(n):
    num = int(input())
    if num == 0:
        if not pq:
            print(num)
        else:
            print(heapq.heappop(pq))
    else:
        heapq.heappush(pq,num)
        

points = [(1,7),(3,2),(3,1),(6,2)]
pq = []

for p in points:
    x,y = p
    heapq.heappush(pq,(-x,-y))
    
    bx,by = pq[0]
    print(-bx,-by)


