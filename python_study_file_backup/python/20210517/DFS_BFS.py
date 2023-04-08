
#push, pop

#stack
stack = []

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(7)
print(stack)
print(stack[::-1])
print("\n")

stack.pop()
print(stack)
print(stack[::-1])
print("\n")

stack.append(1)
stack.append(4)
print(stack)
print(stack[::-1])
print("\n")

stack.pop()
print(stack) #최하단 원소부터 출력
print(stack[::-1]) #최상단 원소부터 출력
print("\n")


#queue
from collections import deque

queue = deque()

queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue) #먼저 들어온 순서대로 출력
queue.reverse()
print(queue) #나중에 들어온 원소부터 출력

queue.reverse()
list_queue = list(queue) #deque를 list형으로 변환
print(list_queue)



#factorial

def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1, n+1):
        result *= i
    return result

def factorial_recursive(n):
    if n <= 1:
        return 1
    # n! = n * (n-1)!
    return n * factorial_recursive(n-1)

print('반복적으로 구현 : ', factorial_iterative(5))
print('재귀적으로 구현 : ', factorial_recursive(5))


# 인접 행렬 : 2차원 배열로 그래프의 연결관계를 표현하는 방식
# 인접 리스트 : 리스트로 그래프의 연결 관게를 표현하는 방식

# DFS : Depth First Search : 깊이 우선 탐색

INF = int(1e9)

# 2차원 리스트를 이용해 인접 행렬 표현
graph1 = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

graph = [[] for _ in range(3) ]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0, 5))

print(graph)




















