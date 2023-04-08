
from collections import deque

q1 = deque([1])
print(q1)

q1.append(2)
print(q1)

q1.extend([3])
print(q1)

if q1:
    print('?')
else:
    print('!')
    
q1.pop()
q1.pop()
q1.pop()
print(q1)

if q1 == []:
    print('?')
else:
    print('!')


'''
양쪽 끝 부분 모양이 동일한 개수 구하기

비교
candy[:n]
candy[len(candy)-n:]

'''
def solution(candy, positions):
    candy = "BPBRBPBRB"
    positions = [3, 6, 9]
    
    answer = []

    # index는 0~p-1
    # p값은 length
    for p in positions:
        cnt = 0
        if p > 1:
            if p%2 == 0:
                pi = p//2
            else:
                pi = p//2+1
            # 확인해야하는 사탕 개수
            # index 0 ~ n-1    candy[0:n]
            # index p-n ~ p-1  candy[p-n:p]
            for n in range(1,pi):
                if candy[0:n] == candy[p-n:p]:
                    #print('candy[0:%d]: '%(n), candy[0:n])
                    #print('candy[%d:%d]: '%(p-n, p), candy[p-n:p])
                    cnt += 1

        answer.append(cnt)

    return answer

