
'''
깊이/너비 우선 탐색 (DFS/BFS)

그래프 graphs
정점(vertex, node) 과 간선(edge, link)
유향(directed)그래프와 무향(undirected그래프
스택(stack)
큐(queue)

깊이 우선 탐색(DFS)
한 정점에서 인접한 모든 (방문하지 않은) 정점을 방문하되
각 인접 정점을 기준으로 깊이 우선 탐색을 끝낸 후 다음 정점으로 진행
스택을 이용해서 어느 정점에서 DFS를 하고 있는지 기억하고 되돌아감

너비 우선 탐색(BFS)
한 정점에서 인접한 모든 (방문하지 않은) 정점을 방문
방문한 각 인접 정점을 기준으로(방문 순서에 따라)
또 다시 너비 우선 탐색을 함

이번 문제는 DFS이용
한 붓 그리기가 가능함이 문제에 보장되어 있음
첫 정점은 ICN
모든 간선을 거쳐야함
간선이 여러개인 경우 알파벳 순서대로

stack을 활용!
재귀적인 성질을 활용

사전을 이용해서 각 공항에서 출발하는 항공권의 리스트 표현
리스트에서 원소 제거할 때 맨 뒤에서 제거하는게 효율이 더 좋으므로
알파벳 역순으로 정렬

알고리즘 복잡도
모든 공항이 stack에 한 번 씩 들어가고, 한 번씩 꺼내진다
리스트 길이에 비례한다
dic을 사용하지 않았으면 O(N^2) 복잡도를 가짐

dic을 sort하는 부분을 봐야함
전체 알고리즘 복잡도는 O(NlogN)에 비례함

반복문의 반복 횟수는 표 길이 만큼
각 단계는 상수시간이므로 linear함

즉 정렬 부분에 시간 복잡도 지

'''
def solution(tickets):
    routes = {}
    for a,b in tickets:
        routes[a] = routes.get(a, []) + [b]
        
    for r in routes:
        routes[r].sort(reverse=True)
        
    stack = ["ICN"]
    path = []
    while stack:
        top = stack[-1]
        # key값이 없고 원소가 없을 때
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top][-1])
            routes[top] = routes[top][:-1]
            
    # 역순으로 출력
    return path[:-1]



















