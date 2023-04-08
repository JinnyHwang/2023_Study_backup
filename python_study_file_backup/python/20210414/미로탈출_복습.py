
n, m = map( int, input().split() )

graph = []

for i in range(n) :
    graph.append( list( map(int, input()) ) )
    

# BFS로 최단거리 찾기

# 0,0에서 n-1, m-1까지

# 시작 좌표 a, b

from collections import deque

# 상 하 좌 우
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(a, b) :
        
    queue = deque()
    queue.append( (a, b) )

    while queue :
        x, y = queue.popleft()

        for i in range(4) :
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or ny < 0 or nx > n-1 or ny > m-1 :
                continue
            
            if graph[nx][ny] == 0 :
                continue

            if graph[nx][ny] == 1 :
                queue.append( (nx, ny) )
                graph[nx][ny] = graph[x][y] + 1

    return graph[n-1][m-1]

        
print(bfs(0, 0))










