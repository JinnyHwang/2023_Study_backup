
# 계산 반복
# 계산의 끝은? 계산횟수!


def solution(numbers, target):
    
    answer = 0
    
    def dfs(cnt, value, numbers, target):
        
        nonlocal answer
          
        if cnt == len(numbers):
            if value == target:
                answer += 1
            return
        
        dfs(cnt+1, value+numbers[cnt], numbers, target)
        dfs(cnt+1, value-numbers[cnt], numbers, target)

    
    dfs(0, 0, numbers, target)
    
    print(answer)
    
    
n1 = [1, 1, 1, 1, 1]
t1 = 3

n2 = [4, 1, 2, 1]
t2 = 4
    
solution(n1, t1)
solution(n2, t2)

















