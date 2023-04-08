
'''
가장 맵게!

모든 음식의 스코빌 지수를 k이상으로 만들기

가장 작은 스코빌지수를 가지는 음식을 섞고 정렬
섞는 횟수 count
=> 시간 복잡도 최악 O(n^2)

heap
최대, 최소 원소를 빠르게 꺼낼 수 있는 자료구조
max heap
min heap

힙은 완전이진트리로 구현

힙 구성
heapify

삽입   O(logN)
insert

삭제   O(logN)
remove


힙 응용

정렬
heapsort

우선순위큐
priority queue
'''

import heapq

L = [2,5, 11]
x = 1

# 접미사 -ify
# justify classify specify simplify
heapq.heapify(L) #리스트 L로부터 min heap 구성

m = heapq.heappop(L) #min heap L에서 최소값 삭제(반환)
heapq.heappush(L, x) #min heap L에 원소 x 삽입


def solution(scoville, k):
    answer = 0
    print(scoville)
    
    #datatype 변화 없이 heap 형식으로 정렬
    heapq.heapify(scoville)
    
    print(scoville)
    while True:
        min1 = heapq.heappop(scoville)
        
        if min1 >= k:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        
        min2 = heapq.heappop(scoville)
        new_scoville = min1 + min2*2
        heapq.heappush(scoville, new_scoville)
        print(scoville)
        answer += 1
    
    print(answer)
    return answer

#s1 = [1, 2, 3, 9, 10, 12]
s1 = [1, 12, 9, 2, 10, 3]
k1 = 10
solution(s1, k1)

#import heapq

# heap: 최대/최소 원소를 빠르게 꺼낼 수 있는 구조 (완전이진트리형식)
def solution2(scoville, k):
    
    heapq.heapify(scoville)
    
    answer = 0
    while True:
        
        min1 = heapq.heappop(scoville)
        
        if min1 >= k:
            break
        elif len(scoville) == 0 :
            answer = -1
            break
        
        min2 = heapq.heappop(scoville)
        new_s = min1 + min2*2
        heapq.heappush(scoville, new_s)
        answer += 1
    
    return answer
    
    
    












