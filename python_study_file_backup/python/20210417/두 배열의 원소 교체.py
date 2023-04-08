
n, k = map(int, input().split())

#graphA = map(int, input().split())
#graphB = map(int, input().split())

graphA = list(map(int, input().split()))
graphB = list(map(int, input().split()))

resultA = sorted(graphA)
resultB = sorted(graphB, reverse=True)

for i in range(k) :
    resultA[i], resultB[i] = resultB[i], resultA[i]
print(sum(resultA))

# sort()는 list 형식에서만 사용 가능
graphA.sort()
graphB.sort(reverse=True)
for i in range(k) :
    graphA[i], graphB[i] = graphB[i], graphA[i]
print(sum(graphA))
    
