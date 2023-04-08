
'''
작은 사람부터 작은 옷부터 입히면 가장 효율적
정렬 후 티셔츠를 하나씩 살피면서
people보다 크면 입히고 아니면 넘기기

내가 생각했던 풀이와 완전 다르고
내 풀이는 숫자를 key값으로, 사람수/개수를 value로 해서 티 나눠줌
해설이 훨씬 심플하게 접근..!
'''

def solution(people, tshirts):
    people.sort()
    tshirts.sort()
    
    p, t, ans = 0, 0, 0
    
    while p < len(people) and t < len(tshirts):
        if tshirts[t] >= people[p]: # 지금 사람이 티셔츠 입을 수 있는가?
            ans += 1
            p += 1 # 다음 사람 탐색
            
        t += 1 # 다음 티셔츠 계속 탐색
        
    return ans
        








