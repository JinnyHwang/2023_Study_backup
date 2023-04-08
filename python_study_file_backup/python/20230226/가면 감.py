
'''
최소 인원으로 모든 사람이 참석할 수 있게 만들기
몇 개의 모임 그래프가 나오는지 구해서 그래프 개수 더하기

순서가 중요한 문제가 아님
그리고 각 사람마다 구분되는 숫자가 명확함(중복 없음)
리스트 아닌 집합으로 구하기


'''

def solution(reply):
    
    # 회장인 영재(0번)을 제외한 동아리 회원 집합 생성
    remaining = set(range(1, len(reply)))
    forward = [set(r) for r in reply] # reply를 집합으로
    reverse = [ set() for _ in range(len(reply))] # i가 참석할 때 따라올 사람 수를 집합에 저장
    
    print('forward ', forward)
    
    for ri, r in enumerate(reply):
        for rv in r:
            reverse[rv].add(ri)
    print('reverse ', reverse)
    
    # 조건에 reply[i]는 항상 1보다 큰데 왜 필요한거지?
    leafs = [ ri for ri, r in enumerate(reply) if not r]
    print('leafs ', leafs)
        
    
    
    return 0











reply = [[0], [8], [1, 3], [2], [1], [1, 4, 6], [2, 5], [3, 6], [4]]
print(solution(reply))


reply =[[0], [4], [1], [2], [3]]
print(solution(reply))

