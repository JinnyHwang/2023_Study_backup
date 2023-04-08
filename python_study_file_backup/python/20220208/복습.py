
def solution_hash(participant, completion):
    answer = ''
    dic = {}
    
    for x in participant:
        dic[x] = dic.get(x, 0) + 1
        
    for x in completion:
        dic[x] -= 1
        
    who = [ name for name, val in dic.items() if val > 0 ]
    answer = who[0]
    
    return answer


def solution_greedy(n, lost, reserve):
    # 안쓰는 index 0, n+1도 초기화
    stu = [1]*(n+2)
    
    for i in reserve:
        stu[i] += 1
        
    for i in lost:
        stu[i] -= 1
        
    for i in range(1, n+1):
        if stu[i] == 2 and stu[i-1] == 0:
            stu[i-1:i+1] = [1, 1]
        elif stu[i] == 2 and stu[i+1] == 0:
            stu[i:i+2] = [1, 1]
            
    answer = len([ x for x in stu[1:-1] if x > 0])    
    return answer

# 집합으로 풀기
def solution_greedy2(n, lost, reserve):
    
    del_p = set(reserve) & set(lost) #교집합
    
    r = set(reserve) - del_p
    l = set(lost) - del_p
    
    sort(r)
    
    for x in r:
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
    
    return n-len(l)

def solution_greedy3(numbers):
    
    # 최종적으로 문자열로 만들어야함, 비교도 문자열로
    numbers = [ str(x) for x in numbers ]
    
    numbers.sort( key=lambda x: (x*4)[:4], reserve=True )
    
    if numbers[0] == '0':
        answer = '0'
    else:
        # 구분자 없이 이어붙이기
        answer = ''.join(numbers)
    
    return answer

import heapq
'''
리스트 datatype을 sort처럼 정렬하는 것
heapq.heapify(scoville) 의 의미는
리스트 scoville을 min heap으로 정렬하겠다는 의미
datatype 변화 없이 리스트 타입임.
'''

def solution_heap(scoville, K):
    
    answer = 0
    '''
    리스트를 min heap 정렬
    연산이 끝나는 조건
    1. 남아있는 원소 중 가장 작은 값이 k 이상일 때
    2. 힙에 남아있는 값이 1개 일 때
    return 연산 횟수
    반복적으로 음식을 섞어야 함
    '''
    
    # min heap 으로 정렬
    heapq.heapify(scoville)
    
    while True:
        min1 = heapq.heappop(scoville)
        
        if min1 >= K:
            break
        elif len(scovile) == 0:
            break
        else:
            min2 = heapq.heappop(scoville)
            new = min1 + (min2*2)
            heapq.heappush(scoville, new)
            answer += 1
    return answer






















