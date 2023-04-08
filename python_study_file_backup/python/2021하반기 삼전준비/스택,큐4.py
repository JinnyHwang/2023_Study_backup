def solution1(prices):
    
    count = 0
    answer = [ 0 for _ in range(len(prices)) ]
    stack = [ ]
    
    for i, p in enumerate(prices):
        count += 1
        
        print("stack:{} , answer:{}".format(stack, answer))
        
        if len(stack) == 0 :
            stack.append([i, count])
            continue
        
        print("prices[0]:{}, prices[stack[-1][0]]:{}".format(prices[0], prices[stack[-1][0]]))
        print("?? : ", stack[-1][0], prices[1])
        if p >= prices[stack[-1][0]]:
            stack.append( [i, count] )
        else:
            a = stack.pop()
            print("a : ", a)
            answer[a[0]] = count - a[1]
            stack.append([i, count])
    
    while stack:
        a = stack.pop()
        print("a : ", a)
        answer[a[0]] = count - a[1]
        
    return answer

def solution(prices):
    
    count = 0
    answer = [ 0 for _ in range(len(prices)) ]
    stack = [ ]
    
    for i, p in enumerate(prices):
        count += 1
        
        print("stack:{} , answer:{} , i:{} , p:{}".format(stack, answer, i, p))
        
        if len(stack) == 0 :
            stack.append([i, count])
            continue

        print("p:{}, prices[stack[-1][0]]:{}, prices[{}-1]:{}".format(p, prices[stack[-1][0]], i, prices[i-1] ))
        if p >= prices[stack[-1][0]]:
            stack.append( [i, count] )
        else :
            if any( p > pp for pp in prices[i+1:] ):
                a = stack.pop()
                answer[a[0]] = count - a[1]
                if i+1 < len(prices) and  p < prices[i+1] :
                    stack.append([i, count])
    
    # stack에 있는 원소 모두 빼기
    while stack:
        a = stack.pop()
        answer[a[0]] = count - a[1]
        
    return answer

print(solution([1, 2, 3, 2, 3]))
#print(solution([1, 2, 3, 2, 3, 3] ))
#print(solution([2, 3, 4, 5, 1]))

print(solution([6, 6, 3, 2, 1, 7, 9, 4]))

