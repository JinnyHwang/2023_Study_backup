#비어있는 리스트
list_test1 = list()
list_test1.append('a')
list_test1.append(1)
list_test1.append("apple")
list_test1.append(300)
print("list1 start : ")
for i in list_test1 :
    print("\t", i)
print("list_test1 is end!\n")

#범위값이 정해진 list
list_test2 = [x for x in range(2, 21, 2)]
for i2 in list_test2 :
    print(i2, end = '\t')
print("\nlist_test2 is end!! \n")

#이차원 list
list_test3 = [ [col for col in range(1, 4)] for row in range(3) ]

for index1, index2, index3 in list_test3 :
    print('[1]', "first", index1, "/", "second", index2, "/", "third", index3, sep = '\t')
    print("[2] first : %d / second : %d / third : %d \n" %(index1, index2, index3))
print("list_test3 Test1 is end! \n")


for col in list_test3 :
    for row in col :
        print(row, end = ' ')
    print('\n')
print("list_test3 Test2 is end! \n")


for y in range(6, 1, -1) :
    print(y, "\t", end='')
print("\ntest is end\n")






















