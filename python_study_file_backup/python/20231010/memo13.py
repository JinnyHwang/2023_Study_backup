
import sys

INT_MAX = sys.maxsize

n = int(input())
num = list(map(int, input().split()))

ans = INT_MAX


def calc():
    diff = 0
    for i in range(2*n):
        # True면 더하고 False면 빼고
        diff = (diff + num[i]) if visited[i] else diff - num[i]
        
    return abs(diff)

def find_min(idx,cnt):
    global ans
    
    if cnt == n:
        ans = min(ans, calc())
        return
    
    if idx == 2*n:
        return
    
    # 현재 숫자를 True 그룹에
    visited[idx] = True
    find_min(idx+1,cnt+1)
    visited[idx] = False
    
    # 현재 숫자를 Flase 그룹에
    find_min(idx+1,cnt)

#find_min(0,0)
#print(ans)

# 해당 코드는 맨 마지막 index까지 모두 탐색해야 계산이 완료될 수 있음
def find_min2(idx,cnt,calc):
    global ans
    
    if idx == 2*n:
        if cnt == n:
            ans = min(ans, abs(calc))
        return
    
    '''
    if cnt == n:
        ans = min(ans, abs(calc))
        return
    
    if idx == 2*n:
        return
    '''
    
    # 확인한 숫자는 플러스
    find_min2(idx+1,cnt+1, calc+num[idx])
    
    # 패쓰한 숫자는 마이너스
    find_min2(idx+1,cnt, calc-num[idx])

find_min2(0,0,0)
print(ans)





