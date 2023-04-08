
'''
기말고사 대비를 할 수 있는 시간 t
구할 수 있는 기출문제 수 k
기출문제 미사용 과목별 시간 study
기출문제 사용 과목별 시간 pstudy

완전탐색하지 않고 주어진 시간 내 가장 많은 과목 수를 공부할 수 있는 방법은?

study, pstudy에서 가장 적은 cost인 원소들을 t 제한까지 계속 더해주기 => heap 사용
1. 같은 과목을 넣지 않게 하기 => visited 사용
2. pstudy에서 뽑은 과목 수가 k개를 넘어가지 않도록 하기

pstudy에서 과목을 뽑을 때
길이가 k인 heap 리스트(diff)에 기출문제 사용 시 save할 수 있는 시간 값을 저장

diff의 역할은
앞 탐색에서 걸리는 시간만을 보고 pstudy에 있는 과목을 수강하는 것으로 기록되었는데,
현재 탐색이랑 비교했을 때 현재 탐색에서 기출 문제 보는게 더 시간을 save할 수 있는 경우
이전에 기출과목을 수강한다 기록했던 과목을 기출미사용 과목으로 처리하고
그만큼의 시간을 계산하기 위함
이 때 기출미사용 처리되는 과목 index는 불필요
왜냐하면 diff에 저장된 시간값만 사용하면 되기 때문
'''

from heapq import heapify, heappop, heappush

def solution(t, k, study, pstudy):
    
    print('study ', study)
    print('pstudy ', pstudy)
    
    visited = [ 0 for _ in range(len(study)) ]
    diff = [ 0 for _ in range(k) ]
    
    #study_hq = heapify(study)
    #paper_hq = heapify(pstudy)
    
    # 시간 값으로 heap 정렬, index정보는 두 번째 인자로 저장
    study_hq = []
    for si, s in enumerate(study):
        heappush(study_hq, (s, si))
    print('study_hq ', study_hq)
    
    paper_hq = []
    for pi, p in enumerate(pstudy):
        heappush(paper_hq, (p, pi))
    print('paper_hq ', paper_hq)
        
    while study_hq:
        print('study_hq:{}, paper_hq:{}, diff:{}'.format(study_hq, paper_hq, diff))
        # study와 paper에서 걸리는 시간이 가장 작은 과목 비교
        # diff의 가장 작은 값을 더하면서 비교
        # 즉 이전 탐색에서 기출을 보기로한 과목을 기출미사용 처리하고,
        # 현재 과목을 기출을 본다 했을 때 걸리는 시간 값을 고려하기 위한 조건문
        # 그리고 해당 조건문은 diff의 가장 작은 값을 확인하기 때문에 0값인 경우(기출 k번사용 전)에도
        # 별도의 조건 처리 없이 사용할 수 있음
        if study_hq[0][0] > paper_hq[0][0] + diff[0]:
            c, i = paper_hq[0]
            print('?? c:{}, i:{}'.format(c, i))
            c += diff[0]
            print('c: ',c)
            heappop(diff)
            heappush(diff, study[i]-pstudy[i]) # save할 수 있는 시간 저장
            print('diff ', diff)
        else:
            c, i = study_hq[0]
            print('!! c:{}, i:{}'.format(c, i))
        
        print('c:{}, t:{}'.format(c, t))
        # 만약 t 시간을 뛰어 넘으면 break
        if c > t:
            break
        
        t -= c
        visited[i] = 1
        print('visited? ', visited)
        
        # root node가 방문한 적 있는 node면 pop
        print('1. study_hq? ',study_hq)
        while study_hq and visited[study_hq[0][1]]:
            heappop(study_hq)
        print('2. study_hq? ',study_hq)
            
        print('1. paper_hq? ',paper_hq)
        while paper_hq and visited[paper_hq[0][1]]:
            heappop(paper_hq)
        print('2. paper_hq? ',paper_hq)
    
    print(visited)
    return sum(visited)



t = 10
k = 2
study = [8, 13, 8, 9, 5]
pstudy = [1, 3, 4, 7, 4]
#print(solution(t, k, study, pstudy))


t = 100
k = 3
study = [90, 100, 90, 80, 40, 50]
pstudy = [1, 2, 3, 10, 20, 30]
print(solution(t, k, study, pstudy))

