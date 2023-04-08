
list1 = [37, 23, 10, 33, 29, 40]
print(list1)

#list1과 list2는 동일한 리스트
list2 = list1
print(list2)

#list1 내용을 copy
list3 = list(list1)
print(list3)

list1.append(16)
print(list1)
# list1 출력과 결과 동일
print(list2)

#list3은 이전과 결과값 동일
print(list3)

list4 = list3 + [16]
print(list4)

list5 = list1 + list3
print(list5)

n = 1
result = n in list5
print(result)

n2 = 16
if n2 in list5 :
    print('{}은 list에 있다'.format(n2))

del(list5[12])
print(list5)
list5.remove(33)
list5.remove(33)
print(list5)

for arr in list2 :
    print(arr)


