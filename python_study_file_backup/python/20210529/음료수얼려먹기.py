
# 한 번에 만들 수 있는 아이스크림 개수는?

# 얼음을 얼릴 수 있는 공간이 상, 하, 좌, 우로 연결되어 있다.

n, m = map(int, input().split())

# 2차원 리스트 맵정보 입력받기
graph = []
for i in range(n):
    graph.append( list( map(int, input()) ) )


#for i in graph:
#    print(i)

# dfs로 특정한 노드를 방문한 뒤에 연결된 모든 노드들도 방문
def dfs(x, y):
    # 주어진 범위를 벗어나는 경우에는 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False

    if graph[x][y] == 0 :

        # 해당 노드 방문처리
        graph[x][y] = 1

        # 재귀적 호출
        dfs(x-1, y)
        dfs(x+1, y)
        dfs(x, y-1)
        dfs(x, y+1)
        return True
    return False

result = 0
for i in range(n) :
    for j in range(m) :
        if dfs(i, j) == True :
            result += 1


print(result)
