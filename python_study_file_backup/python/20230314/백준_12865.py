
N, K = map(int, input().split())
print(N, K)

w = []
v = []
for i in range(N):
    ww, vv = map(int, input().split())
    w.append(ww)
    v.append(vv)

print(w, v)

# 물건 개수, 배낭 용량, 물건 가치
dp = [ [0 for _ in range(K+1)] for _ in range(N) ]

'''
가장 가치 값이 큰 것 배열에 저장
i번째 물건은 넣지 않았을 때  VS  i번째 물건을 넣었을 때
dp[i][j] = dp[i-1][j]  VS  dp[i-1][j-w[i]]+v[i]
'''

for n in range(N):
    for k in range(K+1):
        if k - w[n] >= 0: # n번째 물건을 넣을 수 있는 경우 확인
            dp[n][k] = max( dp[n-1][k], dp[n-1][k-w[n]]+v[n] )
        else: # 물건을 못넣으면 
            dp[n][k] = dp[n-1][k]


print(dp[N-1][K])

