
'''
힙 heap
효율성테스트를 해야함

알고리즘 복잡도
- 최악의 경우 : 수가 1개 남을 때가지 섞어야하는 경우 (n-1)회
- 각 단계에서 요구되는 계산량
  정렬된 리스트 순서에 맞춰 원소 삽입.
문자길이 비례 O(n)
--> 전체 문제 풀이 복잡도 : O(n^2)
지나치게 높음

가장 효율적인 계산은?
heap - 최대/최소 원소를 빠르게 찾을 수 있음
상수 시간에 원소중 가장 큰거, 가장 빠른거 찾을 수 있음
max heap : 최대 원소를 빠르게 꺼내는 자료구조
min heap : 최소 원소를 빠르게 꺼내는 자료구조

힙 구성(heapify) : 하나의 원소를 삽입하는데 logN. n개원소 O(NlogN)
삽입(insert)
삭제(remove)

원소가 n개일 때 삽입, 삭제연산은 O(logn)
log에 비례하는 복잡도를 가짐

힙의 구현
root node 존재 가장 큰 수
완전 이진 트리 (complete binary tree)
-> 배열을 이용해 구현 가능
배열에 넣어서 index를 가지고 child node, parent node를 찾을 수 있는 성질
공간효율성이 높음

!!!heapsort 정렬!!!
임의의 순서로 수가 주어졌을 때
빈 heap에 모든 원소 삽입(NlogN)
최대원소, 최소원소 remove(NlogN)

!!!우선 순위 큐(priority queue)!!!
fifo이 아닌
우선순위대로 접근 가능 -> 여기서는 스코빌지수
'''

'''
파이썬 힙 라이브러리 사용
import heapq (priority queue 성질을 가지고 있기 때문)
heapq.heapify(L) : 리스트 L로부터 min heap 구성
리스트에 L에 어떤 순서로 구성되어 있든간
min heap으로 리스트를 구성한다
리스트 인덱스로 노드 위치 알 수 있음

m = heapq.heappop(L)
min heap L에서 최소값 삭제, 반환

heapq.heappush(L, x)
min heap L에 원소 x삽입

(+) max heap 만들기1
heapq.heappush(h, -itme)
ha = heapq.heappop(h) * (-1)
(+) max heap 만들기2
# 우선순위는 -값으로 실제로 넣는 값은 원래값으로
heapq.heappush(h, (-itme, item))
             우선순위기준, 넣는값


---> min heap 구조 유지
어떤 자료구조를 사용해야하는지 파악하면
어려운 부분은 라이브러리가 다 해주는구나
각 자료형 사용 방법 익히고
효율적인 문제 풀이 방법을 찾자

이 문제 물론 리스트로 풀 순 있음
그런데 NlogN vs N^2
힙을 이용하는 것이 훨씬 효율적

리스트 datatype을 sort처럼 정렬하는 것
heapq.heapify(scoville)의 의미는
리스트 scoville을 min heap으로 정렬하겠다는 의미임
datatype 변화 없이 리스트

heapq.heapify(listForTree)             # for a min heap
heapq._heapify_max(listForTree)        # for a maxheap!!
'''

# heapq.heapify(L)  #min heap으로 정렬
# heapq._heapify_max(L)  #max heap으로 정렬
# heapq.heappush(L, item)
# heapq.heappush(L, (-itme, item))  #-item기준으로 위치지정, item값 넣기 : max heap

import heapq

def solution(scoville, K):
    answer = 0
    # 리스트를 min heap 정렬
    # 연산이 끝나는 조건
    # 1. 남아있는 원소중 가장 작은 값이 k 이상일 때
    # 2. 힙에 남아있는 값이 1개일 때
    # return 연산 횟수
    # 반복적으로 음식을 섞어야함
    
    # min heap으로 정렬
    heapq.heapify(scoville)
    
    while True:
        print(scoville)
        min1 = heapq.heappop(scoville)
        
        if min1 >= K:
            break
        elif len(scoville) == 0:
            answer = -1
            break
        else:
            min2 = heapq.heappop(scoville)
            new = min1 + (min2*2)
            heapq.heappush(scoville, new)
            answer += 1
    
    return answer


solution([1, 2, 3, 9, 10, 12], 7)

















