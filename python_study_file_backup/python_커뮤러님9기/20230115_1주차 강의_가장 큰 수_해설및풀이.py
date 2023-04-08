
'''
정렬 - 가장 큰 수

해결 방법

1. 빈 문자열로 수를 초기화
2. 가장 크게 만들 수 있는 수 고르기
3. 그 수를 현재 수에 이어 붙이기
4. 모든 수를 다 사용할 때 까지 반복

=> '크게 만드는 수' 기준은?

길이가 각자 다르기 때문에..
앞자리가 같을 때 어떤 수를 고르는가?

만약 수가 정렬되어 있다 가정.
현재 수는 무조건
현재+현재 붙이는 수가 현재+다음 붙이는 것 보다 크다

대소관계 비교를 위한 기준은?
이어붙인 문자로 비교
'''

def solution(numbers):
    
    # N회 반복
    numbers = [ str(n) for n in numbers ]

    # O(NlogN)
    numbers.sort( key = lambda x : (x*4)[:4], reverse = True )
    
    if numbers[0] == '0': # 상수 시간
        return '0'
    
    # join() N에 비례
    answer = ''.join(numbers)
    return answer
# 총 시간 복잡도는 O(NlogN)

