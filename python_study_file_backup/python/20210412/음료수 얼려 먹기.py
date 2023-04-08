
# 배열 내 그래프가 몇개 존재하는가

n, m = map(int, input().split())

graph = []
for i in range(n) :
    graph.append(list( map( int, input() ) ) )

# DFS로 특정 노드 방문한 뒤 연결된 모든 노드도 방문
def dfs_1(x, y) :
    #주어진 범위를 벗어나는 경우 즉시 종료
    if x <= -1 or x >= n or y <= -1 or y >= m :
        return False

    if graph[x][y] == 0 :
        #해당 노드 방문 처리
        graph[x][y] = 1
        dfs_1(x-1, y)
        dfs_1(x+1, y)
        dfs_1(x, y-1)
        dfs_1(x, y+1)

        print(x, y,' 탐색 \n', graph)
        return True

    return False

result = 0

for i in range(n) :
    for j in range(m) :
        # 현재 위치에서 dfs 수행
        if dfs_1(i, j) == True :
            result += 1
            print(result,'번 graph 탐색 완료')

print(result)

# 4 5
# 00110
# 00011
# 11111
# 00000


# 15 14
# 00000111100000
# 11111101111110
# 11011101101110
# 11011101100000
# 11011111111111
# 11011111111100
# 11000000011111
# 01111111111111
# 00000000011111
# 01111111111000
# 00011111111000
# 00000001111000
# 11111111110011
# 11100011111111
# 11100011111111

