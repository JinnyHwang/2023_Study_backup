
def solution1(n, lost, reserve):
    
    # 배열 앞,뒤에 쓰레기값 여분을 넣어줌
    u = [ 1 for _ in range(n+2) ]
    
    for i in reserve:
        u[i] += 1
        
    for i in lost:
        u[i] -= 1
    
    for i in range(1, n+1):
        if u[i] == 2 and u[i-1] == 0 :
            u[i-1:i+1] = [1,1]
        elif u[i] == 2 and u[i+1] == 0:
            u[i:i+2] = [1,1]
    
    return len([x for x in u[1:-1] if x > 0])


# 집합 사용 set() : hash
# dictionary와 달리 key, value없이 해당 원소가 집합에 속해 있는지 아닌지만.    
def solution2(n, lost, reserve):
    
    s = set(lost) & set(reserve)
    l = set(lost) - s # 체육복 빌려야 하는 학생들
    r = set(reserve) - s # 체육복 빌려줄 수 있는 학생들
    
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remover(x+1)
    
    # 체육복 못빌린 학생 빼기
    return n-len(l)
    


