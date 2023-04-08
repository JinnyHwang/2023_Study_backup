'''
접근법.. 정말 다양한 경우의수를 고려해야하는구나..

1. 만족도가 가장 높은 사람이 식사

2. 만족도가 가장 높은 사람이 식사 안 함. 양옆 사람이 꼭 식사를 해야 이득
만족도가 가장 높은 사람의 옆자리는 만족도가 작은 사람들.
만족도가 작은 사람 '하나만' 식사를 하는 경우 만족도가 가장 높은 사람이 식사를 하지 못함
만족도가 가장 높은 사람이 식사하는 경우보다 무조건 만족도가 낮음
따라서 만족도가 가장 높은 사람이 식사를 포기하는 경우, 양옆 사람이 모두 식사를 해야
비교하는 의미가 있음


만족도 가장 높은 사람 VS (만가높 양옆사람 만족도 합)

최대의 만족도를 구하는 계산식은
각 단계에서 구할 수 있는 최대의 만족도는
만족도 가장 높은 사람 + a(양옆사람 만족도 합이 더 큰 경우)

만족도 비교할 때
해당 비교 리스트에서 가장 높은 만족도를 더하면서 누적
만약 양옆 사람이 식사할 때 만족도가 더 높으면? (만가높 양옆사람 만족도 합) - (만족도 가장 높은 사람 값) 더함
(만가높 양옆사람 만족도 합) - (만족도 가장 높은 사람 값) 결과값이 마이너스인 경우는 만가높 사람을 선택하는게 이득이라는 뜻

비교가 끝나는 순간은?
1. k 횟수 소진 시
2. 비교 리스트에 마이너스 값만 남은 경우
'''

def solution1(satisfy, k): # 해설만 보고 직접 작성. 테케 1번만 성공. 나머지 시간초과
    
    total_satisfy = 0
    
    #satisfy = [1, 2, 3, 4, 5, 6, 10]
    #print(satisfy.index(max(satisfy)))
    
    for _ in range(k):
        
        if max(satisfy) < 0 :
            break
            
        si = satisfy.index(max(satisfy))
            
        total_satisfy += satisfy[si]
        
        if si+1 == len(satisfy):
            satisfy[si] = (satisfy[si-1]+satisfy[0] - satisfy[si])
            satisfy.pop(si-1)
            satisfy.pop(0)
        else:
            satisfy[si] = (satisfy[si-1]+satisfy[si+1] - satisfy[si])
            satisfy.pop(si+1)
            satisfy.pop(si-1)
        #print(satisfy)  
    #print(total_satisfy)
        
    return total_satisfy

# heapq 완전이진트리 사용
import heapq

def solution(satisfy, k):
    
    n = len(satisfy)
    l = list(range(-1, n-1)) # 왼쪽 index
    r = list(range(1, n+1)) # 오른쪽 index
    # out of range를 방지하기 위함.
    l[0] = n-1 # 식사하는 철학자 index가 0일 때, 왼쪽 사람은 n-1번째 사람
    r[n-1] = 0 # 식사하는 철학자 index가 n-1일 때, 오른쪽 사람은 0번째 사람
    visit = [ 0 for _ in range(n) ] # 식사를 할 수 있는가?
    
    hq = [ (-s, i) for i, s in enumerate(satisfy)] # 만족도에 - 처리
    heapq.heapify(hq) # queue형태로 변경
    
    total_s = 0
    while hq and k: # 리스트 안에 값이 있거나, k가 0이 아닐 때
        s, si = heapq.heappop(hq) # s는 마이너스 값
        if visit[si]: # 방문했으면 pass
            continue
            
        total_s -= s
        satisfy[si] = satisfy[l[si]] + satisfy[r[si]] - satisfy[si]
        if satisfy[si] > 0: # 양옆사람 식사할 때 만족도가 더 큰 경우
            # 해당 값으로 이어서 비교 진행
            heapq.heappush(hq, (-satisfy[si], si))
        visit[l[si]] = visit[r[si]] = 1
        
        # 왼오 index 표시 배열 조정. 탐색한 index의 양옆을 한 칸씩 더 옆으로 조정
        # 탐색한 index는 사용되지 않을 것
        l[si] = l[l[si]] # si 왼쪽값은 왼쪽의왼쪽
        r[si] = r[r[si]] # si 오른쪽값은 오른쪽의오른쪽
        l[r[si]] = si # 오른쪽 값의 왼쪽
        r[l[si]] = si # 왼쪽 값의 오른쪽
        k -= 1

    return total_s
