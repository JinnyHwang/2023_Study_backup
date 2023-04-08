
n = int(input())

if (n>100) or (n<1) :
    print('숫자 잘못입력!')
    quit()

# input().split() 결과는 문자열 리스트
walk_list = input().split()
# walk_int = map(int, walk) #리스트 요소를 int로 변환
# a, b, c = walk_int # 맵 객체는 변수 여러개에 저장할 수 있음.

#map1 = list( (0 for x in range(n)) for y in range(n) ) -> 틀린답!
#map1 = [ [0 for x in range(n)] for y in range(n) ]

map1 = [1, 1]

L = [ 0, -1]
R = [ 0,  1]
U = [-1,  0]
D = [ 1,  0]

# 1 <= map1[0], map1[1] <= n

x = 0
y = 0

for walk in walk_list :

    x = 0
    y = 0

    if walk == 'L' :
        x = L[0]
        y = L[1]
        
    elif walk == 'R' :
        x = R[0]
        y = R[1]
        
    elif walk == 'U' :
        x = U[0]
        y = U[1]
        
    elif walk == 'D' :
        x = D[0]
        y = D[1]
        
    else :
        print('틀렸어!')
        quit()

    if ((1 > (map1[0] + x)) or (n < (map1[0] + x))) or \
       ((1 > (map1[1] + y)) or (n < (map1[1] + y))) :
       # print('무시! ', map1[0], map1[1], x, y)
        continue
    else :
        map1[0] += x
        map1[1] += y
       # print('결과! ', map1[0], map1[1])
        

print( map1[0], map1[1] )
