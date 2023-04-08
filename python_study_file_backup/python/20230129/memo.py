'''
reply 0 ~ n : 0은 회장이므로 pass

모두를 참여하게 하기 위한 필참멤버는 누구?

그럼 몇 번 참여시 누구가 오는지로 정리?
'''
from collections import deque

def solution(reply):
    
    reply = [[0], [8], [1, 3], [2], [1], [1, 4, 6], [2, 5], [3, 6], [4]]

    r_dic = {}

    for i in range(1,len(reply)):
        for ri in reply[i]:
            r_dic[ri] = r_dic.get(ri, []) + [i]

    # key 사람을 부르면 value 사람들이 참석함
    print(r_dic)

    # 일단 가장 많은 사람을 부를 수 있는 사람을 참여시켜야하지 않을까?
    # 1. 한 번 초대했을 때 가장 많은 사람을 부를 수 있는 사람
    # 2. key값 순서
    # -> 그런데.. 연쇄적으로 부를 수 있게되는데 길이가 상관 있을까..
    # 지금의 정렬 의미 없음
    #reply_2 = sorted(r_dic, key = lambda x : (-len(r_dic[x]), x))
    #print(reply_2)

    min_cnt = len(reply)

    for key in r_dic:

        no_participant = [ i for i in range(1,len(reply))]
        r_q = deque()
        cnt = 0
        r_q.append(key)
        #print(no_participant)
        #print(r_q)

        while no_participant:
            #print(no_participant)
            #print('!!', r_q)
            if not r_q:
                #print('??!', no_participant[0])
                r_q.append(no_participant[0]) #i번 친구가 참석하면?
            #else:
                #print('?!?!?')

            cnt += 1
            while r_q:
                #print(cnt,'?? ', r_q)
                p = r_q.pop()
                no_participant.remove(p)
                
                if not no_participant:
                    break
                
                #print('p? ',p, '  no_participant? ',no_participant)
                if p in r_dic:
                    #r_q.extend(r_dic[p]) 다 넣지 않기
                    #print(r_dic[p])
                    for p2 in r_dic[p]:
                        if p2 in no_participant:
                            r_q.append(p2)

        print(min_cnt, cnt)
        min_cnt = min(min_cnt, cnt)
                    

    answer = 0
    return answer

solution([])
print('!')
