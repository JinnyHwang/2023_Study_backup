
# https://www.acmicpc.net/problem/23289

import copy

# 우 좌 상 하
d = [(0,1),(0,-1),(-1,0),(1,0)]


    
# cknum이 0이면 진행방향만 확인: 벽 한 개 확인
# cknum이 1이면 두 번째 진행방향도 확인 : 벽 두 개 확인
def wall_check(y, x, cknum, di1, di2):
    
    if cknum == 0:
        if wall_map[y][x][di1]:
            return False
    else:
        wy = y + d[di2][0]
        wx = x + d[di2][1]
        if wall_map[y][x][di2]:
            return False
        if wy>=0 and wy<R and wx>=0 and wx<C:
            if wall_map[wy][wx][di1]:
                return False
    
    return True



def heater_action( room_map, temp, y, x, di, visited):
    
    if temp == 0:
        return
    
    #if temp == 5:
    #    visited[y][x] = 1
    
    if y>=0 and y<R and x>=0 and x<C:
        if visited[y][x] == 0:
            room_map[y][x] += temp
            visited[y][x] = 1
            #print('wall check: y:{}, x:{}, di:{}'.format(y,x,di))
            #if wall_check(y, x, di, wall):
                #room_map[y][x] += temp
            #visited[y][x] = 1
    else:
        return
                
                    
    ny = y + d[di][0]
    nx = x + d[di][1]
    
    if ny>=0 and ny<R and nx>=0 and nx<C:
        if di == 0 or di == 1:
            if wall_check(y, x, 0, di, -1):
                heater_action( room_map, temp-1, ny, nx, di, visited )
            if wall_check(y, x, 1, di, 2):
                heater_action( room_map, temp-1, ny-1, nx, di, visited )
            if wall_check(y, x, 1, di, 3):
                heater_action( room_map, temp-1, ny+1, nx, di, visited )
        elif di == 2 or di == 3:
            if wall_check(y, x, 0, di, -1):
                heater_action( room_map, temp-1, ny, nx, di, visited )
            if wall_check(y, x, 1, di, 1):
                heater_action( room_map, temp-1, ny, nx-1, di, visited )
            if wall_check(y, x, 1, di, 0):
                heater_action( room_map, temp-1, ny, nx+1, di, visited )


def temp_control(room_map, new_room_map):
    
    for y in range(R):
        for x in range(C):
            
            if new_room_map[y][x] > 0:
                for i in range(4):
                    ny = y + d[i][0]
                    nx = x + d[i][1]
                    
                    if ny>=0 and ny<R and nx>=0 and nx<C :
                        if wall_check(y, x, 0, i, -1) and new_room_map[y][x] >= new_room_map[ny][nx]:
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
# [우, 좌, 상, 하]
wall_map = [ [ [0 for _ in range(4) ] for _ in range(C) ] for _ in range(R) ]

for _ in range(wall_num):
    y, x, t = map(int, input().split())
    y -= 1
    x -= 1
    if t == 0:
        # y,x 좌표의 위쪽 / y-1,x 좌표의 아래쪽에 벽이 생김
        wall_map[y][x][2] = wall_map[y-1][x][3] = 1
    elif t == 1:
        # y,x 좌표의 오른쪽 / y,x+1 좌표의 왼쪽에 벽이 생김
        wall_map[y][x][0] = wall_map[y][x+1][1] = 1
#print(wall_map)
        
# t == 0 x,y 기준 위쪽
# t == 1 x,y 기준 우측
#wall = [ list(map(int, input().split())) for _ in range(wall_num) ]

#print('wall ', wall)
#for w in wall:
    #w[:2] = [ i1+i2 for i1, i2 in zip(w,[-1,-1]) ]
    #for i, w2 in enumerate(w):
        #if i == 0 or i == 1:
            #print(w2)
            #w[i] = w2-1
#print('wall ', wall)

turn_cnt = 1
while turn_cnt < 101:
    
    #print('\nTurn: ',turn_cnt)
    
    #if turn_cnt == 3:
        #break

    #print('start!')
    for h in heater_list:
        visited = [ [0 for _ in range(C)] for _ in range(R) ]
        #print('before h? ', h, '\n room_map?')
        #show(room_map)
        
        heater_action( room_map, 5, h[0]+d[h[2]][0], h[1]+d[h[2]][1], h[2], visited)
        #print('after room_map?')
        #show(room_map)

    #new_room_map = [ [0 for _ in range(C)] for _ in range(R) ]
    new_room_map = copy.deepcopy(room_map)
    temp_control(room_map, new_room_map)
    #print('result??')
    #show(room_map)
    
    temp_down(room_map)
    #show(room_map)
    
    flag = 0
    for ct in check_temp:
        if room_map[ct[0]][ct[1]] < K:
            flag += 1
    
    if flag == 0:
        break
    
    turn_cnt += 1
 
#show(room_map)
print(turn_cnt)

