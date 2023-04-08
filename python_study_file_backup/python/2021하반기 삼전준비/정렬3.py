
# 과학자는 논문 n편을 발표
# 이 중 h번 인용된 논문이
# h편 이상
# 나머지 논문(n-h)편은 h번 이하 인용
# h의 최댓값이 과학자의 H-index
# 최대 기준점은?

def solution(citations):
    
    citations.sort(reverse=True)
    print(citations)
    print(list(map( min, enumerate(citations, start=1) )))
    # 인용된 횟수, 몇번째로 많이 인용된 논문인지 index를 비교
    # 둘 중 더 작은 값을 mapping
    # 이렇게 만들어진 map중 가장 큰 값을 return
    answer = max( map( min, enumerate(citations, start=1) ) )
    # 천재가 아닐까?
    
    return answer


def solution1(citations):
    
    cita_sort = sorted(citations, reverse=True)
    #print(cita_sort)
    
    if cita_sort[0] == 0:
        return 0
    
    for i, c in enumerate(cita_sort, start=1):
        
        if i == c:
            return i
        
        if i < len(cita_sort) and i >= cita_sort[i]:
            return i
    else:
        return i
        

l1 = [3, 0, 6, 1, 5]
l2 = [2, 4, 3, 10, 10, 10, 10, 12]
l3 = [3, 1, 1, 1, 4]
l4 = [0, 0, 0, 0, 0, 0, 0]
l5 = [0, 0, 0, 1]
l6 = [9, 9, 9, 12]
l7 = [1, 1, 5, 7, 6,]


print(solution(l1) , 3)
print(solution(l2) , 5)
print(solution(l3) , 2)
print(solution(l4) , 0)
print(solution(l5) , 1)
print(solution(l6) , 4)
print(solution(l7) , 3)


