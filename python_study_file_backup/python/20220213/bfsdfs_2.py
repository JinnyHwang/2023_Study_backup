
# 너비 우선 탐색 queue

from collections import deque

# 한 노드에 연결되어 있는 모든 노드 탐색해서 visited로 변경
def bfs(visited, computers, i, n):
    q = deque()
    # 아직 방문한 적 없는 node (False)
    q.append(i)
    
    while q :
        node = q.popleft()
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and visited[i] == False:
                a.append(i)

# n : node 개수
def solution(n, computers):
    answer = 0
    visited = [ False for _ in range(n) ]
    
    for i in range(n):
        if visited[i] == False:
            bfs(visited, computers, i, n)
            # bfs가 한 번 끝날 때 하나의 네트워크를 찾음
            answer += 1
    return answer










