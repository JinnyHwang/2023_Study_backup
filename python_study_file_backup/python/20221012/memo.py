
l1 = [2,4,6,3,5,4,2]
print(min(l1))

l2 = list( filter(lambda x: l1[x] == min(l1), range(len(l1))))
print(l2)

n = len(l1)
print(n)
for i in range(n):
    print(i, end=' ')
print('\n')
    
for i in reversed(range(n)):
    print(i, end=' ')
print('\n')

for i in range(n,0,-1):
    print(i, end=' ')
print('\n')

for i in range(n-1,-1,-1):
    print(i, end=' ')
print('\n')