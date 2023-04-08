
# https://www.acmicpc.net/problem/23289

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
            
            for i in range(4):
                ny = y + d[i][0]
                nx = x + d[i][1]
                
                if ny>=0 and ny<R and nx>=0 and nx<C :
                    
                    if wall_check(y, x, di, wall):
                    
                        new_temp = abs(room_map[y][x] - room_map[ny][nx])//4
                        
                        if room_map[y][x] >= room_map[ny][nx]:
                            new_room_map[y][x] = new_temp
                            new_room_map[ny][nx] += new_temp
                        else:
                            new_room_map[ny][nx] = new_temp
                            new_room_map[y][x] += new_temp
                            
                        temp_control(room_map, new_room_map, ny, nx)
                

def temp_down(room_map):
    
    for y in range(N):
        for x in range(N):
            if y == 0 or y == N-1 or x == 0 or x == N-1:
                room_map[y][x] -= 1
    


def show(arr):
    for a in arr:
        print(a)
    print('\n')


R, C, K = map(int, input().split())
print('R:{}, C:{}, K:{}'.format(R, C, K))

input_map = [ list(map(int, input().split())) for _ in range(R) ]
room_map = [ [0 for _ in range(C) ] for _ in range(R) ]
show(input_map)

# y,x,d
heater_list = []
check_temp = []

for r in range(R):
    for c in range(C):
        if input_map[r][c] == 5:
            check_temp.append([r,c])
        elif input_map[r][c] != 0:
            heater_list.append([r,c,input_map[r][c]-1])

print('heater_list ', heater_list)
print('check_temp ', check_temp)

wall_num = int(input())

# t == 0 x,y 기준 위쪽
# t == 1 x,y 기준 우측
wall = [ list(map(int, input().split())) for _ in range(wall_num) ]

print('wall ', wall)
for w in wall:
    for i, w2 in enumerate(w):
        if i == 0 or i == 1:
            print(w2)
            w[i] = w2-1
print('wall ', wall)

cnt = 0

while True:
    
    cnt += 1
    if cnt == 3:
        break

    print('start!')
    for h in heater_list:
        visited = [ [0 for _ in range(C)] for _ in range(R) ]
        print('before h? ', h, '\n room_map?')
        show(room_map)
        
        heater_action( room_map, 5, h[0]+d[h[2]][0], h[1]+d[h[2]][1], h[2], visited, wall)
        print('after room_map?')
        show(room_map)

    new_room_map = [ [0 for _ in range(C)] for _ in range(R) ]
    temp_control(room_map, new_room_map)
    room_map = new_room_map.copy()
    
    temp_down(room_map)
    
    count = 0
    for ct in check_temp:
        if room_map[ct[0]][ct[1]] >= K:
            count += 1
    
    if count == len(check_temp):
        break
    



