
# number가 주어지고, target이 주어질 때
# target을 만들 수 있는 방법 개수는?

def solution(numbers, target):
    
    answer = 0
    answer1 = 0
    
    def dfs(numbers, i, result, target):
        nonlocal answer
        
        if i == len(numbers):
            if result == target:
                answer += 1
            return
        
        dfs(numbers, i+1, result+numbers[i], target)
        dfs(numbers, i+1, result-numbers[i], target)
        
    def dfs1(i, re):
        nonlocal answer1
        if i == len(numbers):
            if re == target:
                answer1 += 1
            return
        
        dfs1(i+1, re+numbers[i])
        dfs1(i+1, re-numbers[i])
                
    
    dfs(numbers, 0, 0, target)
    dfs1(0, 0)
    print(answer)
    print(answer1)
    
n1 = [1, 1, 1, 1, 1]
n2 = [4, 1, 2, 1]
        
solution(n1, 3)
solution(n2, 4)












