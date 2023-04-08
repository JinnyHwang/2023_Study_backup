
# <<스택>>
stack = []

stack.append(5)
print(stack)
stack.append(2)
print(stack)
stack.append(8)
print(stack)
stack.append(7)
print(stack)
stack.pop()
print(stack)
stack.append(3)
print(stack)
stack.pop(0) # 큐 같이 사용할 수 있음
print(stack)

# 최상단 원소부터 출력
print(stack[::-1])



# <<큐>>
# Queue 구현을 위해 deque 라이브러리 사용
# 데크(deque)는 스택과 큐 기능을 둘 다 가진 객체. 출입구를 양쪽에서 사용 가능.
# append(), pop()은 오른쪽에서 추가, 삭제
# 스택 구현 : append(), pop()
# 큐 구현 : appendleft(), pop() / append(), popleft()
# 큐는 왼쪽 추가 시 오른쪽 삭제 / 오른쪽 추가 시 왼쪽 삭제
#  queue = deque([1, 2, 3]) : deque 인자로 리스트를 쓰면 deque화 시켜준다
from collections import deque

queue = deque()

queue.append(5)
print(queue)
queue.append(2)
print(queue)
queue.append(8)
print(queue)
queue.popleft()
print(queue)
queue.append(7)
print(queue)

queue.reverse() # 역순으로 바꾸기
print(queue)


# <<재귀 함수>>

# 1. 무한 재귀 함수
#def recursive_function() :
#    print('재귀 함수 호출')
#    recursive_function()
#recursive_function()

# 2. 조건문 stop
def recursive_function(i) :
    if i == 10 :
        return
    print(i, '번째 재귀 함수에서 ', i+1, "번째 재귀 함수를 호출합니다")
    recursive_function(i+1)
    print(i, '번째 재귀 함수 종료')
    
recursive_function(1)

# 가장 마지막에 호출한 함수가 먼저 수행을 끝내야
# 앞에 호출한 함수 호출이 종료된다.

# 3. n! 팩토리얼 재귀함수
def factorial_iterative(n) :
    result = 1
    # 1부터 n까지 수를 차례대로 곱하기
    for i in range(1, n+1) :
        result *= i
    return result

def factorial_recursive(n) :
    print(n, '번째 재귀 함수 in!')
    if n <= 1 :
        return 1

    print(n, '번째 재귀 함수 out!')
    # n! : n*(n-1)!
    return n*factorial_recursive(n-1)

print('반복적 : ', factorial_iterative(5))
print('재귀적 : ', factorial_recursive(5))















