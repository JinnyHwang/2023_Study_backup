from collections import deque

def solution(begin, target, words):
    answer = 0
        
    #if words.count(target) == 0 :
    #    return answer
    
    # 이거 잊지 말자
    # target word가 아예 리스트에 없는 경우
    if target not in words:
        return answer
    
    visited = [ 0 for _ in range(len(words)) ]
    
    # words를 node라고 생각
    # 한 부분만 다른 단어 찾기
    def compare_help(aWord, bWord):
        difference = 0
        for i in range(len(aWord)):
            if aWord[i] == bWord[i]:
                difference += 1
        
        if difference == 1:
            return True
        else:
            return False
        
    # target word가 있지만, 경로를 거쳐도 target word가 만들어지지 않는 경우
    
    def bfs(curr, words, visited):
        # 현재 단어에서 변환이 가능한 단어를 queue에 추가
        # (현재 단어, 거쳐온 횟수)
        q = deque()
        q.append((curr, 0))
        
        while q:
            aw = q.popleft()
            if aw[0] == target:
                return aw[1]
            
            # 모든 words 탐색
            for i, w in enumerate(words):
                if compare_help(aw[0], w) and visited[i] == 0:
                    q.append((w, aw[1]+1))
                    visited[i] = 1
            
        return 0

    return bfs(begin, words, visited)

def solution1(begin, target, words):
    
    # 단어 한글자만 다른가 파악하는 method
    def check_word(word1, word2):
        count = 0
        for i, w1 in enumerate(word1):
            if w1 != word2[i]:
                count += 1
        if count == 1:
            return True
        else:
            return False
    # check_word end
    
    
    if target not in words:
        return 0
    
    # bfs 사용
    # 앞으로 탐색할 수 있는 node(현재 단어에서 한글자만 다른 단어) 다 탐색
    # [현재 단어, 탐색 경로]
    # 방문하지 않은 node중에 현재 단어에서 한글자만 다른 단어가 존재하는가?
    visited = [ 0 for _ in range(len(words)) ]
    
    q = deque() # 앞으로 탐색해야할 node를 queue에 저장(bfs탐색)
    q.append([begin, 0])
    
    # 더이상 node가 없을때가지
    while q:
        print(q)
        qw = q.popleft()
        
        # target word에 도달하면 방문 횟수 return 하고 end
        if qw[0] == target:
            return qw[1]
        
        for i, w in enumerate(words):
            if visited[i] == 0:
                # qw의 단어와 방문한 적 없는 현재 단어가 한글자 차이로 다른지 확인.
                # 한글자 차이로 다른 단어는 queue에 삽입
                if check_word(qw[0], w):
                    q.append([w, qw[1]+1])
                    visited[i] = 1
        print(q)
                    
    return 0



b1 = "hit"
t1 = "cog"
w1 = ["hot", "dot", "dog", "lot", "log", "cog"]

b2 = "hit"
t2 = "cog"
w2 = ["hot", "dot", "dog", "lot", "log"]

print(solution1(b1, t1, w1))
print(solution1(b2, t2, w2))

