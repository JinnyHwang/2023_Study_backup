
#이진 탐색 복습
def binary_search(array, target, start, end) :
    while start <= end :
        mid = (start+end) // 2

        if array[mid] == target :
            return mid
        elif array[mid] > target :
            start = mid + 1
        else :
            end = mid - 1
    return mid


# set() 중복이 없는 요소들로만 구성된 집합 컬렉션
# set은 {}을 사용해 컬렉션을 표현함.
mylist = ['A', 'A', 'A', 'B', 'B']
myset = {'A', 'B'}

# set은 집합 연산이 가능하다
a = {1, 2, 3}
b = {3, 4, 5}

#교집합
i1 = a & b
i2 = a.intersection(b)

#합집합
u1 = a | b
u2 = a.union(b)

#차집합
d1 = a - b
d2 = a.difference(b)


# 집합 자료형 이용
n = int(input())
array = set(map(int, input().split()))

m = int(input())
x = list(map(int, input().split()))

for i in x :
    if i in array :
        print('yes', end=' ')
    else :
        print('no', end=' ')










