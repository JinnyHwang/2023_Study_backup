
# 4가지 연산으로 탐색

x = int(input())

d = [0]*100

# bottom up 방식 사용
# d[i]에 저장된 수는 숫자 i에 도달할 때 까지 거쳐온 연산 횟수
for i in range(2, x+1) :

    # 현재의 수에서 1을 빼는 경우
    d[i] = d[i-1] + 1

    # 현재의 수가 2로 나누어 떨어지는 경우
    if i%2 == 0 :
        # 연산 횟수가 더 작은 수로 저장
        d[i] = min(d[i], d[i//2] + 1)

    if i%3 == 0 :
        d[i] = min(d[i], d[i//3]+1)

    if i%5 == 0:
        d[i] = min(d[i], d[i//5]+1)

print(d[x])











