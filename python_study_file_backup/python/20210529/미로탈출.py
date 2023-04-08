
# 탈출을 위해 움직여야하는 최소 칸의 개수는?
# 해당 좌표에 위치하기 위해서 거쳐야하는 최소한의 칸 개수를 해당 좌표에 저장.

from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append( list(map(int, input())) )


visited = [ [False]*m for i in range(n) ]


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):

    queue = deque()
    queue.append((x, y))

    while queue:
        x, y = queue.popleft()
        visited[x][y] = True

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m :
                continue

            # 갈 수 없는 길 pass
            if graph[nx][ny] == 0:
                continue

            if visited[nx][ny] == True:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
                visited[nx][ny] = True

    return graph[n-1][m-1]



for i in graph:
    print(i)

print(bfs(0, 0))

for i in visited:
    print(i)

for i in graph:
    print(i)
