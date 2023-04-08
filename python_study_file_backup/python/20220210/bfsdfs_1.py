
def solution_1(nums, target):
    
    result = 0
    
    def dfs1(index, hap):
        nonlocal result
        
        if index == len(nums):
            if hap == target:
                result += 1
            return
        
        if index == 0:
            dfs1(index+1, hap)
            dfs1(index+1, -hap)
        else:
            dfs1(index+1, hap + nums[index])
            dfs1(index+1, hap - nums[index])
        
    dfs1(0, nums[0])

    return result



def solution(numbers, target):
    result = 0
    
    def dfs(num, level):
        # 지역변수, 전역변수 둘 다 아닌 변수.
        # def solution에서 선언한 변수
        nonlocal result
        
        if level == len(numbers):
            if num == target:
                result += 1
            return
        
        if level == 0:
            dfs( num, level+1 )
            dfs( -num, level+1 )
        else:
            dfs( num + numbers[level], level+1 )
            dfs( num - numbers[level], level+1 )
            
    dfs(numbers[0], 0)
    return result

num1 = [1, 1, 1, 1, 1]
print(solution(num1, 3))
print(solution_1(num1, 3))

num2 = [4, 1, 2, 1]
print(solution(num2, 4))
print(solution_1(num2, 4))








