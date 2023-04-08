
sy = 3
sx = 5

dy = 7
dx = 2

[y1, y2] = lambda x : sy, dy if sy < dy else dy, sy
x1, x2 = lambda x : sx, dx if sx < dx else dx, sx

print("y1:{}, y2:{}, x1:{}, x2:{}".format(y1, y2, x1, x2))



a1 = -1
b1 = -1

if [a1, b1] == [-1, -1]:
    print("@#@#")

a = [-1, -1]

if a == [-1,-1]:
    print("!!")
else :
    print("??")


# 메모리할당?
# C언어에서 사용하는 call by value, call by reference 아님
# pass by assignment

def aaa(a):
    print('a1:',a, id(a)) # a1: 0 1742268912 # call한 func의 매개변수 주소값과 동일
    a += 1
    print('a2:',a, id(a)) # a2: 1 1742268928 # 해당 func에서 작업 시 값이 새로운 메모리로 할당됨
    return a

def bbb(b):
    list1 = []
    list1.append(b)
    list1.append(b)
    print(list1, id(list1), id(list1[0])) # [0, 0] 54410496 1742268912
    list1[0] = aaa(list1[0]) # 새롭게 할당된 메모리로 list1[0] 주소값이 변경
    print(list1[0], id(list1[0])) # 1 1742268928
    print(list1, id(list1), id(list1[0])) # [1, 0] 54410496 1742268928 # list1의 주소값은 동일


bbb(0)



# 입출력 방식 익히기
a, b, c = map(int, input().split())
print('??:',a, b, c)

#n = int(input())
#n = 5
n = int(input())
list1 = []

for _ in range(n):
    list1.append( list( map(int, input().split()) ) )

#list1 = [ [0]*n for _ in range(n) ]
#for i in list1:
#    i = list( map(int, input().split()) )

#list1 = [ [ 0 for _ in range(n) ] for _ in range(n)]
#data = list(map(int, input().split()))
print(list1)


