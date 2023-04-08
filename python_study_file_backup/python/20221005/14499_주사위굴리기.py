
# 주사위 굴리기
# 주사위 윗면에 적힌 숫자 출력

N, M, y, x, K = map(int, input().split())
#print('N:{}, M:{}, y:{}, x:{}, K:{}'.format(N,M,y,x,K))

#dice_map = [ list(map(int, input().split())) for _ in range(N) ]
dice_map = [ [ int(i) for i in input().split() ] for _ in range(N) ]
#print(dice_map)

#order = list(map(int, input().split()))
order = [ int(x)-1 for x in input().split() ]
#print(order)

# y,x
dice_d = [(0,1), (0,-1), (-1,0), (1,0)]

# 주사위를 굴릴때마다 맨 윗면의 index?
dice = [0, 2, 4]
dice_index = dice[0]
dice_info = [ 0 for _ in range(6) ]
#print(dice, dice_index, dice_info)



# 주사위 굴렸을 때 맨 윗면 인덱스를 구하는 방법!
# 맨 처음 주사위 초기 상태
# 3025  1045

# 우,좌 d[0], d[1]
# 상,하 d[1], d[2]

# dice [0,2,4]
def roll_dice(dice, d):

    if d == 0:  #동
        # dice [3,0,4]
        return [5-dice[1], dice[0], dice[2]]
    elif d == 1:  #서
        # dice [2,5,4]
        return [dice[1], 5-dice[0], dice[2]]
    elif d == 2:  #북
        # dice [4,2,5]
        return [dice[2], dice[1], 5-dice[0]]
    elif d == 3:  #남
        # dice [1,2,0]
        return [ 5-dice[2], dice[1], dice[0]]
    else:
        return []
        
for i in range(K):
    
    d = order[i]
    #print('Turn ', i, ' d? ', d)
    
    # 주사위가 구를 수 있는 지 우선 확인
    ny = y + dice_d[d][0]
    nx = x + dice_d[d][1]
    
    if ny >= 0 and ny < N and nx >= 0 and nx < M:
        #print('ny, nx? ', ny, nx, '  dice_map[ny][nx]? ', dice_map[ny][nx])
        
        #print('before roll: ', dice)
        dice = roll_dice(dice, d)
        dice_index = dice[0]
        #print('after roll: ', dice, '  dice_index? ', dice_index)
        
        #print('\n before action')
        #print('dice_map?\n',dice_map)
        #print('dice_info? ',dice_info)
        if dice_map[ny][nx] == 0:
            dice_map[ny][nx] = dice_info[5-dice_index]
        else:
            dice_info[5-dice_index] = dice_map[ny][nx]
            dice_map[ny][nx] = 0
        #print('\n after action')
        #print('dice_map?\n',dice_map)
        #print('dice_info? ',dice_info)
        y = ny
        x = nx
        print(dice_info[dice_index])
    
    

