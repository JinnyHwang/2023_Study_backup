
# 우선순위 큐
# 항상 우선순위가 가장 높은 데이터에만 관심이있고
# 이 데이터 먼저 나갈 수 있는 형태의 자료구조
# 배열, 연결리스트를 통해서도 구현 가능
# 그런데 힙을 사용해야 삽입,삭제 시간을 맞출 수 있다
# 힙을 사용해 우선순위 큐 구현
# python에서 제공하는 PriorityQueue class 사용하면 속도 너무 느려짐
# heapq를 사용!

# heapq는 기본적으로 min-heap이다
# max-heap으로 사용하려면 값에 -를 붙여서 관리하면 됨

import heapq

# make PriorityQueue
class PriorityQueue:
    def __init__(self): # 빈 priority queue 생성
        self.items = []
        
    def push(self, item): # 우선순위 큐에 데이터 하나 추가
        heapq.heappush(self.items, -item) # 최대값 순서대로
    
    def empty(self): # 우선순위 큐 비어있으면 return True
        return not self.items
    
    def size(self): # 우선순위 큐 안에 있는 데이터 수 반환
        return len(self.items)
    
    def pop(self): # 우선순위 큐에 있는 데이터 중 최댓값에 해당하는 데이터 반환하고 제거함
        if self.empty():
            raise Exception('PriorityQueue is empty')
        return -heapq.heappop(self.items) # 넣을 때 (-)붙여 넣어서 뺄 때 - 붙여서
    
    def top(self): # 최댓값 데이터를 알려줌 삭제 안함
        if self.empty():
            raise Exception('PriorityQueue is empty')
        return -self.items[0]

pq = PriorityQueue()
print(pq, pq.items)
pq.push(5)
print(pq, pq.items)
pq.push(2)
print(pq, pq.items)
pq.push(9)
print(pq, pq.items)
pq.push(-1)
print(pq, pq.items)

print('size: ',pq.size())
print(pq.top())
pq.pop()
print('size: ',pq.size())
while not pq.empty():
    print(pq.top())
    pq.pop()



