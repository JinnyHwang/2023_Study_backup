'''

탐욕법(Greedy)

가능한 많은 학생이 수업을 들을 수 있도록

탐욕법 Greedy Algorithm
알고리즘 각 단계에서 그 순간에 최적이라 생각되는 것 선택
탐욕법으로 최적해를 찾을 수 있는 문제는?
현재의 선택이 마지막 해답의 최적성을 해치지 않을 때

탐욕법 적용 가능성 확인.

   2   4   6
1   3   5
=> 체육복을 빌려줄 학생들을 "정해진 순서"로 살피기
"정해진 순서"에 따라 우선하여 빌려줄 방향 정하기


(해결 방법1)
학생의 수는 기껏해야 30
학생 수 만큼 배열 확보, 각자 가지고 있는 체육복 수 기록
-> 번호 순서대로 스캔하면서 빌려줄 관계 정하기

알고리즘 복잡도는?
여벌을 가져온 학생 처리: reserve 길이에 비례
체육복 잃어버린 학생 처리: lost 길이에 비례
체육복 빌려주기 처리: 전체 학생 수 N에 비례
=> 즉, 상수시간 O(N)
==> 해당 방법은 N 크기가 매우 커지면 복잡도 증가
만약 학생 수가 매우 크다면? 또는 여벌의 체육복을 가져온 학생이 매우 적다면?
'''
def solution1(n, lost, reserve):
    
    u = [ 1 for _ in range(n+2) ]
    
    for i in reserve: # N에 비례
        u[i] += 1
        
    for i in lost: # N에 비례
        u[i] -= 1
    
    for i in range(1, n+1): # N회 반복
        if u[i] == 2 and u[i-1] == 0 :
            u[i-1:i+1] = [1,1]
        elif u[i] == 2 and u[i+1] == 0:
            u[i:i+2] = [1,1]
    
    return len([x for x in u[1:-1] if x > 0]) # N회 반복
# 전체 알고리즘은 N에 비례 : O(N)



'''
(해결 방법2)
여벌 체육복 가져온 학생들의 번호 '정렬'
하나하나 순서대로 살피면서 '빌려줄 수 있는 다른 학생 찾아서' 처리
-> 여벌 체육복 가져온 학생 수 : k
'정렬'이 들어가기 때문에 시간복잡도는O(klogk)
'빌려줄 수 있는 다른 학생 찾아서'는 해시를 적용해서 상수시간에 처리하기
==> 만약 N과 k값 차이가 비슷하다면 방법1보다 시간복잡도가 크지만,
보다 다양한 상황에서 사용할 수 있다

알고리즘 복잡도는?
여벌의 체육복을 가져온 학생들의 번호(reserve) 정렬 => O(klogk)
체육복을 빌려줄 수 있는 학생을 찾아 처리 => O(k)*O(1)
=> 빌려줄 수 있는 학생이 집합에 속해 있는지 아닌지는 상수시간에 처리할 수 있다(hash)
즉, 전체 알고리즘 시간 복잡도는 O(klogk)
-> N이 매우 크고, k는 작아서 O(N)보다 O(klogk)가 유리할 때 사용함.
'''
# 집합 사용 set() : hash
# dictionary와 달리 key, value없이 해당 원소가 집합에 속해 있는지 아닌지만.    
def solution2(n, lost, reserve):
    
    s = set(lost) & set(reserve)
    l = set(lost) - s # 체육복 빌려야 하는 학생들
    r = set(reserve) - s # 체육복 빌려줄 수 있는 학생들
    
    for x in sorted(r): # O(klogk)
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remover(x+1)
    
    # 체육복 못빌린 학생 빼기
    return n-len(l)


