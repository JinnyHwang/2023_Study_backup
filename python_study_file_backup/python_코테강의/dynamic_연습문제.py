
'''
동적계획법 (Dynamic Programming)
문제에 답인지 확인하기 위해
탐색해야하는 범위(soultion dpace)를 어떤 부분을 탐색하는가를
진전하면서 동적으로 탐색하는 것

주어진 최적화 문제를
재귀적 방식으로 작은 부분으로 문제를 나눠
부분 문제를 풀어서, 이 해를 조합하여
전체 문제의 해답에 이르는 방식

알고리즘의 진행에 따라
탐색해야할 범위를 동적으로 결정
탐색 범위를 한정할 수 있다

동적계획법 적용 예
- 피보나치수열
직전 두 항의 합이 다름 수가 되는 수열

재귀함수의 대표적인 예
f(4) = f(3)               + f(2)
     = f(2)        + f(1) + f(1) + f(0)
     = f(1) + f(0) + f(1) + f(1) + f(0)
-> 복잡도 : 지수함수 형태로 나타남

동적계힉법 적용?
f(0) = 0 ,  f(1) = 1
f(2) = f(1)+f(0) = 1
f(3) = f(2)+f(1) = 2
f(4) = f(3)+f(2) = 3
-> 복잡도 : 선형함수의 형태 (주어진 수에 비례)
'''
def fibo_old(n):
    if n == 0 or n == 1:
        return n
    else :
        return fibo_old(n-1) + fibo_old(n-2)

l = [0 for i in range(100)]
def fibo(n):
    if n == 0 or n == 1:
        l[n] = 0
        return n
    else :
        if l[n] != 0:
            return l[n]
        else:
            l[n] = fibo(n-1) + fibo(n-2)
            return l[n]

'''
!!! 적용 예 !!!
Knapsack Problem
가장 높은 값을 가지도록
물건을 골라 배낭에 담아라

weight = [3, 4, 5, 6]
value = [6, 8, 12, 13]

i : 물건번호 , w : 최대 넣을 무게
Val(i, w) = (w >= weight[i]) ? max(Val(i-1,w), Val((i-1, w-weight[i])+value[i])) : Val(i-1,w
'''


'''
N으로 표현

동적계획법으로 설계
N을 한 번 사용해서 만들 수 있는 수
N을 두 번 사용해서 만들 수 있는 수
N을 세 번 사용해서 만들 수 있는 수
...반복...

Ex1. N = 5
1 : 5
2 : 55 10 0 25 1
3 : 555 ,
     '1번사용해서 만든 수' + - * / '2번사용해서 만든 수',
     '2번사용해서 만든 수' + - * / '1번사용해서 만든 수'
---> 집합을 사용해서 중복 제거
4 : 5555 ,  1 (+) 3
            2 (+) 2
            3 (+) 1
            
5 : 55555,  1 (+) 4
            2 (+) 3
            3 (+) 2
            4 (+) 1
            
n : "N"*n,  1 (+) n-1
            2 (+) n-2
            ...
          n-1 (+) 1

문제의 복잡도
사칙연산 -> 한가지 계산에 4가지 방법
같은 값이 나오는 것 pass


동적계획법으로 탐색하는 범위를 효과적으로 줄임
'''

'''
중복을 허용하지 않고 수를 모으기
집합 : set()
'''
'''
s = [ set() for i in range(8) ]
print(type(s))
print(type(s[0]))
print(len(s))
for i in range(1, len(s)):
    print(i)
'''
'''
s = [ set() for i in range(8) ]
    
for i, x in enumerate(s):
    x.add(int(str(5)*i))

print(s)
'''

