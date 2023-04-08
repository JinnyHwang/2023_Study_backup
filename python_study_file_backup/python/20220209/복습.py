
'''
사전을 이용하여 각 공항에서 출발하는 항공원의 집합 표현
그런데 알파벳 순서 라는 조건이 들어가기 때문에,
리스트로 표현
그리고 리스트의 원소를 제거할 때
뒷번호 인덱스부터 삭제하는게 더 효율적이기 때문에
사용하는 리스트는 알파벳 역순으로 표현
'''

def solution_DFS(tickets):
    routes = {}
    for t in tickets:
        # 리스트 병합 사용
        routes[t[0]] = routes.get(t[0], []) + [t[1]]
        
    for r in routes:
        # 알파벳 역순으로 각 key의 value 정렬
        routes[r].sort(reverse=True)
    
    # 맨 처음 공항은 무조건 ICN
    stack = ["ICN"]
    path = [] # 경로 저장을 위한 list
    
    while len(stack) > 0:
        top = stack[-1]
        # top이 key값으로 등록되어 있지 않거나,
        # key값으로 사용하여도 가지고 있는 value가 없으면 pop
        if top not in routes or len(routes[top]) == 0:
            path.append(stack.pop())
        # top이 가지고 있는 value 중 가장 맨 끝 원소를 stack에 추가
        else:
            stack.append(routes[top][-1])
            # 맨 끝 value 삭제
            routes[top] = routes[top][:-1]
     
    # path에 쌓은 원소들 역순으로 return
    return path[::-1]
















