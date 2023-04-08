
'''
큰 수 만들기
탐욕법
앞 단계 선택이 이후 단계 동작에 영향을 주지 않는 것

어떤 숫자에서 k개 수를 제거했을 때 얻을 수 있는 가장 큰 수?

원칙??
앞자리에 큰 수가 오도록

앞쪽에서부터
빼고 당기고 반복
'''

def solution(number, k):
    
    collected = []
    
    for i, num in enumerate(number):
        # 정수 변환 없이 문자열 상태로 비교 괜찮은가? 한 자리 수 비교이기 때문에 무관함
        while len(collected) > 0 and collected[-1] < num and k > 0:
            collected.pop()
            k -= 1
        
        if k == 0:
            collected += list(number[i:])
            break
            
        collected.append(num)
        
    
    collected = collected[:-k] if k>0 else collected
    print(collected)
    
    answer = ''.join(collected)
    print(answer)
    return answer



n1 = "1924"
k1 = 2
solution(n1, k1)

n2 = "1231234"
k2 = 3
solution(n2, k2)

n3 = "4177252841"
k3 = 4
solution(n3, k3)



def solution1(number, k):
    c = []
    
    for i, num in enumerate(number):
        
        while len(c) > 0 and k > 0 and c[-1] < num:
            c.pop()
            k -= 1
        
        if k == 0:
            # c.append(list(number[i:])) c의 맨 끝 원소로 리스트가 들어가는 코드
            c += list(number[i:])
            break
        c.append(num)
        
        print(c)
        answer = ''.join(c)
        return answer











