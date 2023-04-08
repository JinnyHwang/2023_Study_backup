'''

16 4
1 10 4 13 8 3 1 7 1 10 4 13 8 3 1 7


'''

'''
피자도우 말고 펴기

N길이 만큼의 도우

1. 밀가루 양이 가장 적은 도우 확인하여 +1

2. 도우 말아주기

2-1. 초기화
도우 말기 전
roll_dough[n-1] = copy.deepcopy(dough)

도우 말고난 후
dough = copy.deepcopy(roll_dough[n-1])


2-2. 도우 말기

-. 올려야하는 도우 확인
roll_dough[n-1] 값이 있는 가장 첫 위치 start_pos_x
roll_dough[start_pos_y][start_pos_x] 도우 높이
roll_dough[start_pos_y][end_pos_x]

--> 위로 옮겨야하는 도우 크기 : (start_pos_y, start_pos_x)(n-1,end_pos_x)


-. 도우를 더 말 수 있는지 확인
((n-1)-start_pos_y) <= ((n-1)-end_pos_x)
=> 조건에 안맞으면 끝


-. 말아야하는 도우를 (n-1, end_pos_x)을 기준으로 시계방향으로 90도 돌림
그리고 전체적으로 y축방향으로 -1만큼 위치 올림
roll_dough[n-1-1][end_pos_x+1]


3. 도우 펼치기

3-1. 밀가루 분배
n-1, n-1을 시작으로 값이 있는 배열 탐색
값 분배해줌
=> map_copy = copy.deepcopy()


3-2. 도우로 옮기기
dough_index = 0
for y in reversed(range(n-1)):
    for x in range(n-1):
        
        if map[y][x] > 0:
            dough[dough_index] = map[y][x]
            dough_index += 1
            
            if dough_index >= n:
                break
        


4. 도우 반으로 접기
(n//2) : 180도 시계방향 돌리기
(n//2)//2 : 180도 시계방향 돌리기


도우로 옮기기
dough_index = 0
for y in reversed(range(n-1)):
    for x in range(n-1):
        
        if map[y][x] > 0:
            dough[dough_index] = map[y][x]
            dough_index += 1
            
            if dough_index >= n:
                break

5. max(dough) - min(dough) < k


'''

import copy

def show(l):
    for l1 in l:
        print(l1)
    print('\n')
    

def list_copy(list_org, n):
    
    list_copy = [ [ 0 for _ in range(n) ] for _ in range(n)]
    
    for y in range(n):
        for x in range(n):
            list_copy[y][x] = list_org[y][x]
            
    return list_copy


# 도우 길이
n, k = map(int, input().split())

dough = list(map(int, input().split()))


def func_roll_dough(roll_dough, n):
    #t = 1
    #start_y, start_x, end_x = n-1
    while True:
        
        # 위치 값  start_y, start_x , end_y(항상 n-1) , end_x
        
        # start_x 찾기
        for i in range(n):
            if roll_dough[n-1][i] > 0:
                start_x = i
                break
        #print('start_x? ', start_x)
        
        # start_y 찾기
        for i in reversed(range(n)):
            #print('start_y i???', i, '  roll_dough[i][start_x]? ', roll_dough[i][start_x])
            if roll_dough[i][start_x] == 0:
                start_y = i+1
                break
        #print('start_y? ', start_y)
        
        # end_x 찾기
        if start_y != n-1:
            for i in range(start_x, n):
                if roll_dough[start_y][i] == 0:
                    end_x = i-1
                    break
            else:
                end_x = n-1
        #print('end_x? ', end_x)
        
        #print('start_y:{}, start_x:{}, end_x:{}'.format(start_y, start_x, end_x))
        
        #print('((n-1)-start_y)+1? ', ((n-1)-start_y)+1)
        #print('(n-1)-end_x? ',(n-1)-end_x)
        if end_x == n-1 or ((n-1)-start_y)+1 > (n-1)-end_x:
            #print('yep!')
            break
            
        # (start_y, start_x) (n-1, end_x) 크기 옮기기
        roll_dough_copy = list_copy(roll_dough, n)
        #print(id(roll_dough_copy), id(roll_dough))
        #copy.deepcopy(roll_dough)
        
        for y in range(start_y, n):
            for x in range(start_x, end_x+1):
                ny = (n-1)+(x-end_x)-1
                nx = (n-1)-y+end_x+1
                #print('y:{} , x:{} , ny:{} , nx:{} '.format(y,x,ny,nx))
                roll_dough[ny][nx] = roll_dough[y][x]
                roll_dough[y][x] = 0
                
        #print('turn ', t)
        #show(roll_dough)
        #t += 1
                
                
    return [start_y, start_x]

