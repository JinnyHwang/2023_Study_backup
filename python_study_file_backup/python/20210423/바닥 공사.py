
# 가로 길이
n = int(input())

# 덮개 종류 : 1*2 / 2*1 / 2*2

# 바닥을 덮는 모든 경우의 수?

d = [0]*n

d[1] = 1
d[2] = 3

for i in range(3, n) :
    d[i] = (d[i-1] + d[i-2]*2) %796796

print(d[i])

