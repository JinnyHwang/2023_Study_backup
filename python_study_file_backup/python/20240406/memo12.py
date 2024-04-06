
n, m = map(int, input().split())
#grid = [list(map(int, input().split())) for _ in range(n)]
max_gold = 0
grid = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    grid[i] = list(map(int, input().split()))
    for j in range(n):
        if grid[i][j] == 1:
            max_gold += m
print(grid)
print(max_gold)

k = 0
while True:
    cost = (k*2)+((k+1)*2)
    if cost > max_gold:
        print(cost)
        k -= 1
        break
    k += 1
print(k)
print((k*2)+((k+1)*2))

# 이번 map에서 최대로 탐색할 k 구함

# 아니다 이렇게 하는게 아님




