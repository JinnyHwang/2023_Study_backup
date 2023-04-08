
'''
알고리즘의 진해엥 따라 탐색해야 할 범위를 동적으로 결정함
피보나치 수열
f(n) = f(n-1) + f(n-2)

f(4) = f(3)             + f(2)
     = f(2)      + f(1) + f(1)+f(0)
     = f(1)+f(0) + f(1) + f(1)+f(0)
     
복잡도 : 지수함수 형태

DP : 중복계산 없애기
'''

d = [ 0 for _ in range(50)]
#print(d)

import time

def fibo(x):
    if x == 0 or x == 1:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]


for num in range(5, 40, 10):
    start = time.time()
    res = fibo(num)
    # round() 반올림함수
    print(res, '=> time: ', time.time() - start, 'sec')










