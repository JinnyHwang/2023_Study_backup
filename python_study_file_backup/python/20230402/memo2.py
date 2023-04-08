
from collections import deque

l = [1,2,3,4]
l2 = [5,6,7,8]
l3 = [-1,-2,-3,-4]

li = []
li.append(deque(l))
li.append(deque(l2))
li.append(deque(l3))
print(li)
print(li[0])
print(min(li[0]))


li2 = []
li2.append(l)
li2.append(l2)
li2.append(l3)
print(li2)
print(li2[0])
print(min(li2[0]))

'''
[deque([1, 2, 3, 4]), deque([5, 6, 7, 8]), deque([-1, -2, -3, -4])]
deque([1, 2, 3, 4])
1
[[1, 2, 3, 4], [5, 6, 7, 8], [-1, -2, -3, -4]]
[1, 2, 3, 4]
1
'''

li3 = []
li3.append(deque(map(int, input().split())))
print(li3)

li3[0].extend([10,11,12])
print('?',li3)

