
# DFS
def dfs ( graph, v, visited ) :
    visited[v] = True
    print(v, end=' ')

    for i in graph[v] :
        if not visited[i] :
            dfs( graph, i, visited )

graph = [
    [],
    [2, 3, 8],
    [1, 7],
    [1, 4, 5],
    [3, 5],
    [3, 4],
    [7],
    [2, 6, 8],
    [1, 7]
]

visited = [False]*9


dfs( graph, 1, visited )
print('\n')



# BFS
from collections import deque

def bfs ( graph, start, visited ) :
    queue = deque()

    queue.append(start)
    visited[start] = True

    while (queue) :
        node = queue.popleft()
        print(node, end=' ')
        
        for i in graph[node] :
            if not visited[i] :
                queue.append(i)
                visited[i] = True
    

visited = [False]*9

bfs(graph, 1, visited)
print('\n')




