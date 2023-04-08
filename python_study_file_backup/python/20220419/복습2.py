
# dic 이용

def solution2(tickets):
    
    dic = {}
    
    for t in tickets:
        dic[t[0]] = dic.get(t[0], []) + [t[1]]
        
    
    
    for v in dic.values():
        v.sort(reverse=True)
        
    stack = ['ICN']
    path = []
     
    while stack:
        top = stack[-1]
        print('1:',dic, '\n',stack, path)
        
        # 해당 원소가 key값으로 없거나, value가 다 비어있으면 탐색 끝
        if top not in dic or len(dic[top]) == 0:
            path.append(stack.pop())
        else:
            stack.append(dic[top].pop())
        
        print('2:',dic, '\n',stack, path,'\n')
    
    return path[::-1]
    


def solution(tickets):
    
    dic = {}
    
    for t in tickets:
        dic[t[0]] = dic.get(t[0], []) + [t[1]]
        
    print(dic)
    
    # 알파벳순서
    
    for k in dic.keys():
        print(k)
    for v in dic.values():
        print(v)
        
    for k, v in dic.items():
        print(k, v)
    
    print(dic)
    
    for v in dic.values():
        v.sort()
    
    print(dic)
    
    # 그런데 맨 끝 원소를 pop하는 것이 시간적으로 이득
    # 때문에 결과값을 알파벳 순서로 하기 위해서 역순으로 sort
    
    for v in dic.values():
        v.sort(reverse=True)
    
    print(dic)
    
    for k in dic:
        dic[k].sort(reverse=True)
        
    print(dic)
    
    stack = ['ICN']
    path = []
    
    # 문제를 잘못 이해
    # 한붓그리기 아님!!!!!!
    # 왔다갔다 하더라도 이동경로 확인!!!!
    # 알파벳 순서로 가장 앞에있는 공항 먼저 탐색
    # 그럼 해당 공항에서 갈 수 있는 공항 또 탐색
    # key로 없거나 배열 빌 때까지
    # 그렇게 모든 이동할 수 있는 경로 모두 탐색하면 끝
    
    # 이건 시간복잡도가 에바인듯
    # del dic O(n)임
    while dic:
        top = stack[-1]
        if top in dic:
            stack.append(dic[top].pop())
        
            if dic[top] == []:
                del dic[top]
        
    print(stack)
    #return stack[::-1]    
    
    
        
    
    # value가 정렬된 dic 준비끝
    
    # 깊이우선탐색
    # stack 사용
    
 #   stack = ['ICN']
 #   visited = ['ICN']
    
    
    # stack의 맨 끝 원소가 갈 수 있는 경로 탐색
    # 1. 해당 원소를 key 값으로 갖는 value 확인
    # 2. 그 value를 key 값으로 갖는 value 확인..
    # 확인한 원소는 stack에 쌓는다
    # dfs는 dic, key
    # 해당 원소가 key값으로 없거나, value가 다 비어있으면 탐색 끝
    # 그러면 다시 그 원소의 다른 value 탐색
    # 즉 탐색하는 key의 value가 빈 리스트가 될 때까지
    
 #   dfs(stack, dic)
    
 #   k1 = stack[-1]
    
 #   if dic[k1] == []:
 #       break
    
 #   v1 = dic[k1][-1]
    
 #   if v1 not in stack
    
    
 #   while stack:
        
 #       s1 = stack.pop()
 #       result += [s1]
 #       visited += [s1]
        
 #       print('1:',stack)
        
 #       for v in dic[s1]:
 #           if v not in visited:
                #stack += [v]
        
 #       print('2:',stack)
    
 #   print(result)
    


t1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
t2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

#print(solution(t1))
print(solution2(t2))


















