
dic = {}

for i in range(15):
    dic[i%5] = dic.get(i%5, 0) + 1

print(dic)

def solution1(participant, completion):
    
    d = {}
    
    for x in participant:
        d[x] = d.get(x, 0) + 1
        
    for x in completion:
        d[x] -= 1
        
    dnf = [ k for k, v in d.items() if v > 0 ]
    
    answer = dnf[0]
    
    return answer


# greedy
# 각 단계에서 그 순간 최적이라 생각되는 것을 선택
# 현재의 선택이 마지막 해답의 최적성을 해치지 않을 때

def solution2(n, lost, reserve):
    
    # 앞뒤로 의미없는 숫자 넣음(예외처리 피하기 위해서)
    # 1~n index 사용
    u = [1]*(n+2)
    
    for i in reserve:
        u[i] += 1
        
    for i in lost:
        u[i] -= 1
        
    for i in range(1, n+1):
        if u[i-1] == 0 and u[i] == 2:
            u[i-1:i+1] = [1, 1]
        elif u[i] == 2 and u[i+1] == 0:
            u[i:i+2] = [1, 1]
            
    return len( [x for x in u[1:-1] if x > 0 ] )

# set() 집합을 만들 때
def solution2(n, lost, reserve):
    s = set(lost)&set(reserve) # 교집합. 2개있었고 하나잃어버린 학생
    l = set(lost) - s # 체육복이 아예 없는 학생
    r = set(reserve) - s # 체육복이 2개 있는 학
    
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
    # 끝까지 체육복이 0개인 학생 수를 뺌
    return n-len(l)

