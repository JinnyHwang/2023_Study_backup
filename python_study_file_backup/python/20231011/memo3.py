

n, m = tuple(map(int, input().split()))

graph = [[] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]

for _ in range(m):
    x,y = map(int, input().split())
    graph[x].append(y)
    graph[y].append(x)


# 도달할 수 있는 정점의 수는?
def dfs(vertex):
    global cnt_vtx
    for v in graph[vertex]:
        if not visited[v]:
            cnt_vtx += 1
            visited[v] = 1
            dfs(v)

start_vertex = 1
visited[start_vertex] = 1
cnt_vtx = 0
dfs(start_vertex)
print(cnt_vtx)




