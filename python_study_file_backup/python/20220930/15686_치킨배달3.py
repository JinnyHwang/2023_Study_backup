
'''
https://yangnyang.tistory.com/14

조합

순열

구현하기
'''


N, M = map(int, input().split())

cmap = [list(map(int, input().split())) for _ in range(N)]

house = []
chicken = []

for y in range(N):
    for x in range(N):
        if cmap[y][x] == 1:
            house.append([y,x])
        elif cmap[y][x] == 2:
            chicken.append([y,x])


def h_dis(h, chicken):
    
    min_dis = abs(h[0] - chicken[0][0]) + abs(h[1] - chicken[0][1])

    if len(chicken) > 1:
       for c in chicken[1:]:
           c_dis = abs(h[0]-c[0]) + abs(h[1]-c[1])
           if min_dis > c_dis:
               min_dis = c_dis                     
    return min_dis


def city_dis(chicken):
    
    city_chicken = 0

    for h in house:
        city_chicken += h_dis(h, chicken)
    return city_chicken


# chicken으로 만들 수 있는 M개 원소 조합을 모두 탐색
# 원소가 M개인 치킨 조합 만들기

from itertools import combinations, permutations

# 순열: Permutation
# permutations(list,num)

# 조합: Combinations
# combinations(list,num)


combi = list(combinations(chicken,M))

min_city_dis = 1e9
city_dis1 = 0

for com in combi:
    city_dis1 = city_dis(list(com))
    if min_city_dis > city_dis1:
        min_city_dis = city_dis1

print(min_city_dis)












