
# DFS : Depth-First Search

# 인접행렬(Adjacency Matrix) : 2차원 배열에 각 노드가 연결된 형태 기록
# 연결되지 않는 노드는 무한(INF)
#   0 1 2
# 0 0 7 5 
# 1 7 0 F
# 2 5 F 0
INF = 999999 #무한의 미용 선언
graph1 = [
    [0, 7, 5],
    [7, 0, INF],
    [5, INF, 0]
]

print(graph1)


# 인접리스트(Adjacency List) : 모든 노드에 연결된 노드에 대한 정보를 차례대로 연결하여 저장
# 행이 3개인 2차원 리스트로 인접 리스트 표현
graph = [ [] for _ in range(3) ]

# 노드 0에 연결된 노드 정보
graph[0].append((1, 7))
graph[0].append((2, 5))

# 노드 1에 연결된 노드 정보
graph[1].append((0, 7))

# 노드 2에 연결된 노드 정보
graph[2].append((0, 5))

print(graph)


# 두 방식의 차이점
# 메모리측면: 저장되는 노드 개수가 많을 수록 메모리 낭비됨
# - 인접리스트 : 연결 정보만 저장하기 때문에 메모리 효율적으로 사용.
#                그러나 두 노드가 연결되어 있는지 정보를 얻는데 속도가 느림
#                연결된 데이터를 하나씩 확인해야하기 때문

# Ex. 노드 0과 1이 연결되어 있는지 확인.
# 인접 행렬 : graph[0][1]
# 인접 리스트 : 노트 0에 대한 인접 리스트를 앞에서부터 차례대로 확인해야함


# DFS(깊이 우선 탐색) : 최대한 멀리 있는 노드부터 탐색. 스택 자료구조 이용.
# 1. 탐색 시작 노드를 스택에 삽입 후 방문 처리
# 2. 스택의 최상단 노드에 방문하지 않은 인접노드가 있을 경우,
#    인접 노드를 스택에 넣고 방문처리를 한다.
#    방문하지 않은 인접 노드가 없으면 스태 최상단에서 노드를 꺼낸다.
# 3. 2번 과정을 더 이상 수행할 수 없을 때까지 반복.
# -> 방문 처리 : 스택에 한 번 삽입되어 처리된 노드가
#                다시 삽입되지 않도록 체크하는 것을 의미

# p.137
# DFS : 깊이 우선 탐색 - 데이터 개수가 N개인 경우 O(N) 시간 소요됨
print('\n\n<<DFS>>')
def dfs ( graph, v, visited ) :
    # 현재 노드 방문 처리
    visited[v] = True
    print(v)

    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v] :
        if not visited[i] :
            print('not visited node', i)
            dfs(graph, i, visited)
            print('visit complete node', i)
        else :
            print('before visited node', i)

graph_1 = [
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

# 1 ~ 8번 노드 방문 정보를 저장하기 위한 리스트 초기화
visited_1 = [False]*9

dfs(graph_1, 1, visited_1)
    

# p.143
# BFS(너비 우선 탐색) : 가까운 노드부터 탐색. 큐 자료구조 이용.
# 탐색 시작 노드를 큐에 삽입 후 방문처리
# 큐에서 노드를 꺼내, 해당 노드의 인접 노드 중 방문하지 않은 노드부터 큐에 삽입
# 2번 과정을 더이상 수행할 수 없을 때까지 반복
from collections import deque
#qu = deque([1])
#print(qu)

print('\n\n<<BSF>>')
def bsf (graph, start, visited) :
    # 큐(queue) 구현을 위해 deque 라이브러리 이용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True

    # 큐가 빌 때까지 반복
    while queue :
        # 큐에서 하나의 원소를 뽑아 출력
        v = queue.popleft()
        print(v)

        for i in graph[v] :
            if not visited[i] :
                print('not visited node', i)
                queue.append(i)
                visited[i] = True
            else  :
                print('before visited node', i)

graph_2 = [
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

visited_2 = [False]*9

bsf(graph_2, 1, visited_2)

