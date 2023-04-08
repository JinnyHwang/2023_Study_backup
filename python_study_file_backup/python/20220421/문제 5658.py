
# int(value, base)
# base는 10이 디폴트
# base로 2~36 입력 가능
# print(int('1a',16))
# 와... 파이썬은 int(valuse, base) 만 알아도
# 8진수 16진수 문제 없다...

# join()
# '구분자'.join(리스트)
# 매개변수로 받은 리스트에 있는 요소를 하나하나 합쳐서 문자열로 변환
# temp = int(''.join(A[i:i+turn]), 16)

T = int(input())
result = [ 0 for _ in range(T) ]
for test_case in range(1, T + 1):
    N, K = map(int, input().split())
    #A = list(input())
    A = input()
    AA = A*2
    turn = N//4
    
    s1 = set()
    
    for i in range(0, N):
        # 리스트를 slice해서 문자열로 변환 후 16진수로 변경
        temp = int(AA[i:i+turn],16)
        #print(temp)
        s1.add(temp)
    result[test_case-1] = sorted(s1, reverse=True)[K-1]
        
    #ll = sorted(s1, reverse=True)
    #print(ll)
    
    print('#{} {}'.format(test_case, sorted(s1, reverse=True)[K-1]))
            







T = int(input())

result = [ 0 for _ in range(T) ]

for test_case in range(1, T + 1):

    N, K = map(int, input().split())
    s = input()
    ss = s*2
    l = N//4
    
    def hexa(ss, l):
        result = 0
        a = 0
        for i in range(l):
            try:
                a = int(ss[i])*(16**(l-i-1))
            except:
                a = (9+ (ord(ss[i]) - ord('A') + 1) )*(16**(l-i-1))
            result += a
        return result
    
    re = set()
    for i in range(N):
        re.add(hexa(ss[i:i+l],l))
        
    list1 = sorted(re, reverse=True)
    result[test_case-1] = list1[K-1]
     
for i in range(T):
    print('#{} {}'.format(i+1, result[i]))






def test():

    T = int(input())



    for _ in range(T):
        
        N, K = map(int, input().split())
        s = input()
        
        ss = s*2
        print(ss)
        
        # ss 문자열 0 ~ N+(N/4) 탐색
        
        l = N//4
        print(l)
        
        def hexa(ss, l):
            result = 0
            a = 0
            for i in range(l):
                #print('? : ',i, ss[i])
                try:
                    #print('...? : ',int(ss[i]), (16**i))
                    a = int(ss[i])*(16**(l-i-1))
                except:
                    #print('!', ss[i] , ' : ',ord(ss[i])-ord('A')+1)
                    #print('...? : ',(9+ (ord(ss[i]) - ord('A') + 1) ) ,(16**i))
                    a = (9+ (ord(ss[i]) - ord('A') + 1) )*(16**(l-i-1))
                result += a
                #print(a, result)
            return result
        
        # re = {} 이건 dictionary로 인식
        re = set()
        
        for i in range(N):
            #print( '!!! : ',ss[i:i+l], ' : ', hexa(ss[i:i+l],l))
            re.add(hexa(ss[i:i+l],l))
        
        #print(re)
        list1 = sorted(re, reverse=True)
        #print(list1, list1[K-1])
        
        
        # 문자열 slice
        
        
        # set으로 저장
        # 값은 10진수로 저장
        













