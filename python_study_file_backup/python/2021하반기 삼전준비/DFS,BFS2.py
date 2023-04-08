
# node와 간선정보가 주어졌을 때
# 그래프의 개수는?
# 그래프의 연결상태 확인하기 위해 BFS 사용

from collections import deque

def bfs(visited, computers, i, n):
    q = deque()
    # 아직 방문한 적 없는 node 탐색
    q.append(i)
    
    while q :
        node = q.popleft()
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and visited[i] == False :
                q.append(i)

def solution(n, computers):
    answer = 0
    visited = [ False for _ in range(n) ]
    print(visited)
    
    for i in range(n):
        if visited[i] == False:
            bfs(visited, computers, i, n)
            answer += 1
    
    return answer


def solution1(n, computers):
    
    def BFS1(node, visit):
        que = [node]
        visit[node] = 1
        
        while que:
            v = que.pop(0)
            for i in range(n):
                if computers[v][i] == 1 and visit[i] == 0:
                    visit[i] = 1
                    que.append(i)
        return visit
    
    visit = [ 0 for _ in range(n) ]
    answer = 0
    
    print(visit.index(0))
    
    print('맨처음:', visit)
    for i in range(n):
        print(i, visit)
        try:
            # 방문하지 않은 node가 존재하는 경우
            visit = BFS1(visit.index(0), visit)
            answer += 1
        except:
            break
    print('마지막:', visit)
    return answer


n1 = 3
c1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

n2 = 3
c2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

print(solution1(n1, c1))

