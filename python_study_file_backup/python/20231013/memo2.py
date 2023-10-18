
import heapq

# 정수를 저장하는 최대 우선순위 큐 구현
class PriorityQueue():
    def __init__(self): # 빈 priority queue 생성
        self.items = []
        
    def push(self, item): # 우선순위 큐에 데이터 하나 추가
        heapq.heappush(self.items, -item)
    
    def empty(self): # 우선순위 큐 비어있으면 return 1
        if not self.items:
            return 1
        else:
            return 0
    
    def size(self): # 우선순위 큐 안에 있는 데이터 수 반환
        return len(self.items)
    
    def pop(self): # 우선순위 큐에 있는 데이터 중 최댓값에 해당하는 데이터 반환하고 제거함
        if self.empty():
            raise Exception('PriorityQueue is Empty')
        return -heapq.heappop(self.items)
        
    def top(self): # 최댓값 데이터를 알려줌 삭제 안함
        if self.empty():
            raise Exception('PriorityQueue is Empty')
        return -self.items[0]
        

n = int(input())
hq = PriorityQueue()

for _ in range(n):
    action = input()
    
    if 'push' in action:
        action,num = action.split()
        hq.push(int(num))
    elif 'pop' in action:
        print(hq.pop())
    elif 'empty' in action:
        print(hq.empty())
    elif 'size' in action:
        print(hq.size())
    elif 'top' in action:
        print(hq.top())
    else:
        print('input is wrong')















