
# round() : 특정 자릿수에서 반올림하는 함
a = 0.123 + 0.22
print(a)
print(round(a,3))

# 거듭제곱
print(5**3)  #125

# 리스트 초기화
a = [0]*10
print(a) # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

# 인덱싱 슬라이싱
# 슬라이싱의 3번째 원소는 step. 몇개씩 끊어서 가져올까
# step이 양수면 오른쪽으로 이동하면서 가져옴
# step이 음수면 왼쪽으로 이동하면서 가져옴
a1 = [ i for i in range(10)]
print(a1)        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(a1[-1])    # 9 
print(a1[1:5])   # [1, 2, 3, 4]
print(a1[:3])    # [0, 1, 2]
print(a1[:3:-1]) # [9, 8, 7, 6, 5, 4]
print(a1[:3:2])  # [0, 2]
print(a1[2::-1]) # [2, 1, 0]

# 특정 크기의 2차원 리스트 초기화
n = 3
m = 4

# 잘못된 방법
arr1 = [[0]*m]*n
print(arr1) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
arr1[1][1] = 5
print(arr1) # [[0, 5, 0, 0], [0, 5, 0, 0], [0, 5, 0, 0]]
# 내부적으로 이 3개 리스트가 모두 동일한 객체에 대한 3개 레퍼런스로 인식됨

# 위와 같은 경우를 방지하기 위해선 리스트 컴프리헨션을 이용해야한다
arr2 = [ [0]*m for _ in range(n) ]
print(arr2) # [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
arr2[1][1] = 5
print(arr2) # [[0, 0, 0, 0], [0, 5, 0, 0], [0, 0, 0, 0]]

# 리스트 메서드
l = [ i for i in range(1,10)]
print(l)

l.append(10)
print(l)

l.insert(2, 333)
print(l)

l.sort(reverse=True)
print(l)

l.insert(4,-30)
print(l)

l.reverse()
print(l)

l.remove(333)
print(l)

l.append(3)
print(l.count(3))


# remove set
a = [ i for i in range(1,6)]
a.append(5)
a.append(5)
print(a)

remove_set = {3,5}

# 문법 자연스럽게쓸 수 있게 하자
result = [ i for i in a if i not in remove_set ]
print(result)


# 한 번 선언된 값을 수정할 수 없는 튜플
a = (1, 2, 3, 4)
print(a)
# a[1] = 22 # Error!

# dictionary
a = {1:[0,2,3], 2:[333,444,555], 'a':3}
print(a)

for i, v in a.items():
    print(i,v)
    try:
        for vi, vv in enumerate(v):
            print(vi, vv)
    except:
        print(v)

# 집합 자료형
data = [i for i in range(1,6)]
data.insert(0,1)
print(data)
print(set(data))
data = {1,1,1,1,1,1,3}
print(data)

a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7}
print(a|b) #합집합
print(a&b) #교집합
print(a-b) #차집합

a.add(6)
b.update([10,11])
a.remove(3)
print(a,b)

'''
주요 라이브러리
내장함수: input() print()
itertools : 순열, 조합 라이브러리. 반복되는 형태 데이터를 처리하는 기능을 제공.
heapq : 힙. 우선순위 큐 기능
bisect : 이진탐색
collections : deque(덱), counter(카운터)
'''




# 실수가 저장된 리스트가 있을 때 이 리스트의 모든 요소를 정수로 변환하려면?
a = [1.1, 2.2, 3.3, 4.4, 5.5]
b = list(map(int, a))
print(a, '\n', b)

n = int(input())

# map() 리스트의 요소를 지정된 함수로 처리해주는 함수
# 원본 리스트를 변경하지 않고 새 리스트를 생성한다
data = list( map( int, input().split()) )
print(sorted(data))

a, b, c = map(int, input().split(','))
print(a,b,c)

'''
import sys
data = sys.stdin.readline().rstrip()
'''










