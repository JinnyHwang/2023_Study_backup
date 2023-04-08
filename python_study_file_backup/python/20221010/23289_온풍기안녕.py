
# https://www.acmicpc.net/problem/23289

import copy

# 우 좌 상 하
d = [(0,1),(0,-1),(-1,0),(1,0)]

def wall_check(y, x, di, wall):
    
    if di == 0:
        wy = y
        wx = x-1
    elif di == 1:
        wy = y
        wx = x
    elif di == 2:
        wy = y+1
        wx = x
    elif di == 3:
        wy = y
        wx = x
        
    #print('y:{}, x:{}, di:{}, wx:{}, wy:{}'.format(y,x,di,wx,wy))
    
    for i,w in enumerate(wall):
        #print('Turn {} w:{}'.format(i,w))
        if (w[2] == 0 and (di == 2 or di == 3)) or (w[2] == 1 and (di == 0 or di == 1)):
            if w[0] == wy and w[1] == wx:
                #print('False??')
                return False
            
    #print('True??')
    return True
    
    

def heater_action( room_map, temp, y, x, di, visited, wall ):
    
    if temp == 0:
        return
    
    #if temp == 5:
    #    visited[y][x] = 1
    
    if y>=0 and y<R and x>=0 and x<C:
        # 벽 존재 체크
        if visited[y][x] == 0:
            #print('wall check: y:{}, x:{}, di:{}'.format(y,x,di))
            if wall_check(y, x, di, wall):
                room_map[y][x] += temp
            visited[y][x] = 1
                
                    
    ny = y + d[di][0]
    nx = x + d[di][1]
    
    if ny>=0 and ny<R and nx>=0 and nx<C:
        if di == 0 or di == 1:
            heater_action( room_map, temp-1, ny, nx, di, visited, wall )
            heater_action( room_map, temp-1, ny-1, nx, di, visited, wall )
            heater_action( room_map, temp-1, ny+1, nx, di, visited, wall )
        elif di == 2 or di == 3:
            heater_action( room_map, temp-1, ny, nx, di, visited, wall )
            heater_action( room_map, temp-1, ny, nx-1, di, visited, wall )
            heater_action( room_map, temp-1, ny, nx+1, di, visited, wall )
        



def temp_control(room_map, new_room_map):
    
    for y in range(R):
        for x in range(C):
            
            if new_room_map[y][x] > 0:
                for i in range(4):
                    ny = y + d[i][0]
                    nx = x + d[i][1]
                    
                    if ny>=0 and ny<R and nx>=0 and nx<C :
                        if wall_check(ny, nx, i, wall) and new_room_map[y][x] >= new_room_map[ny][nx]:
                            new_temp = (new_room_map[y][x] - new_room_map[ny][nx])//4
                            room_map[y][x] -= new_temp
                            room_map[ny][nx] += new_temp
                

def temp_down(room_map):
    
    for y in range(R):
        for x in range(C):
            if room_map[y][x] > 0:
                if y == 0 or y == R-1 or x == 0 or x == C-1:
                    room_map[y][x] -= 1
    


def show(arr):
    for a in arr:
        print(a)
    print('\n')


R, C, K = map(int, input().split())
#print('R:{}, C:{}, K:{}'.format(R, C, K))

input_map = [ list(map(int, input().split())) for _ in range(R) ]
room_map = [ [0 for _ in range(C) ] for _ in range(R) ]
#show(input_map)

# y,x,d
heater_list = []
check_temp = []

for r in range(R):
    for c in range(C):
        if input_map[r][c] == 5:
            check_temp.append([r,c])
        elif input_map[r][c] != 0:
            heater_list.append([r,c,input_map[r][c]-1])

#print('heater_list ', heater_list)
#print('check_temp ', check_temp)

wall_num = int(input())

# t == 0 x,y 기준 위쪽
# t == 1 x,y 기준 우측
wall = [ list(map(int, input().split())) for _ in range(wall_num) ]

#print('wall ', wall)
for w in wall:
    w[:2] = [ i1+i2 for i1, i2 in zip(w,[-1,-1]) ]
    #for i, w2 in enumerate(w):
        #if i == 0 or i == 1:
            #print(w2)
            #w[i] = w2-1
#print('wall ', wall)

turn_cnt = 0

while True:
    
    turn_cnt += 1
    if turn_cnt > 100:
        turn_cnt = 101
        break

    #print('start!')
    for h in heater_list:
        visited = [ [0 for _ in range(C)] for _ in range(R) ]
        #print('before h? ', h, '\n room_map?')
        #show(room_map)
        
        heater_action( room_map, 5, h[0]+d[h[2]][0], h[1]+d[h[2]][1], h[2], visited, wall)
        #print('after room_map?')
        #show(room_map)

    #new_room_map = [ [0 for _ in range(C)] for _ in range(R) ]
    new_room_map = copy.deepcopy(room_map)
    temp_control(room_map, new_room_map)
    #print('result??')
    #show(room_map)
    
    temp_down(room_map)
    #show(room_map)
    
    count = 0
    for ct in check_temp:
        if room_map[ct[0]][ct[1]] >= K:
            count += 1
    
    if count == len(check_temp):
        break
 
#show(room_map)
print(turn_cnt)
