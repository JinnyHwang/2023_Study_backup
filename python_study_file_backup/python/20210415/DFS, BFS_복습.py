
#DFS
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


def dfs (graph, v, visited) :
    # 방문 표시
    visited[v] = True
    print(v, end=' ')

    for i in graph[v] :
        if visited[i] == False :
            dfs(graph, i, visited)
            


dfs(graph, 1, visited)
print('\n')


#BFS
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

from collections import deque

def bfs (graph, start, visited) :
    queue = deque()
    visited[start] = True
    queue.append(start)

    while queue :
        node = queue.popleft()
        print(node, end=' ')

        for i in graph[node] :
            if visited[i] == False :
                visited[i] = True
                queue.append(i)

bfs(graph, 1, visited)
print('\n')














