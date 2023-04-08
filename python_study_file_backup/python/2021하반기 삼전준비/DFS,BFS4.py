# 현재 탐색하는 node에서 방문할 node를 stack으로 쌓음
# 알파벳순서가 앞순서인 항공을 먼저 가야함
# stack에 쌓을 때 알파벳 앞순서인 node를 나중에 쌓기
# 기존 ticket list 정렬 필요
# 경로를 pop 다시 
def solution(tickets):
    
    #tickets를 정렬
    #sort_tickets = sorted(tickets, key=lambda t : t[1])
    #print("tickets\n{}\nsort_tickets\n{}".format(tickets, sort_tickets))
    
    # dictionary로 정리
    dic_tickets = {}
    
    for t in tickets:
        dic_tickets[t[0]] = dic_tickets.get(t[0], []) + [t[1]]
    
    for dt in dic_tickets:
        # pop() 했을 때 알파벳 앞순서 공항이 오기 위함
        dic_tickets[dt].sort(reverse=True)
        # 정방향 sort시 pop(0)해야함
        #dic_tickets[dt].sort()
    
    print("tickets\n{}\ndic_tickets\n{}".format(tickets, dic_tickets))
    
    # value가 없어지면 key값 자체가 사라짐
    #dic_tickets.pop('ICN')
    #print('1pop:',dic_tickets)
    
    # stack에서 나온 공항 기록
    path = []
    
    # 방문할 공항 stack으로 쌓기
    visit = []
    
    # 맨처음 무조건 ICN
    visit.append("ICN")
    
    # 갈 수 있는 모든 path가 없을 때 pop
    while visit :
        print("visit:",visit)
        print("dic_tickets:",dic_tickets)
        # 탐색할 공항
        v = visit[-1]
        
        try:
            nv = dic_tickets[v].pop()
            visit.append(nv)
        except:
            path.append(visit.pop())
            
        
    
    # path 역순 return
    return path[::-1]



t1 = [["ICN", "JFK"], ["HND", "IAD"], ["JFK", "HND"]]
t2 = [["ICN", "SFO"], ["ICN", "ATL"], ["SFO", "ATL"], ["ATL", "ICN"], ["ATL","SFO"]]

#print(solution(t1))
print(solution(t2))
