'''
큰 수 만들기 원칙
앞 자리에 큰 수가 오는 것이 전체를 크게 만든다
-> 큰 것을 우선해서 골라담고 싶다

수를 뺄 때 작은 수를 없애는데,
앞자리에 있는 작은수가 우선 순위

k개를 뺀다!

어떻게 단계적으로 수행할까?

앞자리에서부터 하나씩 골라서 담되,
지금 담으려는 것 보다 작은 것들은 도로 뺀다

큰 수가 앞자리, 작은 수가 뒷자리
제약 : 뺄 수 있는 수의 개수

number = "4177252841"

우선 앞에서부터 담는다
작은 수를 빼는 것을 기록

4
41
417
47   |
7    ||
77
772
7725
775   |||
7752
77528
7758  ||||
---> 뺄 수 있는 남은 개수를 모두 소진했기 때문에5는 뺄 수 없음
775841 (나머지 붙이기)

그런데!
number = "98765"
이미 큰 수대로 정렬되어 있음
-> 위 방식으로는 뺄 수 있는 수 없음
-> 맨 뒤에서 빼야할 개수 만큼 뺌
987
'''

'''
주어진 숫자로 부터 하나씩 꺼내서 모음
- 이미 모아둔 것 중 지금 등장한것보다 작은 것 뺌
모은 숫자들은 자릿수를 맞추어 반환
- 아직 뺄 개수를 채우지 못한 경우
-> 뒤에서부터 뺀다
자릿수는 어떻게 계산?
'''

'''
알고리즘 복잡도
- 가장 단순한 방법은?
가능한 조합의 수를 모두 구해서 그 중 가장 큰 수
-> 조합의 수가 너무 큼
O(n)
모든 자리의 수
한 수는 들어가거나 빠지거나 하나의 동작만?
주어진 수의 길이에 비례하는 알고리즘
-> 음... 어렵네
'''

'''
탐욕법 (Greedy Approach)
앞 단계에서의 선택이
이후 단계에서의 동작에 의한 해(solution)의
최적성(optimality)에 영향을 주지 않음

-> 모든 방향을 살피는 것이 아니라
한 방향으로 진행
왜냐면 이후 계산이 앞서 수행한 동작에 영향주지 않기 때문
'''

'''

'''

def solution(number, k):
    collected = [] # 숫자를 하나하나 모으는 용도
    
    # 파이썬은 str은 뮤터블, 리스트는 인뮤터블
    # 문자열보다 리스트를 이용하는 것이 효율 좋음
    
    # 인덱스, 숫자 모두 확인
    for i, num in enumerate(number): # 시간복잡도를 결정하는 순환문
        
        # collected에 값이 있을 때
        # collected의 맨 마지막값과 현재 탐색중인 값 비교
        # collected에 들어있는 값이 더 작으면 빼기
        # 뺄 수 있는 횟수 소진(k==0) break
        # collected 마지막 숫자가 더 크면 break
        while len(collected)>0 and k>0 and collected[-1] < num: # 이중순환문
            collected.pop()
            k-=1
        if k==0:
            collected += list(collected[i:])
            break
        collected.append(num)
        
'''        
    if k > 0:
        # 남은 k개수 만큼 뒤에서 list 삭제
        collected = collected[:-k]
'''
        collected = collected[:-k] if k > 0 else collected
        
        # 리스트를 문자열로
        answer = ''.join(collected)
        return answer


def solution(number, k):
    # 큰수를 만들기위해서는 맨 앞에 가장 큰 수가 나와야한다
    # 맨 앞에서부터 비교
    # 다음에 들어올 숫자가 더 크다면
    # 이전에 들어온 앞숫자 빼기 pop
    # 내 앞 숫자가 더 크다면 현재수 더하기 append
    # 뺄 수 있는 횟수를 소진하면 리스트에 남은 숫자 ++
    # 탐색이 끝났는데 k가 남아있는 경우
    # 맨 뒷자리에서부터 뺀다
    
    # 빈 리스트 생성
    result = []
    
    # 문자열 인덱스 하나하나 탐색
    # enumerate를 사용하면 인덱스도 함께 확인 가능
#    for num in number :
    for i, num in enumerate(number):
       # 다른 조건문에서 해당 동작 대체
       # if len(result)==0:
       #     result.append(num)
        
        # 탐색하는 숫자가 result의 마지막 숫자보다 작을 때까지 제거 반복
        while len(result) > 0 and result[-1] < num and k > 0:
            result.pop()
            k -= 1
        if k == 0:
            # result.append(list(number[i:])) # [ , []] 리스트 안에 리스트가 있는 형태가됨
            result.append(number[i:])
            break
        result.append(num)
    
    # 아직 뺄 횟수가 남아있음
    # 맨 뒤에서부터 k개수만큼 자름
    if k > 0:
        result = result[:-k]
    
    # 현재 리스트형태로 구성
    # 문자열 형태로 반환
    answer = ''.join(result)
    return answer













