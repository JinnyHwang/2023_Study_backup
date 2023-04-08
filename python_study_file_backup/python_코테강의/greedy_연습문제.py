'''
탐욕법 (Greedy Algorithm)
반복을해서 처리할 때 그 순간에 지역적으로,
자기 자신의 주변만보면서 최적이라 생각되는 것을 선택하는 것

알고리즘의 각 단계에서 그 순간 최적이라 생각되는 것을 선택
현재의 선택이 마지막 해답의 최적성을 해치지 않을 때 사용

!탐욕법 적용 가능성 확인

정해진 순서로 살피고,
정해진 순서에 따라 우선해서 빌려줄 방향을 정함

학생수는 최대 30 -> 적음
학생 수만큼 배열 확보
각자 가지고 있는 체육복 수 기록
번호 순서대로 스캔하면서 빌려줄 관계 정함

n =  학생 수
lost
reserve
'''

'''
[방법1]
1. 모든 학생이 체육복을 하나씩 가지고 있다고 가정
2. 1~10 학생을 탐색.
-> 편의를 위해 앞뒤에 0, 11 인덱스 여유롭게 사용
3. 번호가 작은쪽으로 주걸 먼저 확인하는 방향이 유리.
-> 모든 상황에 적용되는 규칙

알고리즘 복잡도
여벌을 가져온 학생 : reserve 길이에 비례
잃어버린 학생 : lost 길이에 비례
-> N을 넘을 수 없음
빌려주기 처리 : 전체학생수 N에 비례
--> O(n) : liner 복잡도
'''

'''
[방법2]
만약 전체 학생수가 크면?
그리고 여벌 체육복 가져온 학생이 매우 적으면?
아니면 도난당한 학생이 매우 적으면?
1)배열을 수 없이 많이 만들어야함
2)불필요한 실핼시간 낭비됨

1. 여벌의 체육복 가져온 학생 번호 정렬
2. 하나하나 순서대로 살펴보면서,
빌려줄 수 있는 학생을 찾아서 처리 -> 해시 적용해서 상수시간에 처리.
시간복잡도 : O(klogk)
-> 극단적인 경우일 때 유리.

알고리즘 복잡도
여벌을 가져온 학생 : O(klogk)
체육복을 빌려줄 수 있는 학생을 찾아 처리 : O(k) * O(1)
-> 학생을 찾는 것, 해시테이블 이용해서 상수 시간에 처리 가능
즉 O(klogk)
'''

# 방법1
def solution1(n, lost, reserve):
    
    # 0~n+1 1로 초기화한 리스트
    u = [1]*(n+2)
    
    for i in reserve:
        u[i] += 1
        
    for i in lost:
        u[i] -= 1
        
    for i in range(1, n+1):
        if u[i-1] == 0 and u[i] == 2:
            # 리스트 i-1, i 인덱스 값 초기화(슬라이서이용)
            u[i-1:i+1] = [1, 1]
        elif u[i] == 2 and u[i+1] == 0:
            u[i:i+2] = [1, 1]
        
    # u[1:] : 맨 끝까지, u[1:-1] : 맨끝-1 까지.
    # 1~n index 탐색하는데 값이 0이상인 원소의 리스트 제작.
    # 이렇게 새롭게 만들어지는 리스트의 len
    return len([x for x in u[1:-1] if x > 0])

#print(solution(10, [1, 3, 5], [2, 6]))

# 방법2
# datatype set(집합) : 해시테이블로 구현되어 있어서 key 접근 시간이 상수시간.
# dictionary와 다른 점은? 사전은 key에 대해 value가 map 되어 있음
# set은 어떤 원소가 이 집합에 속해 있는지 아닌지 상관하는 자료구조
# set : 순서의미X, 중복제거
def solution2(n, lost, reserve):
    # set datatype을 가진 두 집합의 교집합
    # set의 시간 복잡도는 배열의 길이에 비례
    # 여분 있으면서 잃어버린 학생
    s = set(lost) & set(reserve)
    
    # 체육복을 빌려야하는 집합
    l = set(lost) - s
    # 체육복 빌려줄 수 있는 집합
    r = set(reserve) - s
    
    # soted(r) : r을 오름차순으로 sorting한 리스트
    # r1 = sort(r) : r1은 r이 오름차순으로 sort된 리스트
    # 내림차순 : reverse()/reversed()
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
        
    # 전체 수에서 체육복을 빌리지 못한 학생 수를 뺌
    return n-len(l)
        
#print(solution2(10, [1, 3, 5], [2, 6]))


def solution1_2(n, lost, reserve):
    # 모든 학생이 체육복이 있는 상태를 우선 만든다
    # 체육복이 없는 학생은 0
    # 체육복 여분이 있는 학생은 2
    # 본인 체육복만 있는 학생은 1
    
    #안쓰는 index 0, n+1도 1로 초기화
    stu = [1]*(n+2) # 0~n+1 index를 가지는 리스트
    
    # 여분이 있는 학생 우선 조사
    for i in reserve:
        stu[i] += 1
    
    # 도난당한 학생 조사
    for i in lost:
        stu[i] -= 1
        
    # 체육복 분배
    # 체격순으로 번호 정렬되어 있음
    # 앞뒤로 빌려줄 수 있음
    # 앞순서 먼저 빌려주는 것이 최대한 많은 학생들을 빌려줄 수 있음
    # 뒷순서 먼저 빌려주는 경우는
    # 맨 처음 학생이 체육복이 없거나, 맨 마지막 학생이 여분이 있는 경우
    # 손해인 상황이 생길 수 있음
    for i in range(1, n+1):
        if stu[i] == 2 and stu[i-1] == 0:
            # i-1 ~ i 라는 뜻 리스트로 초기화
            stu[i-1:i+1] = [1, 1]
        elif stu[i] == 2 and stu[i+1] == 0:
            # i ~ i+1 범위의 리스트 초기화
            stu[i:i+2] = [1, 1]
    
    # 체육복이 있는 학생 리스트
    # 해당 리스트의 크기는 len()으로 구한다.
    answer = len([ x for x in stu[1:-1] if x > 0 ])
    
    return answer


# lost, reserve list를 보고
# reserve가 빌려줄 수 있는 사람이 lost에 있는가 확인 (앞순서 우선 확인)
# 이 반대로 lost가 reserve에서 빌릴 수 있는 사람이 있는지 확인 (뒷순서 우선 확인)
# reserve, lost에 모두 속한 사람은 계산에서 빼기
# 중복 없고 순서가 무의미하기 때문에 집합 datatype인 set 사용
def solution2_2(n, lost, reserve):
    
    # 계산에서 제외 할 reserve, lost에 모두 속한 사람
    del_p = set(reserve) & set(lost) # 교집합
    # 체욱복 빌려줄 수 있는 사람
    r = set(reserve) - del_p
    # 체육복을 빌려야하는 사람
    l = set(lost) - del_p
    
    # 체육복이 없는 사람을 찾을 것
    # 빌려줄 수 있는 사람을 확인, 체육복 받은 사람을 집합에서 제외
    # 체격순으로 탐색하기 위해 빌려줄 사람 체격순으로 정렬
    sorted(r) # sort를 거쳐서 datatype set -> list형으로 순서가 유의미해짐
    
    for x in  r:
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
    
    # 체육복이 없는 사람의 수 : len(l)
    # 체육복이 있는 사람의 수
    return n - len(l)








