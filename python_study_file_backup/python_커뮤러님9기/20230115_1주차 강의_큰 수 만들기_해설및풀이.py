
'''
탐욕법 - 큰 수 만들기

원칙
앞 자리에 큰 수가 오는 것이 전체를 크게 만든다
-> 큰 것 우선해서 담고 싶음

방법
앞 자리에서 하나씩 골라서 담되
담으려는 것보다 작은 것은 도로 뺀다
단, 뺄 수 있는 수효에 도달할 때 까지

큰 수가 앞자리, 작은 수가 뒷자리에 놓이도록
제약: 뺄 수 있는 수의 개수

[case 1]
numbers = "4177252841" / k = 4
4
4 1
4 1 7 => 4 7 => 7
7 7
7 7 2
7 7 2 5 => 7 7 5
7 7 5 2
7 7 5 2 8 => 7 7 5 8
(k 4회 소진)
7 7 5 8 4 1

[case 2]
numbers = "98765" / k = 2
이미 정렬이 되어 있기 때문에
맨 뒤 2개 숫자 빼기
9 8 7


주어진 숫자로부터 하나씩 꺼내서 모은다
이 때, 이미 모아둔 것 중 지금 등장한 것보다 작은 것은 뺀다
이렇게 모은 숫자들은 자릿수를 맞춰서 반환한다
뺄 개수를 채우지 못하는 경우는? 맨 뒤에서 빼기
-> 자릿수는 어떻게 계산하는가?


가장 무식한 방법은?
모든 경우의 수를 나열하고 가장 큰 수 고르기 => 수가 클수록 조합의 수가 너무 많음

설계한 알고리즘 복잡도는?
numbers의 자릿수에 비례하는 O(N)

모든 경우의 수 조사하는 것이 아닌
앞에서부터 순차적으로 확인
탐욕법
앞 단계에서의 선택이
이후 단계에서의 동작으로 나온 해의 최적성에 영향을 주지 않는다.
'''

# 파이썬 mutable , immutable
# mutable - 변경 가능한 객체 : list, set, dictionary 등
# 값 변경 시 할당된 메모리에 전달 됨. call by reference

# immutable - 변경 불가능 객체  : 숫자, string, tuple
# 값 변경 시 새로운 메모리에 전달 됨. call by value
def solution(number, k):
    
    # 숫자 채우기. mutable한 list로 (string은 immutable)
    collected = []
    
    for i, num in enumerate(number): # N회 반복. 시간 복잡도는 상수 시간 O(1) linear
        # 뺄 숫자가 존재하고, k횟수가 남아있을 때
        while len(collected) > 0 and collected[-1] < num and k > 0: # 이중 순환문
            # 숫자를 올바르게 collect했다면, collected[-1]와 대소비교로 확인 가능
            # 문자열 한 글자이기 때문에 정수 비교와 동일. 정수 변환 없이 비교 가능
            collected.pop()
            k -= 1
            
        if k == 0:
            collected += list(number[i:])
            break
        
        collected.append(num)

    # collected[:-k] 확인하기
    collected = collected[:-k] if k > 0 else collected
    
    answer = ''.join(collected)
    return answer




















