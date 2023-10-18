import heapq

# 중앙값은 어떻게 구할 수 있을까?
# 주어진 숫자가 2n+1개면?
# median이라는 중앙값을 기준으로 봤을 때
# 중앙값보다 작은 숫개 개수(n개) == 중앙값보다 큰 숫자 개수(n개)

# median은 어떻게 update해줄 수 있을까?
# 최대heap, 최소heap 활용
# median보다 작은 숫자들 중 최댓값
# 기존 median 값
# median보다 큰 숫자들 중 최솟값
# [0 ~ (median 이전 값 중 최댓값) median (median 이후 값 중 최솟값) ~ m]
#            max heap 활용                     min heap 활용

t = int(input())
arr = []

def find_median():
        
    min_pq = []
    max_pq = []
    median = arr[0]
    print(median,end=' ')
    
    for i in range(1,m):
        if i%2 == 1: # 짝수번째
            # median에 대한 기준이 모호함
            if arr[i] < median:
                heapq.heappush(max_pq,-arr[i])
            else:
                heapq.heappush(min_pq,arr[i])
            #print('짝수 - min_pq: ', max_pq, '  min_pq: ', min_pq)
        elif i%2 == 0:
            # min heap과 max heap 중 개수가 더 많은 곳 존재
            min_len = len(min_pq)
            max_len = len(max_pq)
            if min_len < max_len:
                new_cand = -heapq.heappop(max_pq)
            elif min_len > max_len:
                new_cand = heapq.heappop(min_pq)
            #print('홀수 - min_pq: ', max_pq, '  min_pq: ', min_pq, '  new_cand: ', new_cand)
            
            # min heap, max heap 길이 동일
            # 현재 단계에서 heap 안에 없는 값 3가지 비교
            # 이전 단계에서 찾은 중앙값 median, 이번에 탐색중인 arr[i], 새롭게 찾은 new_cand
            nums = sorted([median, arr[i], new_cand])
            #print('median, arr[i], new_cand? ',median, arr[i], new_cand)
            #print('nums: ', nums)
            # 양 끝 값 작은건 max heap, 큰건 min heap에 넣음
            heapq.heappush(max_pq, -nums[0])
            median = nums[1] # 중앙값은 heap에 넣지 않고 median에 기록
            heapq.heappush(min_pq, nums[2])
            
            print(median,end=' ')
            
    #print(pq)
    print()

for _ in range(t):
        
    m = int(input())
    arr = list(map(int,input().split()))
    
    find_median()
    


