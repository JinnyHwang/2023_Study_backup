
from copy import deepcopy

a = 0.02
b = 10
print(a*b)
print(int(a*b))



l = [[1,2],[3,4],[5,6],[7,8]]
l2 = [[4,4,4],[5]]

l3 = reversed(l[1])
print(l3)

l = deepcopy(l2)
l2 = []

print(l)
print(l2)

#for x,y in l:
#    x, y = -1,-1

for i, v in enumerate(l):
    l[i] = [-1,-1]
    
print(l)



if [1,2] in l:
    print('a')
else:
    print('b')
    

if [2,3] in l:
    print('a')
else:
    print('b')
    








