'''
각 월에 제작해야하는 자전거 수를 구하기
최종적으로 retrun 하는 값은 자전거 생산을 위한 전기 요금 값
전기값 계산전에
최적의 월 별 자전거 생산 수량을 구하는 것이 우선이다

만들어야 하는 자전거 수는 납기를 맞추면서 앞 뒤로 골고루 분배해야한다

문제에서 주어지는 order 리스트 원소의 0번째 값은 month 정보를 담고있는데,
month 정보를 생산 기한. 구간 값으로 변경

주어지는 order는 정렬되어 있지 않고
month 정보는 중복될 수 있다
order = [[3,50], [7,200], [8,200]]
_order = [[3,50], [4,200], [1,200]]

순차적으로 확인하면서 뒷쪽의 월 별 제작해야하는 자전거 수가 더 많은 경우 앞쪽과 합쳐줌
[3,50], [4,200] => [7,250]
stack = [[7,250], [1,200]]

최종적으로 구해진 stack list에 맞춰 누진세 구하기

'''
def solution(cost, order): # 풀이 안보고 혼자 작성 한 code.
    
    cost = [[0,10], [50,20], [100,30], [200,40]]
    order = [[8,200], [3,500], [7,200], [3,200]]
    #order = [[3,50], [7,200], [8,200]]
    
    # order 순차적으로 정렬
    #order.sort()
    
    # month를 구간으로 변경한 _order를 구하기
    #_order = [order[0]] # 기준 값을 위해 0번째 값으로 초기화
    
    #for oi, ov in enumerate(order):
        #ov[0] : month / ov[1] : 자전거 수
        # month가 같은 경우는 어떻게 처리할까?
    
    # order를 month를 key로 값는 dic으로 만들고 sort할까?
    order_dic = {}
    for o in order:
        order_dic[o[0]] = order_dic.get(o[0], 0) + o[1]
    print(order_dic)
    #order_dic.sort()
    print(sorted(order_dic))
    print(order_dic)
    
    month = [ m for m in sorted(order_dic) ]
    print(month)
    
    # 맨 처음은 초기화
    _order = [[month[0], order_dic[month[0]]]]
    print(_order)
    for i in range(1, len(month)):
        _order.append([month[i] - month[i-1], order_dic[month[i]]])
    print(_order)
    # 뭔가 _order구하는 code가 더러움...
    
    # 값을 반복 비교해서 합치기
    stack = [_order[0]]
    print(stack)
    
    # stack의 맨 끝 원소와 값비교
    # 만약 _order 원소의 월 제작해야하는 자전거 수가 더 많은 경우
    # stack 원소 pop하고 다시 append 해줌
    # stack 맨 끝 원소의 생산량이 더 크면 그냥 append
    for i in range(1, len(_order)):
        s_make = stack[-1][1]/stack[-1][0]
        o_make = _order[i][1]/_order[i][0]
        print('s_make %d, o_make %d'%(s_make, o_make))
        
        if s_make < o_make:
            s_v = stack.pop()
            stack.append([s_v[0]+_order[i][0], s_v[1]+_order[i][1]])
            print('?',i, stack)
        else:
            stack.append(_order[i])
            print('!',i, stack)
        
    print(stack)
    
    # stack 값을 확인해서 전기값 계산
    # cost 정보의 생산대수 정보를 구간 값으로 변경
    _cost = [cost[0]]
    for ci in range(1, len(cost)):
        _cost.append([cost[ci][0]-cost[ci-1][0], cost[ci][1]])
    print(_cost)
    
    total_cost = 0
    for sv in stack:
        #sv[0] # 기한
        sv1_copy = sv[1] # 생산대수
        print('stack value? ',sv[0], sv[1])
        
        for ci in range(1,len(_cost)): # cost 생산 대수에 sv[0]값을 곱해서 기한동안 만들 수 있는 자전거 대수로 계산
            possible_make = _cost[ci][0] * sv[0]
            print(ci,' cost? ', _cost[ci], '\n possible_make? ', possible_make)
            if sv1_copy//possible_make == 0 or ci == len(_cost)-1:
                total_cost += sv1_copy*_cost[ci-1][1]
                print('!! sv1_copy? ', sv1_copy, ' total_cost? ', total_cost)
                break
            else:
                total_cost += possible_make*_cost[ci-1][1]
                sv1_copy -= possible_make
                print('?? total_cost? ', total_cost, ' sv1_copy? ', sv1_copy)
    
    print(total_cost)
    
        
        
        
        
    
    
    
    answer = 0
    return answer


print(solution([], []))


