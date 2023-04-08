
'''
해당 문제에는 어떤 알고리즘이 적합한지?
문제를 파악하고 직접 해결해보기
문제의 크기, 제약, 조건이 무엇인지?

1. 완주하지 못한 선수

1 <= participant <= 10^5
N or NlogN 으로 풀어나가면 좋다

조건: 동명이인이 존재

name이 주어졌을 때 해당 name이 몇 번 등장했는가? 중요함
-> hash와 연관되어 있다

자료구조(알고리즘) 선택

만약 이름 대신 번호가 주어졌다면?
=> 최대 크기 10만인 배열에 완주 여부 저장

그런데 이름이 주어짐.
가능한 모든 이름의 조합.. 26개 알파벳에 최대 20개 알파벳 사용 가능.. 대략 26^20
=> 배열 불가능

그럼 문자열로 접근하기 좋은 자료형은?
=> 정수로 주어지는 인덱스로 접근하는 것 말고..

Hash(해시)
key값으로 hash table(value 저장) 접근
-> 각 key값은 hash function을 통해 hash table에 mapping됨?

같은 hash table에 다른 key값이 mapping되는 경우 존재. (충돌)
충돌은 반드시 해결해야 하는데, 충돌이 발생하는 경우에는 몇 가지 해결 방법이 있음
같은 칸에 옆으로 다른 bucket을 늘어놓기 등..
=> hash function을 만들 때 알아야함


(예제 풀이 방법)
hash 사용
key : name / value : name 등장 횟수

python data type 중 dictionary를 사용
-> hash를 사용해서 data에 접근하기 때문에
상수시간 O(1) 시간에 접근 가능하다
dic = {"leo":30, "kiki":12, "eden":3}

participant에 몇 번 나왔는지 count / completion에 나온 만큼 차감
'''
def solution(participant, completion):
    d = {}
    
    for x in participant:
        d[x] = d.get(x, 0) + 1
    
    for x in completion:
        d[x] -= 1
    
    dnf = [ k for k,v in d.items() if v > 0 ]
    
    return dnf[0]
'''
알고리즘의 복잡도?
2개 순환문

리스트 원소 각각에 대해서 key값으로 사용해서 hash table에 접근함
즉, 시간복잡도는 participant, completion 배열 길이에 비례함.
마라톤에 참가한 수 N : O(N)

dnf = [ k for k,v in d.items() if v > 0 ]
=> dictionary의 크기에 비례함. participant 배열과 길이 동일

=> 즉, 마라톤에 참가한 수 N에 비례하는 linear

!다른 풀이 방법
정렬 이용
participant, completion를 정렬해서 각 index 원소 value 비교
sort()의 시간복잡도는? 최적의 정렬 상황이여도 O(NlogN)
'''



