import heapq
def solution1(scoville, K):
    
    # 작은 원소 2개로 계산
    # min heap으로 정렬
    heapq.heapify(scoville)
    count = 0

    while True:
        
        min1 = heapq.heappop(scoville)

        if K <= min1:
            break
        
        if len(scoville) == 0:
            return -1
        
        min2 = heapq.heappop(scoville)
        heapq.heappush(scoville, min1 + (min2*2))
        count += 1
            
    return count

def solution(scoville, K):
    
    heapq.heapify(scoville)

    min1 = heapq.heappop(scoville)
    for i in range(1, len(scoville)):
        min2 = heapq.heappop(scoville)
        min1 = heapq.heappushpop(scoville, min1 + min2*2)
        if min1 >= K :
            return i
    return i

def solution(scoville, K):
    
    heapq.heapify(scoville)

    min1 = heapq.heappop(scoville)
    for i in range(1, len(scoville)+1):
        min2 = heapq.heappop(scoville)
        min1 = heapq.heappushpop(scoville, min1 + min2*2)
        if min1 >= K :
            return i
        print(scoville, min1 + min2*2)
    return -1

print(solution([1,2,3], 11))
#print(solution([1, 2, 3, 9, 10, 12], 7))


