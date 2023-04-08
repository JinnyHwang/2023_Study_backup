
# 참가자 중 동명이인이 있을 수 있음
# 특정 이름을 가진 사람의 수를 count

# 어떤 알고리즘을 적용할 것인가?

'''
[해시 개념]

만약 이름 대신 번호가 주어짐
-> 선형 배열(linear array)
최대 크기 10만
인덱스를 사용해 바로 배열에 접근할 수 있기 때문
배열을 이용하면 번호를 인덱스로 사용하기 쉽기 때문!

1~20자리의 알파벳 소문자 가지는 이름
가능한 이름의 모든 조합의 수를 배열로 선언해서
이용하기엔 원소가 과하게 많음. 비효율적!

배열의 인덱스 말고 문자열로 접근할 수 있는 방법은?
-> 해시(Hash)

Key, Hash table
key가 어떤 hash table있는지
index 대신에 key를 이용

각 key를 hash table에 맵핑하는 것은 hash function을 이용함
가급적 key가 서로 다른 칸에 사상되도록... 보장할 순 없지만!
해시 버킷(hash bucket) :  해시테이블 내의 각각의 칸
해시 버킷의 수가 많을 수록 서로 다른 key가 서로 다른 칸에 사상될 확률이 높아질 것

만약 다른 key가 같은 칸을 가리킬 때? 같은 칸에 사상될 경우
해시 충돌(hash collision) -> 해결해야함
해당 칸 옆으로 다른 버킷을 연달아 놓아서 각 key를 구분질 수 있게 해야함
'''

'''
Python dictionary
dictionary 원소들을 해시를 이용해 시간복잡도 O(1)(상수시간)로 접근 가능
dictionary을 구현할 때 내부적으로 해시테이블을 이용하기 때문에
dictionary 원소들을 해시를 이용해 상수시간에 접근 가능

d = {"leo":30, "kiki":62, "eden":5}
x = d["leo"]
d["leo"] = 58
'''

'''
동명이인 처리는?

participant 참가자
completion 완주자

participant 이름이 몇번 나왔는지 count,
completion에 나온 이름 count 감소
'''

# 파이썬 딕셔너리는
# x가 key값에 없을 경우 get()에서 설정한 default 값인 0 +  1이 들어간다.
# 만약 x라는 key가 있다면 dictionary에 저장된 값 + 1
# d dictionary에 x라는 key가 없을 때 d[x]를 쓰면,
# d dictionary에 x key가 추가
# 시간복잡도 O(N)
def solution(participant, completion):
    d = {}
    for x in participant:
        # x가 key값에 없을 경우 get()에서 설정한 default 값인 0 +  1이 들어간다.
        # 만약 x라는 key가 있다면 dictionary에 저장된 값 + 1
        # d dictionary에 x라는 key가 없을 때 d[x]를 쓰면,
        # d dictionary에 x key가 추가
        d[x] = d.get(x, 0) + 1
    print("1 : ", list(d.values()))
    
    for x in completion:
        d[x] -= 1
    print("2 : ", list(d.values()))
    
    # dnf : did not finish
    
    # 사전 크기에 비례하는 복잡도를 가짐.
    # 해쉬 테이블이 키를 기준으로 해시 테일블을 상수 시간에 읽고 씀.
    dnf = [ key for key, val in d.items() if val > 0 ]
    answer = dnf[0]
    
    return answer

# 정렬을 이용
# 시간 복잡도는
# 2행과 3행의 배열들을 크기 순으로 정렬 하는 연산은
# sorting 최적 알고리즘도 O(NlogN) 복잡도를 가짐
# 시간 복잡도 너무 큼 -> 별로!
# 해시를 이용한 구성이 좋
def solution2(participant, completion):
    participant.sort()
    completion.sort()
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    return participant[len(participant)-1]



participant = ['leo', 'kiki', 'leo', 'eden']
completion = ['kiki', 'leo', 'eden']
print(solution(participant, completion))

