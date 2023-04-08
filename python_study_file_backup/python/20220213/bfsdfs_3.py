
# node를 탐색하면서 목적지까지 도달할 수 있는가?
# words에 포함된 단어들이 node
# 간선은 현재 단어에서 한 글자만 다른 단어
# 모든 node를 탐색했지만 목적지 node에 도달하지 못한 경우 return 0
# 목적지 node가 없는 경우 return 0

# bfs 사용
# 앞으로 탐색할 수 있는 node(현재 단어에서 한 글자만 다른 단어) 모두 탐색
# [현재 단어, 탐색 경로]
# 방문하지 않은 node 중에는 현재 단어에서 한 글자만 다른 단어가 존재하는가?

from collections import deque

def solution(begin, target, words):
    
    # 단어 한 글자만 다른가 파악하는 method
    def check_word(word1, word2):
        count = 0
        for i, w1 in enumerate(word1):
            if w1 != word2[i]:
                count += 1
            if count == 1:
                return True
            else:
                return False
    
    # target 단어가 리스트 안에 없으면 0
    if target not in words:
        return 0
    
    visited = [ False for _ in range(len(words)) ]
    
    q = deque()
    q.append([begin, 0])
    
    while q:
        # 탐색해야하는 단어
        qw = q.popleft()
        
        if qw[0] == target:
            return qw[1]
        
        for i, w in enumerate(words):
            # 방문한 적 없는 단어인가?
            if visited[i] == False:
                # 한 글자만 다른가?
                if check_word(qw[0], w):
                    q.append([w, qw[1]+1])
                    visited[i] = True
                    
    return 0

















