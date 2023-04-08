
# 최단 경로 모두 출력보단
# 최단 거리 출력 문제가 많음
# 최단 거리 알고리즘  : 다익스트라 최단 경로 알고리즘, 플로이드 워셜, 벨만 포드 알고리즘
# 다익스트라 최단 경로 알고리즘, 플로이드 워셜 공부!

# Dijkstra 다익스트라 최단 경로 알고리즘 -> 그리디 알고리즘으로 분류됨
# 여러개 노드가 있을 때 특정 노드에서 출발하여 다른 노드로 가는 각각의 최단경로를 구해주는 알고리즘
# '음의 간선'이 없을 때 정상동작함
# 가장 비용이 적은 노드를 선택해서 임의의 과정 반족

# 1. 출발 노드를 설정
# 2. 최단 거리 테이블을 초기화
# 3. 방문하지 않은 노드 중 최단 거리가 가장 짧은 노드 선택
# 4. 해당 노드를 거쳐 다른 노드로 가는 비용을 계산하여 최단거리 테이블 갱신
# 5. 3, 4번 반복
# 방문하지 않은 노드 중 현재 최단 거리가 가장 짧은 노드를 확인하여 4번을 수행 : 그리디 알고리즘과 유사

# 다익스트라 알고리즘 구현 방법
# 방법1. 구현하기 쉽지만 느리게 동작하는 코드
# 방법2. 구현하기 까다롭지만 빠르게 동작하는 코드 -> 이걸루

# 파이썬에서 기본으로 1e9(10억)를 실수 자료형으로 처리함
# int(1e9) 모든 간선이 정수형으로 표현되는 문제에서 무한 값 표현시 사용

# 기본 설정으로 가져가자
import sys
input = sys.stdin.readline
INF = int(1e9)

# 노드 개수, 간선 개수
n, m = map(int, input().split())

# 시작 노드
start = int(input())

# n개 노드를 가진 graph
graph = [ [] for i in range(n+1) ]

# 방문 정보 Check
visited = [False]*(n+1)

# 최단 거리 (무한으로 초기화)
distance = [INF]*(n+1)

# 간선 정보
for _ in range(m) :
    a, b, c = map(int, input().split())
    graph[a].append( (b, c) )

#for i in range(len(graph)) :
#    print(graph[i])

# 방문하지 않은 노드 중 가장 거리가 짧은 노드 번호 반환
def get_smallest_node():
    min_value = INF
    index = 0 # 없는 노드 번호인 0으로 초기화
    for i in range(1, n+1) :
        if distance[i] < min_value and visited[i] == False :
            min_value = distance[i]
            index = i
    return index

#if get_smallest_mode() == 0 :
#    break

# 시간 복잡도가 O(V^2) 인 방법 (V 노드 개수) - 선형적 탐색
def dijkstra(start) :

    # 시작 노드에 대해 초기화
    distance[start] = 0
    visited[start] = True

    for data in graph[start] :
        distance[ data[0] ] = data[1]

    # 시작 노드를 제외한 전체 n-1개 노드에 대해 반복 (횟수)
    for i in range(n-1) :
        now = get_smallest_node()

        # 어차피 노드 개수만큰 탐색하기 때문에 해당 조건문 필요 없당
        #if now == 0 :
        #    break

        visited[now] = True

        for j in graph[now] :
            distance[j[0]] = min(distance[j[0]], j[1]+distance[now])

        
dijkstra(start)

for i in range(1, n+1) :
    if distance[i] == INF :
        print('Infinity')
    else :
        print(distance[i])




