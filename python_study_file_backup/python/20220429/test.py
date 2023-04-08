
num = [1, 2, 3, 4 , 5]
fruit = ['apple', 'banana', 'orange', 'airplane']
color = ['red', 'yellow', 'orange']

# 입력받은 인자 값의 개수 중 최소 갯수를 받아서 묶어서 튜플로 보내줌
# list로 변환하지 않으면 zip object 주소값이 출력됨
# <zip object at 0x034A6EB8>
l3 = list(zip(num, fruit, color))
print(l3)
# [(1, 'apple', 'red'), (2, 'banana', 'yellow'), (3, 'orange', 'orange')]



l1 =  [[2, 3, 1, -2, -1, 2], [2, -1, 4, -2, -2, 3], [3, 0, 4, -2, -2, 1],
       [-1, 4, -1, -2, -2, 4], [3, -1, -2, 0, 3, 3], [1, -2, 4, 1, 3, 1]] 
print('list\n',l1)

tmp = []
# 시계로 돌리는 효과
for item in zip(*l1):
    #print(item)
    tmp.append(list(reversed(item)))
print('tmp\n',tmp)

tmp3 = []
# 반시계로 돌리는 효과
for item in zip(*l1):
    #print(item)
    tmp3.append(list(item))
tmp3.reverse()
print('tmp3\n',tmp3)
'''
list
 [[2, 3, 1, -2, -1, 2], 
[2, -1, 4, -2, -2, 3], 
[3, 0, 4, -2, -2, 1],
[-1, 4, -1, -2, -2, 4], 
[3, -1, -2, 0, 3, 3], 
[1, -2, 4, 1, 3, 1]]

tmp
 [[1, 3, -1, 3, 2, 2], 
[-2, -1, 4, 0, -1, 3], 
[4, -2, -1, 4, 4, 1], 
[1, 0, -2, -2, -2, -2],
[3, 3, -2, -2, -2, -1], 
[1, 3, 4, 1, 3, 2]]

tmp3
 [[2, 3, 1, 4, 3, 1], 
[-1, -2, -2, -2, 3, 3], 
[-2, -2, -2, -2, 0, 1], 
[1, 4, 4, -1, -2, 4], 
[3, -1, 0, 4, -1, -2],
 [2, 2, 3, -1, 3, 1]]
'''


# * 별표의 의미는?
# unpack을 의미: list나 튜플을 풀어주는 것
# 만약 별표가 2개면 딕셔너리를 unpack하는걸 의미함

print( '??: ',list( zip(l1) ) )
# [([2, 3, 1, -2, -1, 2],), ([2, -1, 4, -2, -2, 3],), ([3, 0, 4, -2, -2, 1],), ([-1, 4, -1, -2, -2, 4],), ([3, -1, -2, 0, 3, 3],), ([1, -2, 4, 1, 3, 1],)]

'''
([2, 3, 1, -2, -1, 2],)
([2, -1, 4, -2, -2, 3],)
([3, 0, 4, -2, -2, 1],)
([-1, 4, -1, -2, -2, 4],)
([3, -1, -2, 0, 3, 3],)
([1, -2, 4, 1, 3, 1],)
'''
# 시계로 돌리는 효
for item in zip(l1):
    print(item)
    tmp.append(list(reversed(item)))

print( '!!: ',list( zip(*l1) ) )
# [(2, 2, 3, -1, 3, 1), (3, -1, 0, 4, -1, -2), (1, 4, 4, -1, -2, 4), (-2, -2, -2, -2, 0, 1), (-1, -2, -2, -2, 3, 3), (2, 3, 1, 4, 3, 1)]


'''
[[2, 3, 1, -2, -1, 2], 
[2, -1, 4, -2, -2, 3], 
[3, 0, 4, -2, -2, 1],
 [-1, 4, -1, -2, -2, 4], 
[3, -1, -2, 0, 3, 3], 
[1, -2, 4, 1, 3, 1]]
'''
'''
(2, 2, 3, -1, 3, 1)
(3, -1, 0, 4, -1, -2)
(1, 4, 4, -1, -2, 4)
(-2, -2, -2, -2, 0, 1)
(-1, -2, -2, -2, 3, 3)
(2, 3, 1, 4, 3, 1)
'''
'''
[1, 3, -1, 3, 2, 2]
[-2, -1, 4, 0, -1, 3]
[4, -2, -1, 4, 4, 1]
[1, 0, -2, -2, -2, -2]
[3, 3, -2, -2, -2, -1]
[1, 3, 4, 1, 3, 2]
'''
for item in zip(*l1):
    #print(item)
    print(list(reversed(item)))
    tmp.append(list(reversed(item)))

print(tmp)

tmp2 = []
for item in zip(*l1[::-1]):
    tmp2.append(list(reversed(item)))
print('tmp2\n',tmp2)


r = len(l1[0])
c = len(l1)

tmp3 = [ [0]*c for _ in range(r) ]
print(tmp3)
# 반시계로 돌리는 효과
for item in zip(*l1):
    #print(item)
    tmp3.append(list(item))
tmp3.reverse()
print('tmp3\n',tmp3)

# zip()은 입력받은 인자를 묶어줌
# zip은 zip object를 return하기 때문에 형변환이 필요람
# *는 리스트, 튜플을 풀어줌
# *없이 zip()후 list로 변환하면 [[]] 이중리스트 형태가 됨
# zip(*list)해서 reverse를 사용하면
# 리스트 안에 있는 원소들을 원하는대로 묶고 해지할 수 있어서
# 리스트를 회전시키거나 뒤집는 것 처럼 만들 수 있다

# 예를들어서 zip(*list[::-1])
# 리스트를 뒤에서부터 탐색해서 append하면?
# 뒤에 원소가 윗줄에 오는 효과를 볼 수 있다.


m = [[-2, -2, 2, 1, 1], [-2, -2, 1, 3, -1], [2, -2, 2, 2, 2], [-1, -2, -2, -2, 2], [-2, 2, -2, -2, 1]] 
#print(m)

#for r in range(5):
#    for c in range(5):
#        print(m[0][c])
#        print(m[1][c])
#        print(m[2][c])
#        print(m[3][c])
#        print(m[4][c])



l1 = [[1, 3], [2, 0], [2, 1], [2, 2], [2, 3], [3, 2]]
#print(l1)
l1.sort()
#print(l1)


l = []

#print(l)

#if not l:
#    print('a')
#else:
#    print('b')

l.append(2)
#print(l)

#if not l:
#    print('aa')
#else:
#    print('bb')

a = l.pop()

#if not l:
#    print('aaa')
#else:
#    print('bbb')

#print(a)

