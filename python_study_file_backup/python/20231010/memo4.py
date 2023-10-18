import functools

n, m = tuple(map(int, input().split()))
a = list(map(int, input().split()))
visited = [False for _ in range(n)]

ans = 0

def calc():
    val = 0
    for i in range(n):
        if visited[i]:
            val ^= a[i]
    return val

def find_max_xor(curr_idx,cnt):
    global ans
    
    if cnt == m:
        ans = max(ans,calc())
        return
    
    if curr_idx == n:
        return
    
    # 선택 안함
    find_max_xor(curr_idx+1,cnt)
    
    visited[curr_idx] = True
    find_max_xor(curr_idx+1,cnt+1)
    visited[curr_idx] = False

find_max_xor(0,0)
print(ans)




