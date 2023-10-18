
# n개 숫자가 주어짐
# 그 중 가장 큰 숫자를 골라 1씩 빼는 작업 m번 반복
# 남아있는 숫자들 중 최댓값은?
import heapq

n, m = tuple(map(int, input().split()))
arr = list(map(int, input().split()))
pq = []

for a in arr:
    heapq.heappush(pq, -a)

for _ in range(m):
    #print('before?', pq)
    
    # 가장 큰 수 빼기
    num = -heapq.heappop(pq)
    #print('1 num? ', num)
    
    num -= 1
    #print('2 num? ', num)
    # 다시 정렬
    heapq.heappush(pq,-num)
    #print('after?', pq)


print(-pq[0])



