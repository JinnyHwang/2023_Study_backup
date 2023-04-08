def solution(answers):
    
    a = [1, 2, 3, 4, 5, 0]
    b = [2, 1, 2, 3, 2, 4, 2, 5, 0]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5, 0]
    
    result = []
    
    for i, ans in enumerate(answers):
        
       # print("ans:{} / a:{} / b:{} / c:{}".format(ans, a[i%5], b[i%8], c[i%10]))
        
        if a[i%5] == ans:
            a[-1] += 1
            
        if b[i%8] == ans:
            b[-1] += 1
            
        if c[i%10] == ans:
            c[-1] += 1
      #  print("a:{}  b:{}  c:{}".format(a[-1], b[-1], c[-1]))
            
    print("a:{}  b:{}  c:{}".format(a, b, c))
    
    result = [a[-1], b[-1], c[-1]]
    print(result.index(max(result)))
    
    re = [ i for i, r in enumerate(result, start=1) if r == max(result) ]
    print(re)
    
    return re

l1 = [1,3,2,4,2,1,3,2,4,2,1,3,2,4,2]
l2 = [1,2,3,4,5]
l3 = [1,3,2,4,2]

print(solution(l3))