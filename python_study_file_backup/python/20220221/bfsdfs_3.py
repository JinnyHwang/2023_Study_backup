
b1 = "hit"
t1 = "cog"
w1 = ["hot", "dot", "dog", "lot", "log", "cog"]

b2 = "hit"
t2 = "cog"
w2 = ["hot", "dot", "dog", "lot", "log"]


# 단어 비교 func
def compare1(w1, w2):
    cnt = 0
    
    for i in range(len(w1)):
        if w1[i] != w2[i]:
            cnt += 1
    
    if cnt == 1:
        return True
    else:
        return False
    

def dfs(b, t, words):
    
    print(b, t)
    
    if b == t:
        return print('a')
    
    ws = []
    
    for w in words:
        if compare(b, w):
            #words.remove(w)
            dfs(w, t, words)
            
    if ws == []:
        return 0
    

def solution_1(begin, target, words):
    answer = 0
    
    dfs(begin, target, words)
    
    # 해당 단어와 딱 한 글자만 다른 words의 리스트 작성
    # 만들어진 words 리스트 하나하나 탐색
    
    
    return answer

#solution_1(b1, t1, w1)

from collections import deque

# 아... 각 단어마다 방향성을 가지는 그래프를 그릴 수 있구나!
def solution(begin, target, words):
    
    # 단어 비교 func
    def compare(w1, w2):
        cnt = 0
        
        for i, w in enumerate(w1):
            if w == w2[i]:
                cnt += 1
        
        if cnt == 1:
            return True
        else:
            return False
        
    # target이 리스트에 없을 때
    if target not in words:
        return 0
    
    visited = [ False for _ in range(len(words))]
    
    q = deque()
    q.append([begin, 0])
    
    while q:
        qw = q.popleft()
        
        if qw[0] == target:
            return qw[1]
        
        for i, w in enumerate(words):
            if visited[i] == False and compare(qw[0], w):
                q.append([w, qw[1]+1])
                visited[i] = True
    
    return 0
                
                    
print(solution(b1, t1, w1))
print(solution(b2, t2, w2))

















