
'''
- 그래프 graphs
정점(vertex, node)과 간선(edge, link)
유향(directed) 그래프, 무향(undirected) 그래프
- 스텍(stack)
- 큐 (queue)

* 깊이 우선 탐색 (DFS : Depth-First Search)
한 정점에서 인접한 모든 정점을 방문하되,
인접 정점을 기준으로 깊이 우선 탐색 끝낸 후 다음 정점으로 진행
-> 스택을 이용해서 어느 정점에서 DFS하고 있는지 기억하고 되돌아감

* 너비 우선 탐색 (BFS : Breadth-First Search)
한 정점에서 인접한 모든 정점을 방문,
방문한 각 인접 정점을 기준으로 너비 우선 탐색
-> 큐를 이용해서 어느 정점에서 BFS를 해야하는지 기록하고 진행함
'''

'''
주어진 항공권을 모두 이용해서 여행경로
만약 가능한 경로가 2개 이상일 땐 알파벳 순서가 앞서는 경로로

* 깊이우선탐색(DFS)응용
한 붓 그리기!: 가능함이 문제에서 보장되어 있음
시작은 항산 ICN
모든 간선을 거쳐야한다

재귀적인 성질을 가진 한 붓 그리기 문제
그래프 깊이 우선 탐색 응용
'''

'''
그래프의 표현

사전을 이용해서 각 공항에서 출발하는 집합 표현
{start(key):destination(value)}

! 알파벳 순서가 중요
항공권의 리스트 표현
리스트를 앞에서부터 제거하는 것보다 뒤에서 제거하는게 더 효율적
알파벳 역순으로 정렬 : 뒤에서부터 제거하기 위함
ICN -> [SFO, ATL]
ATL -> [SFO, ICN]
SFO -> [ATL]
'''


def solution(tickets):
    # 딕셔너리
    # key : 출발공항
    # value : 도착공항. 리스트형태
    # { "ICN" : ["JFK", "IAD"] , "IAD" : ["HND", "JFK"] }
    routes = {} 
    
    for t in tickets:
        # key : 출발공항, value : 도착공항 리스트
        # routes dictionary에 value를 넣을 때
        # 기존값 + 새로 탐색해서 넣을 값
        # 만약 기존 dictionary에 해당 key값으로 get()할 수 있는 value가 없을 때
        # default값인 [] 빈 리스트 생성 후 + [t[1]]
        # t[0] key에 value를 넣을 때 기존 값 + t[1]리스트
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
        
#    print(routes)
#    print(routes["ICN"])
    
#    for k, i in routes.items():
#        i.sort(reverse=True)
    
    for r in routes: #key값 빼기
        # 해당 key값을 가진 value(리스트type)를 알파벳 역순으로 sort
        # 알파벳순으로 접근해야하는데
        # 앞순서 공항부터 pop해야함
        # 먼저 pop할 공항이 리스트의 맨 끝에 있는 것이 효율적이기 때문에
        # 알파벳 역순으로 sort
        routes[r].sort(reverse=True)
#    print(routes)
    
    # 무조건 start 지점이기 때문
    stack = ["ICN"]
    path = []
    
    while len(stack) > 0:
        # stack의 맨 위에있는 원소
        top = stack[-1]
        
        # 해당 공항이 key 값으로 없거나
        # 해당 key값을 value 리스트에 더이상 값이 없을 때
        if top not in routes or len(routes[top]) == 0:
            # stack의 제일 상단에 있는 공항을 방문 경로에 추가
            # 해당 공항에 대한 탐색이 끝났기 때문에 stack에서 제
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())
         #   stack.append(routes[top][-1])
         #   routes[top] = routes[top][:-1]
    
    # 리스트 [start index : last index : 간격]
    # [::-1] : 전체리스트를 -1간격으로 즉, 역순으로 탐색
  #  print(path)
    return path[::-1]


# 항공루트 정렬 : 방향성이 있는 그래프
# 시작점을 key로 갖는 dictionary
# 도착점 value는 리스트형태
# 한붓그리기. 방문지점을 stack에 쌓음. 
# 알파벳순서대로 앞순서를 먼저 방문.
# stack의 top 즉, 가장 최근에 방문한 지점을 기준으로
# 다음에 방문할 지점이 있는지 탐색. 탐색한 지점 티켓 remove
# 해당 지점에서 방문할 수 있는 지점탐색이 완료되면 탐색완료
# stack에서 pop하여 patch에 추가
# DFS사용.

def solution(tickets):
    # 항공권 정보를 dictionary에 정리
    routes = {}
    
    for t in tickets:
         routes[t[0]] = routes.get(t[0], []) + [t[1]]
    
    for k in routes:
        routes[k].sort(reverse=True)
    
    s = ["ICN"]
    path = []
    
    while len(s) > 0:
       # if top = s.pop() is null:
       #     break
        top = s[-1]
        # top : key
        if top not in routes or len(routes[top]) == 0:
            path.append(s.pop())
        else:
            s.append(routes[top].pop())
    
    return path[::-1]


tickets = [ ["ICN", "ATL"],
            ["ICN", "SFO"],
            ["SFO", "ATL"],
            ["ATL", "ICN"],
            ["ATL", "SFO"] ]

print(solution(tickets))

'''
r = {}
for i in tickets:
    print(i[0], i[1])
  #  print(r[i[0]])
    r[i[0]] = [i[1]]
    r[i[0]] = r.get(i[0]) + [i[1]]
    print(r[i[0]])
    #    r[] = r.get()
'''







