'''
n, m = map(int, input().split())
combination = []

def find_combination(curr_num, cnt):
    if curr_num == n+1:
        if cnt == m:
            print(cnt)
        return
    
    combination.append(curr_num)
    find_combination(curr_num+1, cnt+1)
    combination.pop()
    
    find_combination(curr_num+1, cnt)
'''
from collections import deque

q1 = deque()
q1.append((1,2))
q1.append((5,3))

q2 = deque()
print(id(q1), id(q2))
print(q1, q2)

q2 = q1[:]
print(id(q1), id(q2))
print(q1, q2)










