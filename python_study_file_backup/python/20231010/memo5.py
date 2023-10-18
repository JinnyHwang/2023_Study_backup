
# 지금까지 선택된 숫자들의 xor 결과값을 인자값으로 가지고 다니기
import functools

n,m = tuple(map(int, input().split()))
a = list(map(int, input().split()))
ans = 0

def find_max_xor(curr_idx, cnt, curr_val):
    global ans
    
    if cnt == m:
        ans = max(ans, curr_val)
        return
    
    if curr_idx == n:
        return
    
    # 선택 안함
    find_max_xor(curr_idx+1,cnt,curr_val)
    
    # 선택 함
    find_max_xor(curr_idx+1,cnt+1,curr_val^a[curr_idx])
    
find_max_xor(0,0,0)
print(ans)

