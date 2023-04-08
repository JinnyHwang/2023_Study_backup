'''
집 리스트 : 변하지 않음

치킨집 리스트

1. 치킨거리 구하기. 집에서 가장 가까운 치킨집 찾기.
2. 도시의 치킨거리 구하기. (누적)
3. 치킨집을 하나씩 폐업시키면서 치킨거리 구하기
치킨 거리가 가장 작은 조합으로 다음 턴 진행
-> 최종 치킨거리 return 하기


[1] 한 도시의 좌표와 치킨리스트가 주어졌을 때 가장 가까운 치킨집 고르기
-> 가장 작은 값 return

[2] 모든 도시 탐색 후 return 값의 합 : 도시의 치킨거리

[3] 도시의 치킨 거리를 비교해서 가장 값이 작은 치킨 리스트 return
-> (치킨집 - M)번 반복

=> 마지막으로 계산된 치킨 거리 return

'''

N, M = map(int, input().split())

cmap = [list(map(int, input().split())) for _ in range(N)]
print('cmap \n', cmap)

house = []
chicken = []

for y in range(N):
    for x in range(N):
        if cmap[y][x] == 1:
            house.append([y,x])
        elif cmap[y][x] == 2:
            chicken.append([y,x])
            
print('house: ', house)
print('chicken: ', chicken)

def h_dis(h, chicken):
    
    min_dis = abs(h[0] - chicken[0][0]) + abs(h[1] - chicken[0][1])
    print('h_dis start! home? ', h, ' chicken[0] & dis1? ',chicken[0], ' ' ,min_dis)

    if len(chicken) > 1:
       for c in chicken[1:]:
           print('c ??? ', c)
           c_dis = abs(h[0]-c[0]) + abs(h[1]-c[1])
           print('min_dis ? ', min_dis)
           print('c_dis ? ', c_dis)
           if min_dis > c_dis:
               min_dis = c_dis
               
    print('h_dis end!! ', min_dis)           
    return min_dis
   
def city_dis(chicken):
    
    city_chicken = 0
    aa = 0
    print('city_dis start! ')
    
    for h in house:
        aa = h_dis(h, chicken)
        city_chicken += aa
        print(' home',h, '  h_dis: ', aa, '  city_chicken: ', city_chicken)
    
    print('city_dis end! ', city_chicken)
    return city_chicken

turn = len(chicken) - M
print('?? turn? ', turn)
answer = 0

if turn == 0:
    print(city_dis(chicken))
else:
    for t in range(turn):
        
        if t == 1:
            break
        
        min_city_dis = 1e9
        min_index = -1
        
        print('\nTurn? ', t)
        
        for index in range(len(chicken)):
            print('\n chicken index: ', index)
            re_chicken = chicken.copy()
            print('chicken id: ', id(chicken), '   re_chicken id: ', id(re_chicken))
            del re_chicken[index]
            print('org \n', chicken)
            print('re chicken \n', re_chicken)
            
            re_chicken_dis = city_dis(re_chicken)
            if min_city_dis > re_chicken_dis:
                min_city_dis = re_chicken_dis
                min_index = index
            print('chicken index end!  min_city_dis: ', min_city_dis, '  min_index: ', min_index)
                
        answer = min_city_dis
        del chicken[index]
        print(' turn end!! answer?? ', answer, ' index?? ', index, ' chicken?? ', chicken, '\n')
        
            
    print('>>> ', answer)
    
    
    













