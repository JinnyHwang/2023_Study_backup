

def solution(numbers, target):
    
    answer = 0
    
    def dfs(i, re):
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
    
    dfs(0, 0)
    
    return answer



l1 = [1, 1, 1, 1, 1]
t1 = 3
print(solution(l1, t1))

l2 = [4, 1, 2, 1]
t2 = 4
print(solution(l2, t2))










