
n = int(input())

food = list( map(int, input().split()) )

d = [0]*n

# 다이나믹 프로그래밍 bottom up
d[0] = food[0]
d[1] = max(food[0], food[1])

print('d[0] : ', d[0], ', d[1] : ', d[1])

# 0번부터 터는가, 1번부터 터는가 확인
# i번째를 터는 것, 이전 창고를 터는 것 어떤것이 더 이득인가 확인
for i in range(2, n) :
    d[i] = max(d[i-1], d[i-2]+food[i])
    print('d[i-1] : %d , d[i-2] : %d, food[i] : %d, d[i] : %d'%(d[i-1], d[i-2], food[i], d[i]))

# 규칙 찾기
# 인접한 칸만 확인
# 어떤 값이 가장 클 까? 누적하여 확인
# 바로 직전에 창고는 터는가? 이전 창고와 지금창고를 터는가?
