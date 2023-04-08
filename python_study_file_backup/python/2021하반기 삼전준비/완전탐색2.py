# 순열과 조합
# combinations , permutations
# itertools
# n개 원소로 수열만들기
# itertools.permutation(list, n)
'''
import itertools from permutation
> list(permutation("246", 1~len("246")))
[('2',), ('4',), ('6',)]
[('2', '4'), ('2', '6'), ('4', '2'), ('4', '6'), ('6', '2'), ('6', '4')]
[('2', '4', '6'), ('2', '6', '4'), ('4', '2', '6'), ('4', '6', '2'), ('6', '2', '4'), ('6', '4', '2')]
'''
from itertools import permutations
import math

# 모든 조합 만들기
# 소수인지 판단하기
# 소수면 바로 count


def is_prime_number(num):
    if num < 2:
        return False
    
    for n in range(2, num):
        if num%n == 0:
            return False
    else:
        return True

def solution(numbers):
    answer = 0
    num_list = []
    num_set = []
    for i in range(1, len(numbers)+1):
    #    print(list(permutations(numbers, i)))
        # permutation으로 만들어지는 tuple을 한 단어로 만들기(join사용)
        # 주어진 원소로 만들 수 있는 모든 조합 num_list에 저장
        # 중복 제거를 위해 set() 집합으로 저장
        num_list += list(''.join(tup) for tup in permutations(numbers, i))
    print(num_list)

    num_set = set(map(int, num_list))
    print(num_set)
        
    for n in num_set:
        if is_prime_number(n):
            answer += 1

    return answer
            
    

def solution1(numbers):
    
    num = []
    for n in numbers:
        num.append(int(n))    
    print(num)
    
    num.sort()
    
    # 소수 (0, 1제외)
    # 2, 3, 5, 7, 11, 13, 17...
    
    print(num)
 #   for i, n in enumerate(num):
        
    
    return 0


s1 = "17"
s2 = "011"
s3 = "244"

#print(solution(s1))
#print(solution(s2))
print(solution(s2))




