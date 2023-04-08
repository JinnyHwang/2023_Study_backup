
# https://www.acmicpc.net/problem/23289

# 우 좌 상 하
d = [(0,1),(0,-1),(-1,0),(1,0)]

def wall_check(y, x, di, wall):
    
    for w in wall:
        if di == 0:
            if w[2] == 1 and y == w[0] and x == w[1]:
                return False
        if di == 1:
            if w[2] == 1 and y == w[0] and x-1 == w[1]:
                return False
        if di == 2:
            if w[2] == 0 and y == w[0] and x == w[1]:
                return False
        if di == 3:
            if w[2] == 0 and y-1 == w[0] and x == w[1]:
                return False
            
    return True
    
    

def heater_action( room_map, temp, y, x, di, visited, wall ):
    
    if temp == 0:
        return
    
    if temp != 5:        
        if y>=0 and y<N and x>=0 and x<N:
            # 벽 존재 체크
            if wall_check(y, x, di, wall):
                if visited[y][x] == 0:
                    visited[y][x] = 1
                    room_map[y][x] += temp
                    
    ny = y + d[di][0]
    nx = x + d[di][1]
    
    if ny>=0 and ny<N and nx>=0 and nx<N:
        if di == 0 or di == 1:
            heater_action( room_map, temp-1, ny, nx, di, visited, wall )
            if temp != 5:
                heater_action( room_map, temp-1, ny-1, nx, di, visited, wall )
                heater_action( room_map, temp-1, ny+1, nx, di, visited, wall )
        elif di == 2 or di == 3:
            heater_action( room_map, temp-1, ny, nx, di, visited, wall )
            if temp != 5:
                heater_action( room_map, temp-1, ny, nx-1, di, visited, wall )
                heater_action( room_map, temp-1, ny, nx+1, di, visited, wall )
        


def temp_control(room_map, new_room_map):
    
    for y in range(R):
        for x in range(C):
            
            for i in range(4):
                ny = y + d[i][0]
                nx = x + d[i][1]
                
                if ny>=0 and ny<N and nx>=0 and nx<N :
                    
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
    


R, C, K = map(int, input().split())

room_map = [ list(map(int, input().split())) for _ in range(R) ]

# y,x,d
heater_list = []
chec_temp = []

for r in range(R):
    for c in range(C):
        if room_map[r][c] == 5:
            chec_temp.append([r,c])
        elif room_map[r][c] != 0:
            heater_list.append([r,c,room_map[r][c]-1])

wall_num = int(input())

# t == 0 x,y 기준 위쪽
# t == 1 x,y 기준 우측
wall = [ list(map(int, input().split())) for _ in range(wall_num) ]

while True:

    print('start!')
    for h in heater_list:
        visited = [ [0 for _ in range(C)] for _ in range(R) ]
        print('before h? ', h, '\n room_map? \n', room_map)
        heater_action( room_map, 5, h[0], h[1], h[2], visited, wall)
        print('after room_map? \n', room_map)

    new_room_map = [ [0 for _ in range(C)] for _ in range(R) ]
    temp_control(room_map, new_room_map)
    room_map = new_room_map.copy()
    
    temp_down(room_map)
    
    count = 0
    for ct in chec_temp:
        if room_map[ct[0]][ct[1]] >= K:
            count += 1
    
    if count == len(chec_temp):
        break
    



