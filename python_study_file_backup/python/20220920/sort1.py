
'''
가장 큰 수

만약 3 , 32 , 33 , 34 가 있다.

이어붙였을 때 가장 큰 수는?
가장 큰 수를 반복적으로 이어붙인 수는
다른 어떤 숫자를 붙인 숫자보다도 크다

반복적으로 이어붙여서 크기 비교하기

매 단계에서 가장 큰 수를 고르는 방법

3 , 33 은 순서 상관 없음


시간복잡도?

sort는 이중에서 가장 높은 시간 복잡도를 가짐
sort : NlogN

리스트생성, join, data 탐색 list 원소 개수에 비례
'''


def solution(numbers):
    # 원소 하나하나 str 자료형으로 변환 후 리스트로
    numbers = [str(x) for x in numbers]
    print(numbers)
    # key값 기준으로 sort
    # key값은 x를 반복적으로 쓰고 이를 앞에서부터 4까지 자르는것
    numbers.sort(key=lambda x : (x*4)[:4], reverse=True)
    print(numbers)
    
    if numbers[0] == '0':
        answer = 0
    else:
        answer = ''.join(numbers)
    print(answer)
    
    return answer




n1 = [6, 10, 2]
print('n1:', solution(n1))

n2 = [3, 30, 34, 5, 9]
print('n2:', solution(n2))

n3 = [3, 30, 34, 5, 9, 33]
print('n3:', solution(n3))


n4 = [0, 0, 0, 0]
print('n4:', solution(n4))






