
n, m = tuple(map(int, input().split()))

graph = [[0 for _ in range(n+1)] for _ in range(n+1)]
visited = [0 for _ in range(n+1)]
vertex_cnt = 0


for _ in range(m):
    x,y = map(int, input().split())
    graph[x][y] = 1
    graph[y][x] = 1

def dfs(vertex):
    global vertex_cnt
    
    for curr_v in range(1,n+1):
        if graph[vertex][curr_v] and not visited[vertex]:
            visited[vertex] = 1
            vertex_cnt += 1
            dfs(curr_v)
    
visited[1] = 1
dfs(1)
print(vertex_cnt)

