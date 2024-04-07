
# 시작 지점, 탐색 길이 정하기
n = int(input())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y <n

# 사각형 만들 수 있을 때만 0보다 큰 값 return
def get_score(x, y, len_1, len_2):    
    # 아래 지점에서 시작
    # 움직이는 방향 정의
    dxs = [-1, -1, 1, 1]
    dys = [1, -1, -1, 1]
    move_nums = [len_1, len_2, len_1, len_2]
    
    sum_of_num = 0
    for dx, dy, move_num in zip(dxs, dys, move_nums):
        for _ in range(move_num):
            x, y = x+dx, y+dy
            if not in_range(x, y):
                return 0
            
            sum_of_num += grid[x][y]
            
    return sum_of_num

max_sum = 0
# 일단 모든 경우의 수 완전 탐색
for i in range(n):
    for j in range(n):
        for len_1 in range(1, n):
            for len_2 in range(1,n):
                max_sum = max(max_sum, get_score(i, j, len_1, len_2))

print(max_sum)



# for문 돌 때 가능한 범위 생각하지 말고 for 문은 일단 완전 탐색으로 진행
# 시작 지점은 x좌표기준 2떨어지고, y좌표기준 양옆으로 1씩 떨어져 있어야 만들 수 있음
#for i in range(2, n):
#    for j in range(1, n-1):
#        sx, sy = i, j
#        for dx, dy in zip(dxs, dys):
#            # 가능한 길이 d 0,2의 길이 d 1,3의 길이
#            for len_1 in range(1,n-sx):
#                for len_2 in range(1, sx+1):
#                    # 만약 range를 벗어나거나 (0,0) (n-1,n-1)이면 pass
#                    nx = cx + dx*len_1
#                   ny = cy + cy*len_2
#                  if in_range(nx, ny):

