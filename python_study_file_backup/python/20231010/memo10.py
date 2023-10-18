
n = int(input())
coin_map = [[0 for _ in range(n)] for _ in range(n)]
# 빈공간 0
# start pos : -1
# end pos  : -2
START = -1
END = -2
start_pos = (-1,-1)
end_pos = (-1,-1)
coins_pos = [0 for _ in range(11)]
#l = ''
for i in range(n):
    l = input()
    for j in range(n):
        if l[j] == '.':
            continue
        elif l[j] == 'S':
            coin_map[i][j] = START
            start_pos = (i,j)
        elif l[j] == 'E':
            coin_map[i][j] = END
            end_pos = (i,j)
        else:
            coins_pos[int(l[j])] = (i,j)
            coin_map[i][j] = int(l[j])
            
            
#print(coin_map)
#print(start_pos, end_pos)
#print(coins_pos)

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n


# 각 조합의 이동거리 계산
def cal_move_cnt():
    #start_pos, combi_coin_pos_list, end_pos
    move = 0
    move_list = [start_pos]+combi_coin_pos_list+[end_pos]
    #print(move_list)
    
    for i in range(1,len(move_list)):
        move = move + abs(move_list[i-1][0] - move_list[i][0]) + abs(move_list[i-1][1] - move_list[i][1])
        # move가 12를 넘기면 계산하지 않음
        
    return move
    


# 동전을 뽑은 모든 조합
# coins_pos
combi_coin_pos_list = []
min_move_cnt = 1e9
def coin_select(idx, coin_cnt):
    global min_move_cnt
    
    if coin_cnt == 3:
        #print(combi_coin_pos_list)
        #print(cal_move_cnt())
        min_move_cnt = min(min_move_cnt, cal_move_cnt())
        return
    
    for i, c in enumerate(coins_pos, start=1):
        # 동전이 있고, 이전에 뽑았던 동전보다 큰값이면 조합 진행
        if c != 0 and i > idx:
            #print(i, c)
            combi_coin_pos_list.append(c)
            coin_select(i, coin_cnt+1)
            combi_coin_pos_list.pop()
            

coin_select(0,0)

if min_move_cnt == 1e9:
    print(-1)
else:
    print(min_move_cnt)
 














