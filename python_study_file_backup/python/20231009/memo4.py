
n,m,c = tuple(map(int, input().split()))
weight = [list(map(int, input().split())) for _ in range(n)]
a = []
max_val = 0

def find_max_sum(curr_idx, curr_weight, curr_val):
    global max_val
    
    if curr_idx == m:
        if curr_weight <= c:
            max_val = max(max_val, curr_val)
        return
    
    # 선택 안함
    find_max_sum(curr_idx+1, curr_weight, curr_val)
    
    # 선택
    find_max_sum(curr_idx+1, curr_weight+a[curr_idx], curr_val+(a[curr_idx]*a[curr_idx]))



def find_max(sx,sy):
    global a, max_val
    
    a = weight[sx][sy:sy+m]
    max_val = 0
    find_max_sum(0,0,0)
    return max_val


def possible(sx1,sy1,sx2,sy2):
    
    last_sy1 = sy1+m-1
    last_sy2 = sy2+m-1
    if last_sy1 >=n or last_sy2 >=n:
        return False
    
    #if sy1 + m - 1 >= n or sy2 + m - 1 >= n:
    #    return False
    
    # 행이 다르면 true!
    if sx1 != sx2:
        return True
    
    return (last_sy1 < sy2 or last_sy2 < sy1)
'''

# 좌표 다 돌려서 안겹치는 경우 value 값 계산
ans = max([
    find_max(sx1,sy1)+find_max(sx2,sy2)
    for sx1 in range(n)
    for sy1 in range(n)
    for sx2 in range(n)
    for sy2 in range(n)
    if possible(sx1,sy1,sx2,sy2)
])
'''

ans = 0
for sx1 in range(n):
    for sy1 in range(n):
        for sx2 in range(n):
            for sy2 in range(n):
                if possible(sx1,sy1,sx2,sy2):
                    fmax = find_max(sx1,sy1)+find_max(sx2,sy2)
                    if ans < fmax:
                        ans = fmax
                        print('ans: ', ans, '  sx1,sy1,sx2,sy2: ', sx1,sy1,sx2,sy2)
print(ans)

