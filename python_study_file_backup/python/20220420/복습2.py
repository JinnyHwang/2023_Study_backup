


# a*b == yellow
# a+b = (brown/2)-2
    
# 가로(a) >= 세로(b)
# b는 1~n n의 값은 (yellow/b) 값 이상일 수 없음
# yellow%b == 0

def solution(brown, yellow):
    
    a = 1
    b = 1
    
    while True:
        
        if b > (yellow/b):
            break
        
        if yellow%b == 0:
            a = yellow//b
            if a+b == (brown/2)-2:
                return [a+2,b+2]
        b += 1
        continue
    
    else:
        print('개수 잘못기억했네')
        
        
b1 = 10
y1 = 2
print(solution(b1,y1))

b2 = 8
y2 = 1
print(solution(b2,y2))

b3 = 24
y3 = 24
print(solution(b3,y3))

















