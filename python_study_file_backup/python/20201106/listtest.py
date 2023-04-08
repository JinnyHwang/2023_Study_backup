#비어있는 list
list_test1 = list()
list_test1.append('a')
list_test1.append(1)
list_test1.append('apple')
list_test1.append(300)
print("list1 start : ")
for test1 in list_test1 :
    print((test1))
print("list1 end!\n")


#범위 값이 정해진 list
list_test2 = [0 for i in range(10)]

print("list2 start : ")
for test2 in list_test2 :
    print((test2), end=' ')
print("list2 end!\n")


#3*3 이차원 list
list_test3 = [[0 for col in range(3)] for row in range(3)]
print("list3 start : ")
for index1, index2, index3 in list_test3 :
    print("%d %d %d" % (index1, index2, index3))
print("list3 end!\n")

print("list3 start : ")
for test3_1 in list_test3 :
    for test3_2 in test3_1 :
        print(test3_2, end=' ')
print("list3 end!\n")

print("list3 start : ")
#for 

print("list3 end!\n")


#range(A, B)는 A부터 B-1 값 까지 반환한다.
#range : 1, 2, 3, 4, 5
print("range1 start \n")
for j in range(1, 6) :
    print("%d " %(j))
print("range1 end!\n")


#증가폭 range 0번부터 시작해서 10까지 가는데  +2씩 증가
print("range2 start \n")
for x in range(0, 11, 2) : 
    print("%d " %(x))
print("range2 end!\n")


#range : 6, 5, 4, 3, 2, 1
print("range3 start \n")
for y in range(6, 0, -1) :
    print("%d " %(y))
print("range3 end!\n")


#감소폭 range 20번부터 시작해서 0까지 가는데 -2씩 감소
print("range4 start \n")
for z in range(20, -1, -2) :
    print("%d " %(z))
print("range4 end!\n")


#list_a = [3.14, 2.5, 6.767, 2.485, 1.3]

#list_a = list(map(int, a))

