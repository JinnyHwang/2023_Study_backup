
'''
최소 인원으로 모든 사람이 참석할 수 있게 만들기
몇 개의 모임 그래프가 나오는지 구해서 그래프 개수 더하기

순서가 중요한 문제가 아님
그리고 각 사람마다 구분되는 숫자가 명확함(중복 없음)
리스트 아닌 집합으로 구하기

=> 사람을 선택하지 않는 경우의 수는 없고, 회장과 본인 제외
1 ≤ reply[i]의 길이 ≤ reply의 길이 - 2
0 ≤ reply[i]의 원소 ≤ reply의 길이 - 1

'''

def solution(reply):
    
    # 회장인 영재(0번)을 제외한 동아리 회원 집합 생성(순서가 상관 없기 때문)
    remaining = set(range(1, len(reply))) # 모든 동아리원 번호 저장
    forward = [set(r) for r in reply] # reply를 집합으로
    reverse = [set() for _ in range(len(reply))] # i가 참석할 때 따라올 사람 수를 집합에 저장
    
    #print('forward ', forward)
    
    for ri, r in enumerate(reply):
        for rv in r:
            reverse[rv].add(ri)
    #print('reverse ', reverse)
    
    # 조건에 reply[i]는 항상 1보다 큰데 왜 필요한거지?
    leafs = [ ri for ri, r in enumerate(reply) if not r]
    #leafs = []
    #print('leafs ', leafs)
    
    
    '''
    remaining 내 원소 하나를 탐색해서 그래프 하나 확인
    해당 그래프 탐색이 끝나면 remaining에서 삭제함
    '''
    def remove_cycle():
        
        # 비지역변수 값을 중첩 함수 내에서 변경하고 싶을 때
        nonlocal remaining
        nonlocal ir
        
        # remaining 안에 있는 원소를 하나씩 탐색
        n = next(ir)
        nexts = {} # 딕셔너리
        #print('remaining: ',remaining)
        while n not in nexts: # n을 key값으로 가질 때 까지 진행
            #print('n:{}, nexts:{}'.format(n, nexts))
            nexts[n] = next(iter(forward[n]))
            #print('n:{}, nexts[n]:{}'.format(n, nexts[n]))
            n = nexts[n]
        #print('end while n:{}, nexts:{}'.format(n, nexts))
        # n이 올 때 오는 사람들을 맨 앞사람들만 확인해서 key, value로 저장
        # ex1에서 맨 처음 n이 1일 때 nexts {1: 8, 8: 4, 4: 1}
        # ex2에서 맨 처음 n이 1일 때 nexts {1: 4, 4: 3, 3: 2, 2: 1}
        
        '''
        while문 end조건이 맨 처음 설정한 key값인 n을
        value로 갖는(n = nexts[n]) key가 나타날 때 까지 반복하는 것
        즉 while문 시작하기 전 n값과 while문 끝났을 때 n값은 동일
        '''
        cycles = [n] # n으로 초기화 한 리스트
        s_f, s_r = forward[n], reverse[n] # n의 forward, reverse 집합 값을 변수 초기화
        
        # nexts를 만든 순서대로 탐색하면서 변수들을 초기화하기 위함
        while True:
            _n = nexts[cycles[-1]] # cycle의 맨 마지막 값을 key로 하는 value값을 _n에 저장
            if _n == n: # n을 value로 갖는 key값이 cycles list의 맨 마지막에 저장되면 end
                break
            # s_f, s_r 집합에 _n 집합 값도 한 번에 저장
            # nexts에는 한 사람 정보만 저장했고
            # nexts를 활용해서 모든 사람 정보를 s_f, s_r 집합에 저장
            s_f.update(forward[_n]) # cycle에 속한 사람들이 희망하는 사람 집합
            s_r.update(reverse[_n]) # cycle에 속한 사람이 올 때 참가 할 사람 집합
            cycles.append(_n)
            
        #print('cycles:{}, s_f:{}, s_r:{}'.format(cycles, s_f, s_r))
        
        cycles = set(cycles)
        
        # cycle에 속한 사람이 올 때 참가 할 사람 집합 탐색
        for i in s_r:
            # cycle에 속한 사람들이 희망하는 사람 집합 재배치
            #print('i:{}, forward[i]:{}'.format(i, forward[i]))
            forward[i] -= cycles
            forward[i].add(n)
            #print('after forward[i]:{}'.format(forward[i]))
        
        # cycle에 속한 사람들이 희망하는 사람 집합
        for i in s_f:
            # cycle에 속한 사람이 올 때 참가 할 사람 집합 재배치
            #print('i:{}, reverse[i]:{}'.format(i, reverse[i]))
            reverse[i] -= cycles
            reverse[i].add(n)
            #print('after reverse[i]:{}'.format(reverse[i]))
        
        #remaining -= cycles
        remaining -= set(cycles)
        remaining.add(n)
        #s_f -= cycles
        #s_r -= cycles
        s_f -= set(cycles)
        s_r -= set(cycles)
        
        if s_f:
            return []
        else:
            return [n]
        
    # 본인이 원하는 사람이 없는 동아리원 확인
    # 근데 문제 조건 상 이런 경우가 없는거 아닌가..
    # 반복문 진행하면서 필요함!
    def remove_leafs(leafs):
        nonlocal remaining
        to_remove = set(leafs)
        #print('leafs:{}, to_remove:{}'.format(leafs, to_remove))
        while leafs:
            leaf = leafs.pop()
            # 본인은 원하는 사람이 없는데, 본인을 원하는 사람이 있는 경우
            for p in reverse[leaf]:
                if p not in to_remove: # to_remove에 이미 속한 사람인지 확인
                    # 속하지 않은 경우 to_remove에 추가
                    leafs.append(p)
                    to_remove.add(p)
        #print('to_remove:{}, leafs:{}'.format(to_remove, leafs))
        remaining -= to_remove
        return leafs
        
    ans = len(leafs)
    #ans = 0
    length = len(remaining)
    while remaining:
        if leafs: # leafs에 값이 있는 경우 재확인
            #print('leafs yes : leafs? ', leafs)
            leafs = remove_leafs(leafs)
            #print('leafs yes : after leafs? ', leafs)
        else:
            ir = iter(remaining)
            #print('leafs no')
            leafs = remove_cycle()
            #print('leafs no : after leafs? ', leafs)
            ans += len(leafs)
        
        if len(remaining) >= length:
            raise ValueError
        length = len(remaining)
        #print('end remaining:{}, length:{}'.format(remaining, length))
        
    return ans


r1 = [[0], [8], [1, 3], [2], [1], [1, 4, 6], [2, 5], [3, 6], [4]]
print(solution(r1))


r2 = [[0], [4], [1], [2], [3]]
print(solution(r2))



