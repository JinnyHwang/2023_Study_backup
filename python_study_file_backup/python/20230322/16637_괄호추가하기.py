
# 브루트포스 알고리즘: 조합 가능한 모든 문자열을 하나씩 대입해 보는 방식으로 암호를 해독하는 방법
# https://jaimemin.tistory.com/1454
# https://www.acmicpc.net/problem/16637

#print(l[0], l[N-1])

# 괄호에 포함되었는지 확인하는 리스트
#use = [ 0 for _ in range(N)]

# 홀수 index: 숫자
# 짝수 index: 연산자

# 괄호를 쓸 수 없는 경우
# 1. 탐색 index와 index+2의 use 값이 1 일 때
# 2. 탐색 index가 N-1 일 때

# 완전 탐색을 어떤 방식으로 하면 좋을까? 재귀!
# 인덱스로 탐색하면서
# 바로 계산하는 방법
# 괄호 묶어서 계산하는 방법

N = int(input())
l = [ ss for ss in input()]


def cal(a, b, op):
    if op == '+':
        return a+b
    elif op == '-':
        return a-b
    elif op == '*':
        return a*b


answer = 0

def sol(idx, cal_data):
    
    global answer
    
    if idx >= N-1:
        answer = max(cal_data, answer)
        return
    
    # 맨 처음 data 계산은 operand '+'로!
    if idx == 0:
        sol(idx+2, cal(cal_data, int(l[idx]), '+'))
    else:
        sol(idx+2, cal(cal_data, int(l[idx]), l[idx-1]))
    
    
    # 괄호로 묶을 수 있는 경우
    if idx != 0 and idx < N-2:
        temp = cal(int(l[idx]), int(l[idx+2]), l[idx+1])
        sol(idx+4, cal(cal_data, temp, l[idx-1]))


sol(0, 0)
print(answer)

'''
# 탐색에서 사용해서 결과값을 return 할 리스트
l2 = [ ll for ll in l ]
l2[0:3] = 계산결과값
치환하면서 결과값 도출하려 했는데... 완전 탐색이 어려워짐

for n in range(0, N, 2):
    # 괄호 묶을지 안묶을지 확인
    # n==0일 때 계산하는건 괄호처리 안함
    if use[n] != 1:
        # 여기서 계산 할지 말지     
'''    





