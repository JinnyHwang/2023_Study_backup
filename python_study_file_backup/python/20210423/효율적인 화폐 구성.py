
n, m = map(int, input().split())

data = []
for i in range(n) :
    data.append(int(input()))


d = [10001]*(m+1)

for i in data :
    if i <= m:
        d[i] = 1

for i in range(1, m+1):
    for j in data :
        if (i - j) > 0 :
            if d[i-j] != 10001 :
                d[i] = min(d[i], d[i-j]+1)

if d[m] != 10001 :
    print(d[m])
else :
    print(-1)