def solution1(N, number):
    # n번 사용해서 만들 수 있는 수들의 집합
    # s는 8개 집합을 가진 리스트
    # 숫자 사용이 8번을 넘으면 return -1 
    s = [ set() for i in range(8) ]
    
    # s의 index와 값
    # x에는 각 index의 집합이 있음
    # 사칙연산 없이 숫자로만 이루어진 것 집합에 추가
    for i, x in enumerate(s):
        x.add(int(str(N)*i))
        
    # 모든 집합 탐색
    # 1 ~ 7번 집합 탐색
    for i in range(1, len(s)):
        # 집합 번호에 따른 탐색 횟수
        # j는 숫자 조합을 하기 위함
        for j in range(i):
            # 연산자 앞에 놓일 숫자
            # 3일 때 1, 2 / 2, 1 계산을 하기 위함
            for op1 in s[j]:
                # n-1 -j
                for op2 in s[i-1-j]:
                    s[i].add( op1 + op2 )
                    s[i].add( op1 - op2 )
                    s[i].add( op1 * op2 )
                    if op2 != 0:
                        s[i].add( op1 // op2 ) #나머지 버리기 위함
        
        if number in s[i]:
            answer = i+1
            break
    
    # for문이 중간에 break 없이 끝까지 수행되었을 때 for-else문
    else:
        answer = -1
                
    return answer



# 숫자가 몇번 들어가야하는가?
# 만들 수 있는 가장 간단한 방법은 사칙연산 없이 이어붙이는 것
# 사칙연산을 이용해서 만들 때
# 숫자 n개 사용해서 다른 숫자를 만드는 방법
# 1, n-1 만드는 방법 조합 / 2, n-2 만드는 방법 조합 / ... / n-1, 1 만드는 방법 조합
# 숫자 n-1개를 사용해서 다른 숫자를 만드는 방법 ... 반복 -> 다이나믹으로 풀어보자
# 중복 숫자는 기록하지 않아도 됨 : 집합(set) 사용
# 집합의 구분은 숫자 사용 개수
# 집합의 원소는 n개 사용해서 만들 수 있는 숫자
# n개 사용해서 만들 수 있는 조합의 계산 가지수 : 집합 i의 원소, 집합 n-i-1의 원소의 사칙연산 조합

def solution2(N, number):
    answer = 0
    
    # 문제에서 주어진 숫자 최대 사용 개수는 8이기 때문에
    # 값을 담을 8개 집합을 가진 리스트를 만들어 초기화
    # 각 집합은 1~8 index로 접근
    s = [ set() for i in range(9) ]
    
    # 우선 만들 수 있는 가장 간단한 수 먼저 삽입
    # N, NN, NNN, NNNN ...
 #   for i in range(1, len(s)):
 #       s[i].add( int(str(N)*i) )
    for i, ss in enumerate(s):
        if i == 0:
            ss.add(0)
        else:
            ss.add(int( str(N)*i ))
        print(i, ss)
        
    for i in range(0, len(s)):
        print(s[i])
        
    print(s)
    
    # 각 집합은 맨 처음 집합부터 초기화
    # 1개 사용해서 만들 수 있는 수
    # 2개 사용해서 만들 수 있는 수
    # ... n개 사용해서 만들 수 있는 수
    # 해당 집합이 s 리스트의 몇번째 인지도 중요한 정보이기 때문에
    # 인덱스 값을 함께 탐색할 수 있는 enumerate로 반복문 진행
    # 1~8 index접근하도록 함
    for i, ss in enumerate(s, start=1):
        print('ss : ', ss)
        print('s[i] : ', s[i])
        '''
        여러개 집합으로 이루어진 리스트 s는
        enumerate()에 start로 값을 주어도 ss에 s[1] 집합부터 접근하는 것이 아닌
        s[0] 집합부터 접근한다.
        ss :  {0}
        s[i] :  {5}
        '''
        
        # 1, n-1 / 2, n-2 / ... / n-1, 1
        # 집합 접근을 위한 인덱스를 만드는 반복문
        for j in range(1, i):
            print("i : ", i, "  j : ", j, "  i-j : " , i-j)
            for op1 in s[j]:
                for op2 in s[i-j]:
                    print("op1 : ", op1, "  op2: ", op2)
                    print("1 : ", ss)
                    ss.add( op1 + op2 )
                    print("2 : ", ss)
                    ss.add( op1 - op2 )
                    print("3 : ", ss)
                    ss.add( op1 * op2 )
                    print("4 : ", ss)
                    if op2 != 0:
                        ss.add( op1 // op2 )
                        print("5 : ", ss)
        print(i,"번째 : ", ss, "  s[i] : ", s[i])
        
        if number in ss:
            answer = i
            break
    else:
        answer = -1
        
    return answer



# 숫자가 몇번 들어가야하는가?
# 만들 수 있는 가장 간단한 방법은 사칙연산 없이 이어붙이는 것
# 사칙연산을 이용해서 만들 때
# 숫자 n개 사용해서 다른 숫자를 만드는 방법
# 1, n-1 만드는 방법 조합 / 2, n-2 만드는 방법 조합 / ... / n-1, 1 만드는 방법 조합
# 숫자 n-1개를 사용해서 다른 숫자를 만드는 방법 ... 반복 -> 다이나믹으로 풀어보자
# 중복 숫자는 기록하지 않아도 됨 : 집합(set) 사용
# 집합의 구분은 숫자 사용 개수
# 집합의 원소는 n개 사용해서 만들 수 있는 숫자
# n개 사용해서 만들 수 있는 조합의 계산 가지수 : 집합 i의 원소, 집합 n-i-1의 원소의 사칙연산 조합

def solution3(N, number):
    # 문제에서 주어진 숫자 최대 사용 개수는 8이기 때문에
    # 값을 담을 8개 집합을 가진 리스트를 만들어 초기화
    # 각 집합은 1~8 index로 접근
    s = [ set() for i in range(9) ]
    
    # 우선 만들 수 있는 가장 간단한 수 먼저 삽입
    # N, NN, NNN, NNNN ...
 #   for i in range(1, len(s)):
 #       s[i].add( int(str(N)*i) )
    for i, ss in enumerate(s):
        if i != 0:
            ss.add(int( str(N)*i ))
            
    #print(s)
        
    # 각 집합은 맨 처음 집합부터 초기화
    # 1개 사용해서 만들 수 있는 수
    # 2개 사용해서 만들 수 있는 수
    # ... n개 사용해서 만들 수 있는 수
    # 해당 집합이 s 리스트의 몇번째 인지도 중요한 정보이기 때문에
    # 인덱스 값을 함께 탐색할 수 있는 enumerate로 반복문 진행
    # 1~8 index접근하도록 함
    for i, ss in enumerate(s):
     #   print('ss : ', ss)
     #   print('s[i] : ', s[i])
        '''
        여러개 집합으로 이루어진 리스트 s는
        enumerate()에 start로 값을 주어도 ss에 s[1] 집합부터 접근하는 것이 아닌
        s[0] 집합부터 접근한다.
        ss :  {0}
        s[i] :  {5}
        '''
        
        if i == 0 :
            continue
        
        # 1, n-1 / 2, n-2 / ... / n-1, 1
        # 집합 접근을 위한 인덱스를 만드는 반복문
        for j in range(1, i):
     #       print("??? i : ", i, "  j : ", j, "  i-j : " , i-j)
            for op1 in s[j]:
     #           print("&&& i : ", i, "  j : ", j, "  i-j : " , i-j)
                for op2 in s[i-j]:
     #               print("op1 : ", op1, "  op2: ", op2)
     #               print("s[",j,"] : ", s[j], "  s[",i-j,"] : " , s[i-j])
     #               print("1 : ", ss)
                    ss.add( op1 + op2 )
     #               print("2 : ", ss)
                    ss.add( op1 - op2 )
     #               print("3 : ", ss)
                    ss.add( op1 * op2 )
     #               print("4 : ", ss)
                    if op2 != 0:
                        ss.add( op1 // op2 )
     #                   print("5 : ", ss)
     #               print("s[",j,"] : ", s[j], "  s[",i-j,"] : " , s[i-j], "  s[",i,"] : " , s[i])
     #               print("!!! i : ", i, "  j : ", j, "  i-j : " , i-j)
     #           print("$$$ i : ", i, "  j : ", j, "  i-j : " , i-j)
     #       print("@@@ i : ", i, "  j : ", j, "  i-j : " , i-j)
     #   print(i,"번째 : ", ss, "  s[i] : ", s[i])
        
        if number in ss:
            answer = i
            break
    else:
        answer = -1
        
    return answer


# 숫자가 몇번 들어가야하는가?
# 만들 수 있는 가장 간단한 방법은 사칙연산 없이 이어붙이는 것
# 사칙연산을 이용해서 만들 때
# 숫자 n개 사용해서 다른 숫자를 만드는 방법
# 1, n-1 만드는 방법 조합 / 2, n-2 만드는 방법 조합 / ... / n-1, 1 만드는 방법 조합
# 숫자 n-1개를 사용해서 다른 숫자를 만드는 방법 ... 반복 -> 다이나믹으로 풀어보자
# 중복 숫자는 기록하지 않아도 됨 : 집합(set) 사용
# 집합의 구분은 숫자 사용 개수
# 집합의 원소는 n개 사용해서 만들 수 있는 숫자
# n개 사용해서 만들 수 있는 조합의 계산 가지수 : 집합 i의 원소, 집합 n-i-1의 원소의 사칙연산 조합

def solution(N, number):
    # 문제에서 주어진 숫자 최대 사용 개수는 8이기 때문에
    # 값을 담을 8개 집합을 가진 리스트를 만들어 초기화
    # 각 집합은 1~8 index로 접근
    s = [ set() for i in range(9) ]
    
    # 우선 만들 수 있는 가장 간단한 수 먼저 삽입
    # N, NN, NNN, NNNN ...
 #   for i in range(1, len(s)):
 #       s[i].add( int(str(N)*i) )
    for i, ss in enumerate(s):
        if i != 0:
            ss.add(int( str(N)*i ))
        
    # 각 집합은 맨 처음 집합부터 초기화
    # 1개 사용해서 만들 수 있는 수
    # 2개 사용해서 만들 수 있는 수
    # ... n개 사용해서 만들 수 있는 수
    # 해당 집합이 s 리스트의 몇번째 인지도 중요한 정보이기 때문에
    # 인덱스 값을 함께 탐색할 수 있는 enumerate로 반복문 진행
    # 1~8 index접근하도록 함
    for i, ss in enumerate(s):
        
        if i == 0:
            continue
        
        # 1, n-1 / 2, n-2 / ... / n-1, 1
        # 집합 접근을 위한 인덱스를 만드는 반복문
        for j in range(1, i):
            for op1 in s[j]:
                for op2 in s[i-j]:
                    ss.add( op1 + op2 )
                    ss.add( op1 - op2 )
                    ss.add( op1 * op2 )
                    if op2 != 0:
                        ss.add( op1 // op2 )
        
        if number in ss:
            answer = i
            break
    else:
        answer = -1
        
    return answer
# 여기서 list의 index를 굳이 1부터 시작하는거로 사용할 필요가 없다
# 다시 코드 깔끔하게 정리하기



print(solution(5, 12))



'''
***enumerate 사용 방법***
for i, s in enumerte(list, start=2)
s는 list에 담긴 원소를 처음부터 끝까지 탐색하는 동안
i는 start에 정의한 숫자부터 +1되면서 numbering한다.

착각했던 것
start=2라고 정의하면
list[2]부터 탐색하는줄 알고 아래와 같이 테스트함

start는 단순히 i의 시작 number를 정할 뿐
list는 맨 처음부터 탐색하게된다
'''

'''
s = [ set() for i in range(9) ]
enum = enumerate(s, start=1)
print(next(enum))
print(next(enum))
print(next(enum))
print(next(enum))

print("TEST1")
s = [ set() for i in range(9) ]
for i, ss in enumerate(s):
    ss.add(i)
    print('ss :', ss, '\ts[',i,'] : ',s[i])

ss : {0} 	s[ 0 ] :  {0}
ss : {1} 	s[ 1 ] :  {1}
ss : {2} 	s[ 2 ] :  {2}
ss : {3} 	s[ 3 ] :  {3}
ss : {4} 	s[ 4 ] :  {4}
ss : {5} 	s[ 5 ] :  {5}
ss : {6} 	s[ 6 ] :  {6}
ss : {7} 	s[ 7 ] :  {7}
ss : {8} 	s[ 8 ] :  {8}

print("TEST2")
s = [ set() for i in range(9) ]
s[0].add(0)
for i, ss in enumerate(s, start=1):
    ss.add(i)
    print('ss :', ss, '\ts[',i,'] : ',s[i], '\ts[',i-1,'] : ',s[i-1])

ss : {0, 1} 	s[ 1 ] :  set() 	s[ 0 ] :  {0, 1}
ss : {2} 	s[ 2 ] :  set() 	s[ 1 ] :  {2}
ss : {3} 	s[ 3 ] :  set() 	s[ 2 ] :  {3}
ss : {4} 	s[ 4 ] :  set() 	s[ 3 ] :  {4}
ss : {5} 	s[ 5 ] :  set() 	s[ 4 ] :  {5}
ss : {6} 	s[ 6 ] :  set() 	s[ 5 ] :  {6}
ss : {7} 	s[ 7 ] :  set() 	s[ 6 ] :  {7}
ss : {8} 	s[ 8 ] :  set() 	s[ 7 ] :  {8}
Traceback (most recent call last):
  File "F:\study_myself\study\python_코테강의\dynamic_연습문제.py", line 271, in <module>
    print('ss :', ss, '\ts[',i,'] : ',s[i], '\ts[',i-1,'] : ',s[i-1])
IndexError: list index out of range


print("TEST3")
s = [ set() for i in range(9) ]
for i, ss in enumerate(s, start=1):
    ss.add(i)
    print('ss :', ss, '\ts[',i,'] : ',s[i], '\ts[',i-1,'] : ',s[i-1])

ss : {1} 	s[ 1 ] :  set() 	s[ 0 ] :  {1}
ss : {2} 	s[ 2 ] :  set() 	s[ 1 ] :  {2}
ss : {3} 	s[ 3 ] :  set() 	s[ 2 ] :  {3}
ss : {4} 	s[ 4 ] :  set() 	s[ 3 ] :  {4}
ss : {5} 	s[ 5 ] :  set() 	s[ 4 ] :  {5}
ss : {6} 	s[ 6 ] :  set() 	s[ 5 ] :  {6}
ss : {7} 	s[ 7 ] :  set() 	s[ 6 ] :  {7}
ss : {8} 	s[ 8 ] :  set() 	s[ 7 ] :  {8}
Traceback (most recent call last):
  File "F:\study_myself\study\python_코테강의\dynamic_연습문제.py", line 268, in <module>
    print('ss: :', ss, '\ts[',i,'] : ',s[i])
IndexError: list index out of range


print("TEST4")
s = [ set() for i in range(9) ]
for i, ss in enumerate(s, start=5):
    ss.add(i)
    print('ss :', ss, '\ts[',i,'] : ',s[i], '\ts[',i-5,'] : ',s[i-5])

TEST4
ss : {5} 	s[ 5 ] :  set() 	s[ 0 ] :  {5}
ss : {6} 	s[ 6 ] :  set() 	s[ 1 ] :  {6}
ss : {7} 	s[ 7 ] :  set() 	s[ 2 ] :  {7}
ss : {8} 	s[ 8 ] :  set() 	s[ 3 ] :  {8}
Traceback (most recent call last):
  File "F:\study_myself\study\python_코테강의\dynamic_연습문제.py", line 243, in <module>
    print('ss :', ss, '\ts[',i,'] : ',s[i], '\ts[',i-5,'] : ',s[i-5])
IndexError: list index out of range
'''
# 리스트안에 비어있는 집합으로 구성되어 있을 때
# enumerate()에 start를 준 다음
# 해당 index에 위치한 집합에 add를 하고 싶었지만
# test결과
# 집합에 add를 할 때 해당 index에 위치안 집합이 아닌
# 맨 앞에 위치한 집합부터 add
