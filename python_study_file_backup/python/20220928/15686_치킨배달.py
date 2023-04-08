'''
0 : 빈 칸
1 : 집
2 : 치킨집

치킨거리


'''

# N: 격자 크기
# M: 치킨집 수
N, M = map(int, input().split())

cmap = [ list(map(int, input().split())) for _ in range(N) ]

#print(N,', ',M)
#print(amap)

home = []
ch = []

for y in range(N):
    for x in range(N):
        if cmap[y][x] == 1:
            home.append([y,x])
        elif cmap[y][x] == 2:
            ch.append([y,x])

print('map: ', cmap)
print('home : ', home)
print('chicken: ', ch)

# 치킨집 개수
ch_cnt = len(ch)

# 제거 횟수
remove = ch_cnt - M


# 도시의 치킨 거리를 구하는 방법
for h in home:
    hy =












