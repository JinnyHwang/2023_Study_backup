import sys

COIN_NUM = 9
INT_MAX = sys.maxsize

n = int(input())
m = 3 #최솟값을 구해야하는 문제이므로 최소구슬
grid = [ input() for _ in range(n) ]

coin_pos = list()
selected_pos = list()
start_pos = (-1,-1)
end_pos = (-1,-1)

ans = INT_MAX

for i in range(n):
    for j in range(n):
        if grid[i][j] == 'S':
            start_pos = (i,j)
        if grid[i][j] == 'E':
            end_pos = (i,j)

for num in range(1,COIN_NUM+1):
    for i in range(n):
        for j in range(n):
            # 작은 coin position부터 input하기 위함
            if grid[i][j] == str(num):
                coin_pos.append((i,j))

def dist(a,b):
    (ax,ay),(bx,by) = a,b
    return abs(ax-bx)+abs(ay-by)

def calc():
    num_moves = dist(start_pos, selected_pos[0])
    for i in range(m-1):
        num_moves += dist(selected_pos[i], selected_pos[i+1])
    num_moves += dist(selected_pos[m-1], end_pos)
    
    return num_moves

def find_min_moves(curr_idx,cnt):
    global ans
    
    if cnt == m:
        ans = min(ans,calc())
        return
    
    if curr_idx == len(coin_pos):
        return
    
    # 동전 선택
    selected_pos.append(coin_pos[curr_idx])
    find_min_moves(curr_idx+1,cnt+1)
    selected_pos.pop()
    
    # 동전 선택 안함
    find_min_moves(curr_idx+1,cnt)


find_min_moves(0,0)
if ans == INT_MAX:
    ans = -1
print(ans)

