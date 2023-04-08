
#https://www.daleseo.com/python-heapq/

#import heapq
from heapq import heappush, heappop, heapify, nsmallest, nlargest

# heap에서는 가장 낮은(높은) 우선순위를 가지는 노트가 항상 루트에 위치
# min heap : 부모 노드 키값이 자식 노드 키값보다 항상 작은 힙
# max heap : 부모 노드 키값이 자식 노드 키값보다 항상 큰 힙

# 파이썬에서는 리스트를 힙처럼 사용할 수 있음
heap = []
heappush(heap, 4)
heappush(heap, 1)
heappush(heap, 7)
heappush(heap, 3)
heappush(heap, 8)
heappush(heap, 5)
print(heap)
'''
min heap
부모 노드는 항상 자식노드보다 작음
[1, 3, 5, 4, 8, 7] 처음부터 완전히 정렬되어 있지는 않음
       1 -----> root     
   3        5
4    8    7
'''

heappop(heap)
print(heap)
# [3, 4, 5, 7, 8]

heappop(heap)
print(heap)
# [4, 7, 5, 8]

heappop(heap)
print(heap)
# [5, 7, 8]

# heap에서는 원소가 삭제될 때 마다 원소 재배치가 일어난다

'''
최소값을 삭제하기 않고 접근하기
단 위에서 본 것 처럼 처음부터 완전히 정렬되어 있지 않고,
원소가 삭제될 때마다 원소 재배치가 일어나므로
heap[1]에 두 번째로 작은 원소가 저장되어 있지는 않다
인덱스로 읽어올 때는 root node를 알아볼 때만 사용할 수 있음
'''
print(heap[0])


# 기존 리스트를 힙으로 변환. 원본을 변환시킴
heap = [4, 1, 7, 3, 8, 5]
heapify(heap)
print(heap) # [1, 3, 5, 4, 8, 7]

nums = [4, 1, 7, 3, 8, 5]
heap_cp = nums[:]
heapify(heap_cp)
print(heap_cp) # [1, 3, 5, 4, 8, 7]
print(nums) # [4, 1, 7, 3, 8, 5]



# 응용 최대 힙
# 첫 번째 원소는 우선순위를 반전시키기 위한 용도
# 두 번째 원소를 value로 쓰면서 최대힙 구현할 수 있음
heap_max = []
for n in nums:
    heappush(heap_max, (-n,n))

print(heap_max)
# [(-8, 8), (-7, 7), (-5, 5), (-1, 1), (-3, 3), (-4, 4)]


# n번째 최소값/최대값
def nth_smallest(nums, n):
    heap = nums[:]
    heapify(heap)
    #for n in nums:
    #    heappush(heap, n)
        
    nth_min = None
    for _ in range(n):
        nth_min = heappop(heap)
    
    return nth_min

print(nth_smallest(nums, 2))

# 사실 이 역할을 하는 함수가 있음
# 가장 작은 3개 원소를 return
# [1, 3, 4]
print(nsmallest(3, nums))

# 3번째 작은 원소는?
# 4
print(nsmallest(3, nums)[-1])

# 가장 큰 원소?
# [8, 7, 5]
print(nlargest(3, nums))
# 5
print(nlargest(3, nums)[-1])


# 힙 정렬!
def heap_sort(nums):
    heap = nums[:]
    heapify(heap)
    
    '''
    heap = []
    for n in nums:
        heappush(heap,n)
    '''
    
    sorted_nums = []
    while heap:
        sorted_nums.append(heappop(heap))
        
    return sorted_nums

# [1, 3, 4, 5, 7, 8]
print(heap_sort(nums))


