
# 책에서는 다루지 않음
# 계산 복잡도 이론 P-NP 문제 풀어보기



# 한 번 계산한 문제는 다시 계산하지 않도록 하는 알고리즘
# 중복 연산 줄이기
# 다이나믹 프로그래밍(동적계획법)
# 탑다운(top down) / 보텀업(bottom up)
# 다이나믹 : 프로그램이 실행되는 도중에 라는 뜻
# 프로그램 실행 중 프로그램 실행에 필요한 메모리를 할당하는 기법


# 피보나치수열 : 두 항의 합을 현재의 항으로 설정하는 특징.
# n번째 피보나치수 = (n-1)번째 피보나치수 + (n-2)번째 피보나치수
# 1번째 피보나치 수 = 1, 2번째 피보나치 수 = 1

# 수열은 프로그래밍에서 리스트, 배열로 표현됨
# 수열 : 여러 개의 수가 규칙에 따라서 배열된 형태를 의미

def fibo_old(n) :
    if n == 1 :
        return 1
    elif n == 2 :
        return 1
    else :
        return fibo(n-1) + fibo(n-2)

#print(fibo(4))
# 재귀 호출로 구현할 경우 fibo(4)를 구하기 위해 fibo(3)이 3번 호출된다
# 재귀적으로 구현시 recursion depth 오류 발생할 수 있다
# sys 라이브러리에 포함된 setrecursionlimit() 사용시 재귀 제한 완화 가능함
# 파이썬의 최대 재귀 깊이는 1000으로 정의되어 있음
# 아래 code와 같이 최대 재귀 길이를 늘릴 수 있다
import sys
sys.setrecursionlimit(2000)
# x ** y : x의 y제곱 값



# 효율적인 구현을 위해 다이나믹 사용
# 메모제이션(캐싱) 사용

# 한 번 계산된 결과를 메모제이션 하기 위한 리스트 초기화
d = [0] * 100

# 피보나치 함수(fibonacci function) 재귀 함수로 구현(top down dynamic programing)
def fibo(x) :
    # 종료 조건
    if x == 1 or x == 2 :
        return 1

    if d[x] != 0 :
        return d[x]

    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(99))



# bottom up : 단순히 반복문을 이용하여 작은 문제부터 차근차근 답을 도출
# 앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 100

d[1] = 1
d[2] = 1
n = 99

for i in range(3, n+1) :
    d[i] = d[i-1] + d[i-2]

print(d[n])























