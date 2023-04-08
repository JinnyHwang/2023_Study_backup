
K, P, N = map(int, input().split())

dev = 1000000007

# N은 최대 10^16 O(N) 시간초과가 날 수 밖에 없다
# K * P^(10*N)
# P^(10^16) 가장 큰 수 : O(logN) 하면 16*log10 약 128 가능!
# P^(10*N)을 어떻게 계산할까? 같은 계산을 줄이자
def f(num, cnt):
    
    if cnt == 1:
        return num
    elif cnt == 2:
        return num*num
    
    if cnt%2 == 0:
        temp = f(num, cnt/2)
        return (temp*temp)%dev
        #return f(num, cnt/2)*f(num, cnt/2)
    else:
        temp = f(num, cnt//2)
        return (temp*temp*num)%dev
        #return f(num, cnt//2)*f(num, cnt//2)*num

answer = (K*f(P, 10*N))%dev
print(answer)
'''
for _ in range(N*10):
    K *= P
    if K > dev:
        k %= dev
print(K)
'''
