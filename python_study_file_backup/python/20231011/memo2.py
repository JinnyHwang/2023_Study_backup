

# 인접리스트
# 시작점
VERTICES_NUM = 7 # 정점
EDGES_NUM = 6 # 간선

graph = [[] for _ in range(VERTICES_NUM+1)]
start_points = [1,1,1,2,4,6]
end_points = [2,3,4,5,6,7]

for s,e in zip(start_points, end_points):
    graph[s].append(e)
    graph[e].append(s)

visited = [0 for _ in range(VERTICES_NUM+1)]
dfs_graph = []

def dfs(vertex):
    for curr_v in graph[vertex]:
        if not visited[curr_v]:
            dfs_graph.append(curr_v)
            visited[curr_v] = 1
            dfs(curr_v)
            
root_vertex = 1
dfs_graph.append(root_vertex)
visited[root_vertex] = 1
dfs(root_vertex)

print(dfs_graph)

