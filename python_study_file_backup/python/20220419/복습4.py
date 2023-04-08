
# 네트워크

# node는 0 ~ n-1
# computers로 연결 확인할 수 있음

# 방향성 없는 그래프 개수
# 넓이 우선 탐색 or 깊이 우선 탐색

n = 3 
# 방문노드 check
visited = [ 0 for _ in range(n)  ]

# 연결 정보
# computers[i][j] = 1 이면 연결

# 연결 정리? 정리 필요한가?
# dic으로 정리해볼까

dic = {}
computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
computers = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

for i in range(n):
    for j in range(n):
        if i != j and computers[i][j] == 1:
            dic[i] = dic.get(i, []) + [j]
            
# 방향성이 없기 때문에 dic 필요 X
# {0: [1], 1: [0]} 반만 check 될듯
#print(dic)


dic2 = {}
for i in range(n):
    for j in range(i+1, n):
        if computers[i][j] == 1:
            dic2[i] = dic2.get(i, []) + [j]


# {0: [1]}
#print(dic2)


for i in range(n):
    for j in range(i+1, n):
        if computers[i][j] == 1:
            visited[j] = 1


from collections import deque

# 방문 노드의 모든 것 탐색
def bfs(node, visited, computers, n):
    
    q = deque()
    q.append(0)
    
    while q:
        node = q.popleft()
        visited[node] = 1
        
        for i in range(n):
            if visited[i] != 1 and node != i and computers[node][i] == 1:
                q.append(i)
                

def bfs_1(node, visited, computers, n):
    
    if visited[node] == 1:
        return
    
    visited[node] = 1
    for i, v in enumerate(computers[node]):
        if v == 1 and visited[i] != 1:
            bfs_1(i, visited, computers, n)
    else:
        return
    

def solution(n, computers):
    
    cnt = 0
    
    visited = [ 0 for _ in range(n) ]
    print(visited)
    for i in range(n):
        if visited[i] != 1:
            bfs_1(i, visited, computers, n)
            cnt += 1
    print(visited)
    
    return cnt

n1 = 3
computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

n2 = 3
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]


print(solution(n1, computers1))
print(solution(n2, computers2))    
    

'''
q = deque()
q.popleft()
q.append()
'''




