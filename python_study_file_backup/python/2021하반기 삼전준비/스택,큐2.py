from collections import deque

def solution1(priorities, location):
    
    a = deque()
    
    for i, p in enumerate(priorities):
        if i == location:
            a.append([p, 1])
        else:
            a.append([p, 0])
            
    print(a)
    
  #  a.sort(key=lambda x : x[0], reverse=True)
    
    # 완전히 pop 한 것을 stack
    s = []
    while a:
        num = a[0]
        
        for aa in a:
            if aa[0] > num[0]:
                a.append(a.popleft())
                break
        else:
            s.append(a.popleft())
        
        print("a: {} , s : {}".format(a, s))
    
    for i, ss in enumerate(s):
        if ss[1] == 1:
            answer = i+1
            break
    else:
        answer = -1
    
    return answer
    
def solution(priorities, location):
    
    queue = [(p, i) for i, p in enumerate(priorities)]
    answer = 0
    
    while True:
        cur = queue.pop(0)
        
        if any( cur[0] < q[0] for q in queue ):
            queue.append(cur)
        else:
            # print할 때마다 count
            answer += 1
            if cur[1] == location:
                # print했는데 내가 찾던 프린트!
                break
        
    return answer



p1 = [2, 1, 3, 2]
p2 = [1, 1, 9, 1, 1, 1]
l1 = 2
l2 = 0

print(solution(p1, l1))
print(solution(p2, l2))





