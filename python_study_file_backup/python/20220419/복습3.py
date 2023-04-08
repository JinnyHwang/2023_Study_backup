
# 특정 숫자를 만드는 방법의 개수
# dic의 key를 만들 수 있는 숫자 value를 방법 개수로 할까?
# 단계별로 만들 수 있는 숫자, 해당 숫자를 만들 수 있는 방법 개수
def solution1(numbers, target):
    
    dic = {0:0}
    print(dic)
    for n in numbers:
        # 딕셔너미 탐색동안 변경X
        for k in dic.keys():
            dic[k+n] = dic.get(k+n, 0) + 1
            dic[k-n] = dic.get(k-n, 0) + 1
    print(dic)
    
    return 0

def solution2(numbers, target):
    
    l = [ [] for _ in range(len(numbers)+1) ]
    l[0] = [0]
    #print(l)
    
    for i, n in enumerate(numbers, start=1):
        for ll in l[i-1]:
            l[i].append(ll+n)
            l[i].append(ll-n)
            
    #print(l)
    cnt = 0
    for v in l[len(numbers)]:
        if v == target:
            cnt += 1
    
    return cnt

# 연산 횟수, 결과 값만 필요
# 스스로 생각해보
def solution(numbers, target):
    
    answer = 0
    
    def dfs(i, re):
        # 로컬변수가 아님을 선언
        # nonlocal은 사용된 함수의 바로 한 단계 바깥에 위치한 변수와 바인딩 하기 위해 사용
        nonlocal answer
        
        if i == len(numbers):
            if re == target:
                answer += 1
            return
        
        
        if i == 0:
            dfs(i+1, numbers[i])
            dfs(i+1, -numbers[i])
        else:
            dfs(i+1, re+numbers[i])
            dfs(i+1, re-numbers[i])
        
        
    
    # 0번 연산 결과값 0
    dfs(0,0)
    
    return answer



n1 = [1, 1, 1, 1, 1]
t1 = 3

n2 = [4, 1, 2, 1]
t2 = 4

print(solution(n1, t1))
print(solution(n2, t2))

