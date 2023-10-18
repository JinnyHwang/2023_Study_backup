import heapq


a = 'test'
b = 222
c = 1.23445
print(f"{a}  {b}  {c:.2f}")



n = int(input())
arr = list(map(int, input().split()))

max_res = 0
for k in range(1,n-1):
    new_arr = arr[k:]

    pq = []
    for na in new_arr:
        heapq.heappush(pq,na)
    heapq.heappop(pq)

    res = sum(pq)/len(pq)
    max_res = max(max_res, res)
print('%0.2f'%max_res)
print(f'{max_res:.3f}')
#print('{:.2f}'.format(max_res))