def func_add_dough(roll_dough, roll_dough_startpos):
    
    # 도우 분배하기
    roll_dough_copy = list_copy(roll_dough, n)

    for y in range(roll_dough_startpos[0], n):
        for x in range(roll_dough_startpos[1], n):
            if roll_dough_copy[y][x] > 0:
                for di in d:
                    ny = y + di[0]
                    nx = x + di[1]
                    if 0 <= ny < n and 0 <= nx < n:
                        if roll_dough_copy[ny][nx] > 0:

                            add_dough = abs(roll_dough_copy[y][x] - roll_dough_copy[ny][nx])//5

                            if roll_dough_copy[y][x] > roll_dough_copy[ny][nx]:
                                roll_dough[y][x] -= add_dough
                            elif  roll_dough_copy[y][x] < roll_dough_copy[ny][nx]:
                                roll_dough[y][x] += add_dough






def func_spread_dough(dough, roll_dough, roll_dough_startpos):
    
    dough_index = 0
    
    for x in range(roll_dough_startpos[1], n):
        for y in range(n-1, roll_dough_startpos[0]-1, -1):
            if roll_dough[y][x] > 0:
                dough[dough_index] = roll_dough[y][x]
                dough_index += 1
                
                if dough_index >= n:
                    return
                
                
def func_half_dough(roll_dough):
    
    
    # 처음 반으로 자르기
    for x in range(0, n//2):
        roll_dough[n-2][n-1-x] = roll_dough[n-1][x]
        roll_dough[n-1][x] = 0
    

    
    # 두번째 반으로 자르기
    for y in range(n-1,n-3,-1):
        for x in range(n//2, n//2 + n//4):
            if y == n-1:
                ny = n-4
            elif y == n-2:
                ny = n-3
                
            nx = (n-1)+n//2-x

            roll_dough[ny][nx] = roll_dough[y][x]
            roll_dough[y][x] = 0
    
        
    

# 상 하 좌 우
d = [(-1,0),(1,0),(0,-1),(0,1)]

turn = 0
while True:
    
    turn += 1
    
    # 밀가루 양이 가장 작은 반죽 밀가루 +1
    min_dough = min(dough)
    for i in range(n):
        if dough[i] == min_dough:
            dough[i] += 1
            
    
    # 도우 말아주기
    
    # 턴이 끝날 때 마다 0으로 초기화
    roll_dough = [ [0 for _ in range(n)] for _ in range(n)]
    
    for i in range(n):
        roll_dough[n-1][i] = dough[i]
    
    #roll_dough[n-1] = copy.deepcopy(dough)
    
    # 도우 길이가 1이 아니면 func_roll_dough 시작 전에 한 번 말아줌
    if n != 1:
        roll_dough[n-2][1] = dough[0]
        roll_dough[n-1][0] = 0
        
    # [start_y, start_x, end_x]
    roll_dough_startpos = func_roll_dough(roll_dough, n)    
    
    # 반죽 추가 제거
    func_add_dough(roll_dough, roll_dough_startpos)

    # 도우 펴주기
    func_spread_dough(dough, roll_dough, roll_dough_startpos)
    
    # 도우 반씩 자르기
    roll_dough = [ [0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        roll_dough[n-1][i] = dough[i]
    #roll_dough[n-1] = copy.deepcopy(dough)
    
    func_half_dough(roll_dough)
   
    func_add_dough(roll_dough, [(n-1)-3, n-(n//4)])
  
    # 도우 펴주기
    func_spread_dough(dough, roll_dough, [(n-1)-3, n-(n//4)])
    
    
    if max(dough) - min(dough) <= k:
        break

print(turn)



