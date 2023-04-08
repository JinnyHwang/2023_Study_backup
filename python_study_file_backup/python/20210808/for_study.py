
for i in range(5) :
    print(i)
    
names = ['A', 'B', 'c', 'D']

for i in range(len(names)) :
    name = names[i]
    print('{}번 이름은 {}입니다.'.format(i+1, name))

# enumerate 사용시 enum, 인자값을 변수로 받을 수 있다
for i, name in enumerate(names) :
    print('{}번 {}'.format(i+1, name))


for i in range(11172) :
    print(chr(44032 + i), end=' ')


