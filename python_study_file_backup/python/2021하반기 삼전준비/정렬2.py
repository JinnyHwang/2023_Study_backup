
# 규칙
# numbers
# 큰 수가 앞으로
# 앞자리 숫자가 같으면?
# number가 정렬되어 있다 가정했을 때
# number를 이어붙여 만들었을 때 숫자는
# 현재 number + 다음 작은 숫자 number를 붙여 만든 값보다 크다
# 현재 number를 이어붙여 만들었을 때 숫자가 해당 숫자로 만들 수 있는 가장 큰 수

#a = map(int, input().split())

def solution(numbers):
    
    numbers.sort(key=lambda x : int((str(x)*4)[:4]), reverse=True)
    
    if numbers[0] == 0:
        return "0"
    
    answer = ''
    for n in numbers:
        answer += str(n)
        
    return answer



a1 = [6, 10, 2]
a2 = [3, 30, 34, 5, 9]

print(solution(a1))
print(solution(a2))





