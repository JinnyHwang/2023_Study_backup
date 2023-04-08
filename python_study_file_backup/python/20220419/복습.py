
# N을 가장 적게 활용해서 number 값을 도출
# N을 1개 써서 만들 수 있는 수
# N을 2개 써서 만들 수 있는수 
# N 1개 수와 N 2개 수의 경우의 수
# 숫자 n개 사용해서 다른 숫자를 만드는 방법
# 1, n-1 만드는 조합 / 2, n-2 만드는 조합 / ... / n-1, 1 만드는 조합
# 반복 다이나믹으로 풀어보자
# 중복 숫자는 기록하지 않음 : 집합 set() 사용
# 집합의 구분은 숫자 사용 개수
# n개 사용해서 만들 수 있는 조합의 계산 가지수는?
# 집합 i의 원소, 집합 n-i의 원소의 사칙연산 조합

def solution(N, number):
    
    # 문제에서 주어진 숫자 최대 사용 개수는 8개
    # 1~8 index로 접근할 수 있는 집합 묶음 s
    s = [ set() for i in range(9) ]
    
    # 우선 만들 수 있는 숫자 add
    
    for i, ss in enumerate(s):
        if i != 0:
            ss.add(int(str(N)*i))
    #print(s)
    
    for i, ss in enumerate(s):
        
        if i == 0:
            continue
        
        for j in range(1, i):
            for op1 in s[j]:
                for op2 in s[i-j]:
                    ss.add(op1 + op2)
                    ss.add(op1 - op2)
                    ss.add(op1 * op2)
                    if op2 != 0:
                        # 몫만 나머지 무시
                        ss.add(op1 // op2)
        if number in ss:
            answer = i
            break
    else:
        # for문을 전체 탐색함
        answer = -1
            
    return answer


print(solution(5, 12))
print(solution(2, 11))








