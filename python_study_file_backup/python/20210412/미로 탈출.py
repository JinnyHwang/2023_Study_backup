
from collections import deque

n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append( list( map(int, input()) ) )

# 이동할 좌표 상, 하, 좌, 우
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

def bsf(x, y) :
    queue = deque()
    queue.append((x, y))

    while queue :
        a, b = queue.popleft()

        # 현재 위치에서 상, 하, 좌, 우 확인
        for i in range(4) :
            nx = a + dx[i]
            ny = b + dy[i]

            if nx <= -1 or nx >= n or ny <= -1 or ny >= m :
                continue

            if graph[nx][ny] == 0 :
                continue

            if graph[nx][ny] == 1 :
                






