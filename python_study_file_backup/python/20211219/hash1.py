# dictionary 연습
wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
    }

def rsp(mine, yours):
    if mine == yours:
        return 'draw'
    elif wintable[mine] == yours:
        return 'win'
    else :
        return 'lose'

result = rsp('가위','바위')

messages = {
    'win':'이겼다',
    'draw':'비겼다',
    'lose':'졌다'
    }

print(messages[result])


list = [1, 2, 3, 4, 5]
print(list)

list[2] = 33
print(list)

list.append(6)
print(list)

dict = {'one':1, 'two':2}
print(dict)

dict['three'] = 3
print(dict)

dict['one'] = 11
print(dict)

del(list[0])
print(list)

del(dict['one'])
print(dict)

print(list.pop(3))
print(list)

print(dict.pop('three'))
print(dict)

# 파이썬 dictionary (해쉬구조)
d = {"leo":30, "kiki":62, "eden":5}
x = d["leo"]
print(x)
d["leo"] = 58
# https://wikidocs.net/16
print(d, d.keys(), d.values())
print(d.items())
print(d.get('kiki', 'who?'))
print(d.get('jiny', 'who?'))
print('jiny' in d)


participant = ['A', 'B', 'C', 'A', 'D']
completion = ['A', 'B', 'A', 'D']

# 단 한 명의 선수를 제외하고는 모든 선수가 마라톤을 완주하였습니다
def solution(participant, completion):
    d = {}
    for x in participant:
        # x key값이 없으면 0
        d[x] = d.get(x, 0) + 1
    for x in completion:
        d[x] -= 1
    
    # d 딕셔너리에 있는 모든 원소 나열, 조건문으로 check
    # 사전 크기에 비례하는 연산
    dnf = [ k for k,v in d.items() if v > 0]
    return dnf[0]

print(solution(participant, completion))


