
# 각 노드의 방향 파악
com = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]
com2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

dic = {}

for i, c in enumerate(com):
    for ci, connect in enumerate(c):
        if connect == 1 and i != ci:
            dic[i] = dic.get(i, []) + [ci]
            
dic2 = {}

for i, c in enumerate(com2):
    for ci, connect in enumerate(c):
        if connect == 1 and i != ci:
            dic2[i] = dic2.get(i, []) + [ci]


print(dic)
print(dic2)


from collections import deque

q = deque()

def bfs(dic, n):
    print(n, dic)
    
    if dic[n] == []:
        return print(1)
    
    c = dic[n].pop()
    bfs(dic, c)

bfs(dic, 0)

bfs(dic2, 0)

def bfs_b(visited, computers, i, n):
    q = deque()
    q.append(i)
    
    while q:
        node = q.popleft()
        visited[node] = True
        for i in range(n):
            if computers[node][i] == 1 and visited[i] == Flase:
                q.append(i)
    

def bfs_a(visited, computers, i, n):
    
    if visited[i] == True:
        return
    
    visited[i] = True
    for ci, c in enumerate(computers[i]):
        if c == 1 and visited[ci] == False:
            bfs_a(visited, computers, ci, n)
    
    return
    

# 문제 의도 명확하게 알기
# 해당 문제에서 중요한 것 : 방문한 적이 있는가?
# 모든 node를 방문해봐야함
def solution(n, computers):
    answer = 0
    visited = [False for _ in range(n)]
    
    for i in range(n):
        if visited[i] == False:
            bfs_a(visited, computers, i, n)
            answer += 1
    
    return answer

print('A1 : ', solution(3, com))
print('A1 : ', solution(3, com2))





















