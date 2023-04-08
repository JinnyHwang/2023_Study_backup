
N, K = map(int, input().split())
#print(N, K)
score = list(map(int, input().split()))
#print(score)
for _ in range(K):
    s, e = map(int, input().split())
    hap = 0
    for i in range(s-1, e):
        hap += score[i]
    print('%.2f'%(hap/(e-s+1)))





