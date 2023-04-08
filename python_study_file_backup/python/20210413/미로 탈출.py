
# p.154

# N*M graph에 탈출구는 (N, M)
n, m = map( int, input().split() )

graph = []

for i in range(n) :
    graph.append( list( map( int, input() ) ) )


# 노드 정보는 x, y
#     상 하 좌 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

#visited = [[False]*m for _ in range(n) ]         

from collections import deque

def bfs ( x, y ) :

    queue = deque()
    queue.append((x, y))

    while queue :
        a, b = queue.popleft()
        
        for i in range(4) :
            nx = a + dx[i]
            ny = b + dy[i]

            if nx < 0 or nx > n-1 or ny < 0 or ny > m-1 :
                continue

            if graph[nx][ny] == 0 :
                continue

            if graph[nx][ny] == 1 :
                graph[nx][ny] = graph[a][b] + 1
                queue.append((nx, ny))

                # bfs를 이해하기 위함
                for i in graph :
                    print(i)
                print('\n')
                
    return graph[n-1][m-1]

print(bfs(0, 0))


 




