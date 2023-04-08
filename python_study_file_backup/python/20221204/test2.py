
R = int(input())
R_height = list(map(int, input().split()))
#print(R_height)

# 모든 돌은 맨 처음에 밟을 수 있음. 경우의 수 1이 가장 기본 값
R_num = [ 1 for _ in  range(R)]
print(R_num)

# 해당 돌까지 올 때 밟게되는 돌의 개수는?
# 내 위치보다 작은 위치에 있는 돌 탐색
answer = 1
for i1 in range(1, R):
    rmax = -1
    for i2 in range(i1):
        if R_height[i1] > R_height[i2] and rmax < R_num[i2]:
            rmax = R_num[i2]
    
    if rmax != -1:
        R_num[i1] = rmax+1
        if answer < R_num[i1]:
            answer = R_num[i1]
    
print(R_num)
print(answer)
