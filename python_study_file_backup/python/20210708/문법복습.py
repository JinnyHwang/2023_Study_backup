
# DFS
visited = [False]*9
print( visited )

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]
print(graph)

def dfs ( graph, v, visited ) :
    visited[v] = True
    print(v, end=" " )

    for i in graph[v] :
        if not visited[i] :
            dfs( graph, i, visited )


# 한 줄에 여러 구문 사용 시 세미콜론 사용
dfs( graph, 1, visited ); print('\n')


# BFS
from collections import deque

visited = [False]*9

def bfs( graph, start, visited ):
    # queue 생성
    queue = deque()

    queue.append(start)
    visited[start] = True

    while( queue ) :
        node = queue.popleft()
        print(node, end=' ' )

        for i in graph[node] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True


bfs(graph, 1, visited)
print('\n')



# 선택 정렬 -  작은 값 순서
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]
print(array)

for i in range( len(array) - 1 ):
    min_index = i
    for j in range( i+1, len(array) ):
        if array[j] < array[min_index] :
            min_index = j

    if min_index != i :
        array[i] , array[min_index] = array[min_index] , array[i]

print('선택 정렬 : ', array)



# 삽입 정렬
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range( 1, len(array) ):
    for j in range( i, 0, -1 ) :
        if array[i] > array[j] :
            array[i], array[j] = array[j] , array[i]

print('삽입 정렬 : ', array)


# 배열 슬라이스
# https://dojang.io/mod/page/view.php?id=2208
arr = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

# 0 ~ 3 index 저장
arr2 = arr[0:4]
print(arr2, ', ', arr)

# 1~0 저장
arr3 = arr[1:1]

# 1 저장
arr4 = arr[1:2]
print('arr3 : ', arr3, ', arr4: ', arr4)


# -인덱스 : 2 ~ len(arr)-3
arr5 = arr[2:-3]
print(arr5)

# 인덱스 증가폭 : 1 ~ 5 내에서 2씩 증가하면서. 1, 3, 5
arr6 = arr[1:6:2]
print('arr6 : ', arr6)

arr7 = arr[5:]
print('arr7 : ', arr7)


arr8 = arr[5::2]
print('arr8 : ', arr8)

arr9 = arr[5:10:2]
print('arr9 : ', arr9)

# 리스트 전체
arr10 = arr[:] # = arr[::]
print('arr10 : ', arr10)

arr11 = arr[:10:3]
print('arr11 : ', arr11)

# 리스트 전체를 3씩 증가하면서
arr12 = arr[::3]
print('arr12 : ', arr12)


# 튜플에도 활용 가능
brr = (0, 10, 20, 30, 40, 50, 60, 70, 80, 90)
brr2 = brr[2::3]
print('brr2 : ', brr2)

# 연속된 숫자를 생성하는 range : 슬라이스
r = range(10)

# 슬라이스를 사용하면 range 객체가 만들어짐
r2 = r[1::3]
print('r2 : ', r2)

r3 = r[::2]
print('r3 : ', r3)


r4 = r[1:9]
print('r4 : ', r4)

print( 'r2 list : ', list(r2), ' , r3 list : ', list(r3), ' , r4 list : ', list(r4) )


# 문자열 슬라이스도 가능
str1 = 'Hello, world!'
str2 = str1[:10:2]
print('str2 : ', str2)


# slice 객체 사용하기 : 시퀀스 객체(시퀀스 자료형으로 만든 변수) 자를 수 있음
s1 = slice(2, 7) # index 2~6 자르는 슬라이스 객체
r5 = r[s1]
print('r5 : ', list(r5)) # r5 :  [2, 3, 4, 5, 6]

s2 = slice(1, 8, 2)
r6 = list(r[s2])
print('r6 : ', r6)

# 시퀀스객체.__getitem__(slice객체) 슬라이서 정의 대로 객체를 만들어줌
r7 = r.__getitem__(s2)
print('r7 : ', r7)

brr3 = brr.__getitem__(s2)
print('brr3 : ', brr3)


# 시퀀스 자료형이 뭐지?
# 각각의 요소들이 연속적으로 이어진 자료형
# 리스트, 튜플, range, 문자열


# 리스트 시퀀스 객체에 슬라이스 요소 할당하기
# 튜플, range, 문자열은 슬라이스 범위를 지정한 요소 할당을 할 수 없다.
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print('a : ', a)
a[2:5] = ['a', 'b', 'c'] #2~4 index 값 할당
print('a : ', a)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print('a : ', a)
a[2:5] = ['a'] #2~4index에 1개값 할당. 요소의 개수 줄어든다.
print('a : ', a)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print('a : ', a)
a[2:5] = ['a', 'b', 'c', 'd', 'e'] #2~4index에 5개값 할당. 요소의 개수 늘어난다.
print('a : ', a)

a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print('a : ', a)
a[2:8:2] = ['a', 'b', 'c'] #2, 4, 6index 값 할당.
# 이 경우 슬라이스 범위의 요소 개수와 할당 요소 개수가 정확하게 일치해야한다.
print('a : ', a)


# del로 슬라이스 삭제하기
a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print('a : ', a)
del a[2:5] #2~4 index 값 삭제
print('a : ', a)


a = [0, 10, 20, 30, 40, 50, 60, 70, 80, 90]
print('a : ', a)
del a[2:8:2] #2, 4, 6 index 값 삭제
print('a : ', a)




# 퀵 정렬 : 리스트의 맨 첫번째 원소가 pivot
# pivot value를 기준으로 왼쪽엔 작은 값, 오른쪽엔 큰 값 배치
array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]



pivot = array[0]


































