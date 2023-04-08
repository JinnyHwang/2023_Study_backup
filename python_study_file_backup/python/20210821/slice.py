
list1 = [0, 1, 2, 3, 4, 5]
print(list1[1])

text1 = "Hello World"
print(text1[2])

print(text1[1:5])

print(list1[1:5])
print(list1[0:2])
print(list1[:2])
print(list1[3:len(list1)])
print(list1[3:])
print(list1[:])

list1 = [2, 87, 154, 668, 254556, 0]

#list1과 주소 공유
list2 = list1
#list1의 값 복사
list3 = list1[:]
print(list2)
print(list3)

print(id(list1))
print(id(list2))
print(id(list3))

list3.sort()
print(list3)



