
def solution(n, lost, reserve):
    answer = 0
    
    # 모든 학생 체육복 1개씩 있다 가정
    cloth = [ 1 for i in range(n)]
    
    for r in reserve:
        cloth[r-1] += 1
        
    for l in lost:
        cloth[l-1] -= 1
    
    print(cloth)
    
    # 가장 많이 빌려줄 수 있는 방법은
    # 우선 앞번호 학생이 뒷번호 학생한테 빌려주는 것
    # 안될경우 뒷번호학생 탐색
    for i, c in enumerate(cloth):
        if c == 0:
            if i != 0 and cloth[i-1] == 2:
                cloth[i] = 1
                cloth[i-1] = 1
            elif i<len(cloth)-1 and cloth[i+1] == 2:
                cloth[i] = 1
                cloth[i+1] = 1
    print(cloth)
    for c in cloth:
        if c >= 1:
            answer += 1
    
    return answer



n1=5
l1=[2, 4]
r1=[1, 3, 5]

n2=5
l2=[2, 4]
r2=[3]

n3=3
l3=[3]
r3=[1]

print(solution(n1, l1, r1))
print(solution(n2, l2, r2))
print(solution(n3, l3, r3))



