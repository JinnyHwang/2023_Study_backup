
'''
탐욕법(greedy)
알고리즘의 각 단계에서
그 순간 최적이라고 생각되는 것을 선택
현재의 선택이 마지막 해답의 최적성을 해치지 않을 때 사용

앞사람한테 우선 빌리는게 더 많은 경우의 수를 충족시킬 수 있음
1. 최대 학생 수는 30명
=> 번호 순서대로 스탠하면서 빌려줄 관계를 정함

'''

def solution_(n, lost, reserve):
    stu = [ 1 for _ in range(n+2) ]
    print(stu)

    for l in lost:
        stu[l] -= 1
        
    for r in reserve:
        stu[r] += 1
        
    print('1: ', stu)
    
    for i in range(1,n+1):
        if stu[i] == 2:
            if stu[i-1] == 0:
                stu[i] = 1
                stu[i-1] = 1
            elif stu[i+1] == 0:
                stu[i] = 1
                stu[i+1] = 1
    
    print('2: ', stu)
    
    re = 0
    for i in range(1,n+1):
        if stu[i] > 0:
            re += 1
            
    return re
    
    
    
def solution(n, lost, reserve):
    
    stu = [1]*(n+2)
    
    for r in reserve:
        stu[r] += 1
        
    for l in lost:
        stu[l] -= 1
        
    for i in range(1,n-1):
        if stu[i] == 2 and stu[i-1] == 0:
            stu[i-1:i+1] = [1,1]
        elif stu[i] == 2 and stu[i+1] == 0:
            stu[i:i+2] = [1,1]
    
    return len([x for x in stu[1:-1] if x>0])
        



l1 = [2, 4]
r1 = [1, 3, 5]
print(solution(5, l1, r1))

l2 = [2, 4]
r2 = [3]
print(solution(5, l2, r2))

l3 = [3]
r3 = [1]
print(solution(3, l3, r3))


'''
알고리즘 복잡도
n값, lost 길이, reserve 길이에 비례 
O(n)

if 학생의 수가 어마어마하게 많다면?
게다가 여벌 체육복 가져온 학생이 매우 적다면?
학생수 천만명이라 가정하면...
=> 학생수만큼 길이의 배열을 차지해야하므로 공간 너무 차지함
=> 게다가 처리도 길어짐

어떻게 푸는 것이 효율적일까?

1. 가져온 학생 sort ( O(klogk) )
=> 앞뒤로 빌려줄 수 있는 학생 찾기 : 해시를 사용해서 상수시간에 처리

집합자료형 set()은 해시형식


'''

def solution2(n, lost, reserve):
    
    s = set(lost) & set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
            
    return n-len(l)
    

l4 = [1,5,8,3,7]
r4 = [7,5,2,9,6]

print(solution2(10, l4, r4))



def solution(n, lost, reserve):
    
    # 집합으로 풀이
    s = set(lost)&set(reserve)
    l = set(lost) - s
    r = set(reserve) - s
    
    for x in sorted(r):
        if x-1 in l:
            l.remove(x-1)
        elif x+1 in l:
            l.remove(x+1)
        
    return n - len(l)
