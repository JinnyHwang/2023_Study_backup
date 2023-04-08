#print( -7//3 ) # -3
#print( 7//3 ) # 2

def solution1(progresses, speeds):
    
    end = []
    
    for data in zip(progresses, speeds) :
       # print("{} {} {} {}".format(i[0], i[1], (100-i[0])//i[1], type((100-i[0])//i[1])))
       # print(i)
        if (100-data[0])%data[1]==0 :
            end.append((100-data[0])//data[1])
        else :
            end.append((100-data[0])//data[1]+1)
        
     #   end[i] = (100-i[0])//i[1] if (100-i[0])%i[1]==0 else (100-i[0])/i[1]+1
  #  print(end)
    
    answer = []
    end_re = end[::-1]
    
    print(end)
    print(end_re)
    
    num = end_re[-1]
    cnt = 1
    
    while len(end_re) > 0:
        
        if num < end_re[-1] :
            num = end_re.pop()
            answer.append(cnt)
            cnt = 1
            print('if : ', end_re)
        else:
            end_re.pop()
            cnt += 1
            print('else : ', end_re)
        
        if len(end_re) == 0:
            answer.append(cnt)
    
    return answer

def solution(progresses, speeds):
    Q = []
    
    for p, s in zip(progresses, speeds):
        # 몫을 음수로 게산하여 음수 몫을 -곱해주면
        # 양수에서 올림한것과 값이 같음!!!!
        # 맨 첫번째 탐색 또는 지금 탐색하는 시간이 이전값보다 크면
        if len(Q) == 0 or Q[-1][0] < -((p-100)//s):
            Q.append([ -((p-100)//s), 1])
        else:
            Q[-1][1] += 1
            
        print("{}  {}".format(Q, Q[-1]))
        
    return [ q[1] for q in Q ]


l1 = [93, 30, 55]
l2 = [95, 90, 99, 99, 80, 99]

s1 = [1, 30, 5]
s2 = [1, 1, 1, 1, 1, 1]



print(solution(l2, s2))








