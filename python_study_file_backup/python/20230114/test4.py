import copy

satisfy_max = 0

def who_can_eat(satisfy, cant_eat, cal_satisfy, cnt_k, k):
    global satisfy_max

    #print('\n cnt_k? ', cnt_k, ' cant_eat? ', cant_eat, ' cal_satisfy? ',cal_satisfy)

    if cnt_k == k or 0 not in cant_eat:
        print('last satisfy? ', cal_satisfy)
        satisfy_max = max(satisfy_max, cal_satisfy)
        return

    # 다른 방법은?
    for si in range(len(satisfy)):
        #print('si? ', si, 'cant_eat? ', cant_eat)
        if cant_eat[si] == 0:
            cant_eat_cp = copy.deepcopy(cant_eat)
            #print('1 cant_eat_cp? ', cant_eat_cp)
            cant_eat_cp[si], cant_eat_cp[si-1] = 1, -1
            if si+1 == len(satisfy):
                cant_eat_cp[0] = -1
            else:
                cant_eat_cp[si+1] = -1
            #print('2 cant_eat_cp? ', cant_eat_cp)
            who_can_eat(satisfy, cant_eat_cp, cal_satisfy + satisfy[si], cnt_k+1, k)


def solution(satisfy, k):

    # 최상의 만족도는?
    global satisfy_max
    # 1명이 식사를하면 양 옆 젓가락을 사용. 양 옆 사람은 식사를 할 수 없음
    # 준비된 식사 수 k가 주어짐
    # 식사수는 철학자수/2 이기 때문에 식사가 남는 경우 생각하지 않아도 됨. 아님..
    
    # 만족도 누적
    # 식사를 못하는 사람을 기록
    # 식사한 사람 1, 식사못하는 사람 -1
    
    #satisfy = [5, 4, 4, 6, 2, 1, 3]
    #k = 3
    satisfy = [10, 1, 1, 10, 1, 1, 10, 1]
    k = 4
    
    cant_eat = [ 0 for _ in range(len(satisfy))]

    who_can_eat(satisfy, cant_eat, 0, 0, k)

    #print(cant_eat)
    #print(satisfy_max)

    return satisfy_max


print(solution([], 0))

