
print(type(5))
print(isinstance(5, float))

numbers1 = []
print(type(numbers1))

numbers2 = list(range(10))
print(type(numbers2))

characters = list("Hello")
print(type(characters))

print(isinstance(numbers1,list))

#instance : characters, numbers1 같은 class로 정의한 data
#class : list, int 같은 type

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(id(list1))
print(id(list2))

if list1 is list2 :
    print("???")
else :
    print("!!!")

if list1 == list2 :
    print("value check")


