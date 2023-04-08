
list1 = [135, 462, 27, 2753, 234]
print(list1.index(27))
#print(list1.index(50))

if 50 in list1 :
    print(list.index(50))

list2 = [1, 2, 3] + [4, 5, 6]
print(list2)

list1.extend([9, 10, 11])
print(list1)

list1.insert(2, 999)
print(list1)

#index에서 -1은 뒤에서 첫 번째.
#가장 마지막 index에 9999를 넣고
#해당 index에 있던 값은 오른쪽으로 밀림
list1.insert(-1, 9999)
print(list1)

#print(list1[1000])

list1.insert(10000, 555)
print(list1)

list1.sort()
print(list1)

list1.reverse()
print(list1)
