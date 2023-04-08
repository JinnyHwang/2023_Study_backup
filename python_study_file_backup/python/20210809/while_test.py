
selected = None
while selected not in ['가위','바위','보']:
    selected = input('가위, 바위, 보 중 선택하세요 > ')

print('선택한 값은? :', selected)


patterns = ['가위','보','보']
length = len(patterns)
i = 0
while i < length :
    print(patterns[i])
    i = i+1

list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for val in list1:
    if val%3 == 0:
        print('== %3', val)
        break
    print('!= %3', val)

for i in list1:
    if i%2 == 0:
        continue
    print(i)

