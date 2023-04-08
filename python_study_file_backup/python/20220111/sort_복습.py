
# 정렬 큰 수 만들기
def solution1(numbers):
    # 문자열 리스트로 변경
    numbers = [ str(x) for x in numbers ]
    
    # 원소 값을 lambda로 구현한 값을 기준으로 오름차순 정렬
    numbers.sort( key=lambda x : (x*4)[:4], reverse=True)
   # print(numbers[0], numbers)
    if numbers[0] == '0': #number의 원소를 str()로 변환하면서 모든 0은 '0'으
        answer = '0'
    else:
        answer = ''.join(numbers)
    print(answer)
    return answer

l = [6, 10, 2]
l2 = [00, 0000]
solution(l)
solution(l2)


def solution2(nlist):
    nlist = [ str(x) for x in nlist ]
    
    nlist.sort(key=lambda x : (x*4)[:4], reverse=True)
    answer = ''.join(nlist)
    return answer


# greedy 큰 수 만들기
# 앞 단계에서의 선택이 이후 단계에서의 동작에 의한 해의
# 최적성에 영향을 주지 않음



















