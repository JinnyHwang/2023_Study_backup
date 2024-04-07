'''
# 직사각형 최대 크기

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m


def make_square(x, y, len1, len2):
    
    for i in range(x, x+len1):
        for j in range(y, y+len2):
            if not in_range(i,j) or grid[i][j] <= 0:
                return False
    return True


max_sum_size = -1
for i in range(n):
    for j in range(m):
        for len1 in range(1,n+1):
            for len2 in range(1, m+1):
                if make_square(i, j, len1, len2):
                    max_sum_size = max(max_sum_size, len1*len2)
                
print(max_sum_size)       
'''

# 해설
# 전처리?
# (i,j)를 시작으로 밑으로 쭉 내려가면서 만들 수 있는 가로 가로가 1인 직사각형 중 최대 크기
# down max를 미리 구해서 구할 수 있는 직사각형 최대 크기 구하기

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
down_max = [[0 for _ in range(m)] for _ in range(n)]

# 맨 마지막행부터 계산을 시작해서 0번쨰 행까지 계산하며
# 해장 좌표에서 최대로 내려할 수 있는 길이 구함
def preprocessing():
    # 맨 마지막 행 계산
    for j in range(m):
        if grid[n-1][j] > 0:
            down_max[n-1][j] = 1
            
    for i in range(n-2, -1, -1):
        for j in range(m):
            if grid[i][j] > 0:
                down_max[i][j] = down_max[i+1][j] + 1



preprocessing()
ans = -1

for i in range(n):
    for j in range(m):
        best_height = 21
        for l in range(j, m):
            # (i,j)를 시작으로 l-j길이의 직사각형이 가질 수 있는 높이 구하기
            best_height = min(best_height, down_max[i][l])
            ans = max(ans, best_height*(l-j+1))
if ans <= 0:
    ans = -1
            

print(ans)

