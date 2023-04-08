
# 반복 : 상어가 이동할 수 없을 때까지

# 물고기 이동
# 같은 번호 물고기 없음
# 작은 숫자 물고기 먼저 이동
# 다른 물고기가 있거나 빈칸으로 한 칸씩 이동 가능
# 상어가 있으면 이동 불가능
# 모든 물고기가 이동해야함
# 이동 불가능하면 방향을 45도씩 옮김
# 끝까지 이동 불가능하면 이동 못함


# 상어 이동
# (0,0)에서 시작. 먹은 물고기의 방향을 가짐
# 한 번에 여려개 칸 이동할 수 있음
# 단 물고기가 있는 칸으로만 이동 가능
# 목적지 물고기만 먹고 방향을 상어가 가지게됨
# ---> 여러 경우의 수 나올 수 있다

# 상어가 먹을 수 있는 물고기 최대 합은?
# 정말 모든 경우의 수를 봐야 함
# 결과값 '상어가 먹은 물고기' 수가 중요

# 반복이 끝나면 해당 턴에서 상어가 먹은 물고기 수 return

# 모든 반복을 봤을 때 max()값을 찾으면 됨
# result = max(result, shark_eat)

# 정말 바로 이동이동해서 fish_map을 바꿔주면 됨
# 상어는 [-1, 방향]
# 공란은 [0, 0]
def fish_move(fish_map):
    # 1 ~ 16번까지
    num = 1
    
    while num <= 16:
    #if num == 16:
        #return
        flag = 0
        for i in range(4):
            if num in fish_map[i]:
                for j in range(4):
                    # fish move 시작
                    #print(fish_map[i][j][0], num)
                    
                    if fish_map[i][j][0] == num:
                        num += 1
                        
                        nd = fish_map[i][j][1]-1
                        for _ in range(8):
                            ni = i + d[nd][0]
                            nj = j + d[nd][1]
                            #print(i, j, '/', ni, nj)
                            
                            # 격자를 벗어나면 방향 45도 틀어줌
                            if ni < 0 or ni >= 4 or nj < 0 or nj >= 4:
                                nd = (nd+1)%8
                                continue
                            # 상어를 만나면 방향 45도 틀어줌
                            if fish_map[ni][nj][0] == -1:
                                nd = (nd+1)%8
                                continue
                            
                            # 이동할 수 있는 dn 찾음. 새로운 nd값으로 바꿔서 초기화시켜줌
                            fish_map[i][j][1] = nd+1
                            # 서로 바꿔줌
                            #print(fish_map[i][j], fish_map[ni][nj])
                            fish_map[i][j], fish_map[ni][nj] = fish_map[ni][nj], fish_map[i][j]
                            #print(fish_map[i][j], fish_map[ni][nj])
                            print('??? num: ',num, '\n',fish_map)
                            flag = 1
                            break
                if flag == 1:
                    break
            else:
                if i == 3:
                    num += 1
            if flag == 1:
                break
        #else:
            # 리스트 다 돌았는데 물고기 없음
            # 없는 물고기면 pass
            #num += 1
                        
                    # 방향 다 돌았는데도 갈 데가 없음.
                    # 이 물고기는 이동 안함
                    #else:
                        # pass
                

def shark_move(shark_pos):
    
    x = shark_pos[0]
    y = shark_pos[1]
    
    for i in range(1,4):
        sd = fish_map[x][y][1]-1
        # 상어가 이동할 수 있는 경우의 수?
        nx = x + (d[sd][0]*i)
        ny = y + (d[sd][1]*i)
        
        if 0 <= nx < 4 and 0 <= ny < 4:
            if fish_map[nx][ny] != 0:
                #value = fish_map[nx][ny][0] # 먹은 물고기 크기
                # 상어 이동 가능
                # 탐색 진행
                fish_map[x][y] = [0,0]
                #nx, ny가 상어 좌표
                shark_pos = [nx, ny]
                fish_map[nx][ny] = [-1, fish_map[nx][ny][1]]
                
            else:
                return
                # 상어 이동 불가. 탐색 멈춤
        else:
            return
            # 상어 이동 불가. 탐색 멈춤
    



# map[x][y]
# 0 1 2 3 4 5 6 7
d = [ (-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1) ]
# 45도 반시계는 방향값+1

# 4X4

fish_map = [ [[0,0]]*4 for _ in range(4) ]
print(fish_map)

#x = 1
#y = 2
#fish_map[x][y][1] = 6
#fish_map[x][y] = [3,5]
#fish_map[x][y][0] = 4
#print(fish_map)

l = []

for i in range(4):
    l = list(map(int, input().split()))
    for j in range(0, 8, 2):
        fish_map[i][j//2] = [ l[j], l[j+1] ]
print(fish_map)

shark_pos = [0,0]
fish_map[0][0][0] = -1
print(fish_map)



result = []


con = True
while con:
    fish_move(fish_map)
    print('?',fish_map)
    shark_move(shark_pos)
    if shark_move(shark_pos) == 0:
        print('!',shark_pos)
        print('???',fish_map)
        con = False
        break
    result += 1
    
print(result)





