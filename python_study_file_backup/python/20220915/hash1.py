
'''
자료구조, 알고리즘 선택
만약 이름(string) 대신 번호가 주어졌으면?
index로 접근할 수 있기 때문에 배열 사용이 용이
그러나 string을 쓰기에는 가능한 모든 이름의 조합의 수가 어마무시.. 비휴율.. runtime error 뜰 듯
번호 말고 다른것(ex.string)으로 접근하기 좋은 자료 구조는? 해쉬

해쉬테이블에 key로 값을 맵핑
해쉬테이블에 맵핑은 hash function으로
=> 자료구조에서 자세히 배울 수 있음
'''

'''
해쉬문제1
이름을 key , value는 사람의 숫자
value count해서 0이 아닌 value를 갖는 key가 답

파이썬에서 dictionary가 해쉬를 사용한 자료형
'''

d = {"leo":30 , "kiki":50, "eden":43 }

print(d["leo"])
d["leo"] = 35
print(d["leo"])


def solution(participant, completion):
    d = {}
    
    for x in participant:
        d[x] = d.get(x, 0) + 1
        
    for x in completion:
        d[x] -= 1

    answer = [ k for k,v in d.items() if v > 0 ]

    return answer[0]


p1 = ["leo", "kiki", "eden"]
c1 = ["eden", "kiki"]
print(solution(p1,c1))

p2 = ["marina", "josipa", "nikola", "vinko", "filipa"]
c2 = ["josipa", "filipa", "marina", "nikola"]
print(solution(p2,c2))

p3 = ["mislav", "stanko", "mislav", "ana"]
c3 = ["stanko", "ana", "mislav"]
print(solution(p3,c3))


'''
알고리즘의 복잡도는?

리스트 안 원소를 탐색해서 dictionary를 접근
-> 상수시간에 접근 가능
N에 비례하는 복잡도를 가진다

answer = [ k for k,v in d.items() if v > 0 ]
=> 사전의 크기에 비례하는 시간 복잡도를 가진다

participant의 원소 개수를 N이라 가정
hash를 사용한 위 풀이는
N에 linear한 복잡도를 가짐
'''


'''
만약 정렬을 사용한다면?

원소를 하나하나씩 확인해서 차이가 나는 부분을 찾는 방법
1. participant 정렬
2. completion 정렬
3. participant, completion 비교

sort는 Nlog(N)의 복잡도를 가짐
'''
