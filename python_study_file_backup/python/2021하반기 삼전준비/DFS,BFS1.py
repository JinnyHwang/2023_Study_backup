
# 덧셈 뺄셈만 사용해서 target number 만들기
# DFS로 탐색
# 주어진 number를 +할지, -할지

# key: 사용한 number개수
# value: set() 사용해서 만들 수 있는 숫자 집합
#redic = {1:set()}
#redic[i] = redic.get(i, set()) + 값(type 집합)
#redic[1] = redic.get(1, set()) + set(2)
#redic[1] = redic.get(1, set()) + [3]
#redic[1] = redic.get(1, set()) + (3)
#redic[1].add(4)
#print(redic)
#for i in range(len(numbers)):
        #redic[i+1] = redic.get(i+1, [])    
    #print(redic)
    
def solution1(numbers, target):
    redic = {}
    
    # number sort
    # 모든 number의 조합을 거쳤을 때 target이 나오는 root 찾기
    
    # 모든 조합 알아보기
    # numbers의 원소로 만들 수 있는 경우의 수 -n, +n
    
    num_tup = [ [n, -n] for n in numbers ]
    
    
    for i, n in enumerate(numbers):
        if i == 0:
            redic[i] = redic.get(i, []) + [n, -n]
        elif i > 0:
            for r in redic[i-1]:
                redic[i] = redic.get(i, []) + [r+n, r-n]
    
    print(redic[len(numbers)-1])
    
    # list.count(value) -> 리스트에 해당 값이 얼마나 있는지 알 수 있음
    answer = redic[len(numbers)-1].count(target)
    #for r in redic[len(numbers)-1]:
    #    if r == target:
    #        answer += 1
    
    
    # 해당 root에서 number 자리를 바꿨을 때 나올 수 있는 경우의 수?
    #---> 비효율적인듯
    
    return answer

# function 내부에서 전역변수를 사용하고 싶을 때
# global x
# 해당 function에서 지역변수, 전역변수 둘 다 아닌 변수를 사용할 때
# nonlocal x

# 질문하기에서 확인한 code
def solution(numbers, target):
    result = 0
    
    def dfs(num, level):
        # 지역변수, 전역변수 둘 다 아닌 변수 (def solution에서 선언한 변수)
        nonlocal result
        
        # 마지막 원소까지 계산 완료.
        if level == len(numbers):
            if num == target:
                result += 1
            return
        
        # num이 numbers[0] 원소일 때
        if level == 1:
            signs = [-num, num]
            # -num, +num 두 번 계산해야하기 때문
            for i in range(2):
                dfs(signs[i] + numbers[level], level+1)
                dfs(signs[i] - numbers[level], level+1)
        else:
            dfs(num + numbers[level], level+1)
            dfs(num - numbers[level], level+1)
                
        
    dfs(numbers[0], 1)
    return result


def solution2(numbers, target):
    # numbers 배열이 없어질 때 까지 반복하는데
    # target이 0이 된다는 뜻은? 해당조합으로 만든 수가 target값이 된다는 뜻
    if not numbers and target == 0:
        return 1
    
    elif not numbers:
        return 0
    
    else:
        return solution(numbers[1:], target-numbers[0]) + solution(numbers[1:], target+numbers[0])




n1 = [1, 1, 1, 1, 1]
t1 = 3

print(solution(n1, t1))





