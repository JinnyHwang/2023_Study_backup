
# dfs
# 스택을 이용해서 어느 정점에서 dfs를 하고 있는지 기억하고 되돌아감

# bfs
# 큐를 이용해서 어느 정점에서 bfs를 해야하는지 기억하고 되돌아감

# 사전을 이용해서 각 공항에서 출발하는 항공원 집합 표현
"""
ICN:{ATL, SFO}
ATL:{ICN, SFO}
SFO:{ATL}
"""

def solution_1(tickets):
    routes = {}
    for t in tickets:
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
        
    #print(routes)
    
    # r은 key값
    # routes[r] r의 value
    # 알파벳 역순으로 정렬 (pop할 때 맨 뒤에서부터 꺼내오기 위함)
    for r in routes:
        routes[r].sort(reverse=True)
    
    # 출발 node
    stack = ['ICN']
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(routes[top].pop())
            #stack.append(routes[top][-1])
            #routes[top] = routes[top][:-1]
        
        # 역순으로 출
        return path[::-1]


t1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
t2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

def solution(tickets):
    
    dic = {}
    for t in tickets:
        dic[t[0]] = dic.get(t[0], []) + [t[1]]
    #print(dic)
        
    # value를 알파벳 역순으로 sort
    for d in dic:
        dic[d].sort(reverse = True)
        
    stack = ['ICN']
    path = []
    while stack:
        top = stack[-1]
        if top not in dic or len(dic[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(dic[top].pop())
    
    return path[::-1]
    

print(solution(t1))
print(solution(t2))











