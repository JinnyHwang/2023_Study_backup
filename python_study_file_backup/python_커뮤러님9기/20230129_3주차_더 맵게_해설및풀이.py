
'''
힙 heap 사용

N개의 수 중에 가장 작은 것, 두 번째로 작은 것
새로운 스코빌지수 구하기
+ 효율성 테스트까지 함께

모든 스코빌 지수를 K이상으로 만들 수 없으면 -1 return

알고리즘 복잡도

- 최악의 경우
수가 하나 남을 때가지 섞어야 하는 경우 (n-1회)

- 각 단계(섞는 일)에서 요구되는 계산량
정렬된 리스트에 순서에 맞추어 원소 삽입
O(n) : 목록의 길이에 비례함

=> 전체 문제 풀이의 복잡도
n번의 단계를 거치는데, 한 단계가 n에 비례하기 때문
O(n^2)
=> 복잡도가 너무 높음!

더 좋은 방법은?

'최소/최대 원소를 빠르게 꺼낼 수 있는 자료구조' 사용
heap : 완전이진트리(complete binary tree)
max heap
min heap

연산
- 힙 구성(heapify) : O(logN) : N개 원소에 삽입하므로
- 삽입(insert) : O(logN) : heap의 크기가 2배가 되어도 반복 단계는 1증가. 4배 2증가.
- 삭제(remove) : O(logN)

heap의 구조
root node를 기준으로 right/left
완전이진트리는  배열을 이용해서 구현 가능하다!
index로 child, parent node를 찾아갈 수 있다. 공간 효율성이 높음

힙 응용

정렬(heapsort)
빈 heap을 만들고 모든 원소를 삽입. O(NlogN)
최대, 최소 찾으며 remove. O(NlogN)에 비례

우선 순위 큐(priority queue)
큐에 들어갈 때는 무작위로 들어가도,
큐에서 나올 때 우선순위에 따라 나오는 것
'''
'''
# 사용 예시
import heapq

L = [1,3,5]

# 리스트 L로 부터 min heap을 구성한다
# 리스트의 index로 접근할 수 있음. 구성 방식이 heap으로 바꼈을 뿐
heapq.heapify(L)

m = heapq.heappop(L) # min heap L에서 최소값 삭제(반환). O(logN)

heapq.heappush(L, 2) # min heap L에 원소 삽입. O(logN)
'''

# 문제 풀이
import heapq

def solution(scoville, K):
    answer = 0
    
    heapq.heapify(scoville)
    
    while True:
        min1 = heapq.heappop(scoville)
        
        # 가장 작은 값이 K를 넘으면 모든 음식의 스코빌 지수가 K를 넘는 것
        if min1 >= K:
            break
        # 마지막 남은 원소가 K값을 넘지 못한다면 return -1
        elif len(scoville) == 0:
            answer = -1
            break
        
        min2 = heapq.heappopo(scoville)
        new_s = min1 + min2*2
        heapq.heappush(scoville, new_s)
        answer += 1
    
    return answer


# 최대 힙 max heap은 어떻게 구할까?
nums = [4, 1, 7, 3, 8, 5]
heap = []

for n in nums:
    # heappush 할 때 (a,b)를 node 원소로 push
    # node의 a기준으로 정렬됨
    # b값을 확인하면 min heap을 max heap처럼 사용할 수 있는 것
    heapq.heappush(heap, (-n, n))

while heap:
    #print(heapq.heappop(heap)) # (-8, 8)
    print(heapq.heappop(heap)[1]) # 원소로 쓸 값을 print



