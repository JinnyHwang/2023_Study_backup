
'''
한 사람당 티셔츠 최대 1개
모든 참가자는 자신의 상의 크기와 같거나 큰 티셔츠를 받을 수 있다.

최대한 많은 참가자에게 티셔츠를 주는 것이 목표

내 생각에는...
1. 최대한 정사이즈 나눠주기
2. 큰사이즈 사람부터 탐색하면서 티 나눠주기.
상이 작은 사람은 선택지가 더 많으니까 선택지가 작은 사람 먼저 배분
'''
def solution(people, tshirts):
    
    people = [1, 2, 3, 3, 4, 4]
    tshirts = [2, 3, 2, 2, 3, 4]
    
    # 특정 상을 받은 사람 수를 저장하는 dic
    p_dic = {}
    for p in people:
        p_dic[p] = p_dic.get(p, 0) + 1
    print(p_dic)
    
    # 남은 티셔츠 수를 저장하는 dic
    t_dic = {}
    for t in tshirts:
        t_dic[t] = t_dic.get(t, 0) + 1
    print(t_dic)
    
    # 정사이즈 티셔츠 먼저 나눠주기
    for k in p_dic:
        if k in t_dic:
            if p_dic[k] <= t_dic[k]:
                t_dic[k] -= p_dic[k]
                p_dic[k] = 0
            else:
                p_dic[k] -= t_dic[k]
                t_dic[k] = 0
    
    print(p_dic)
    print(t_dic)
    
    p_k_list = [ k for k in sorted(p_dic, reverse=True) if p_dic[k] > 0 ]
    print(p_k_list)
    
    t_k_list = [ k for k in sorted(t_dic, reverse=True) if t_dic[k] > 0 ]
    print(t_k_list)
    
    for pk in p_k_list:
        for tk in t_k_list:
            if pk <= tk: #티셔츠를 받을 수 있는 경우
                if p_dic[pk] <= t_dic[tk]:
                    t_dic[tk] -= p_dic[pk]
                    p_dic[pk] = 0
                else:
                    p_dic[pk] -= t_dic[tk]
                    t_dic[tk] = 0
            else:
                break
    
    print(p_dic)
    print(t_dic)
    
    remain_p = sum( v for k,v in p_dic.items() if v > 0 )
    print(remain_p)
    
    
    return len(people)-remain_p

print(solution([],[]))
