
def solution(participant, completion):
    d = {}
    
    for x in participant:
        d[x] = d.get(x, 0) + 1
    
    for x in completion:
        d[x] -= 1
    
    # 단 한 명만 value 1값을 가지고 있음
    # 딱 한 명의 이름이 배열에 저장
    dnf = [ k for k,v in d.items() if v > 0 ]
    
    return dnf[0]

p = ["bb","aa","ki"]
c = ["bb","ki"]

print(solution(p, c))





