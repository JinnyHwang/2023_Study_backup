

# 번호가 증가하는 순서대로 수집해야만 합니다
# 같은 위치를 2번 이상 지나가는 것 역시 허용
# 해당 위치를 지나가더라도 동전을 수집하지 않아도 되며

# 수집하는 경우 or 안하는 경우 동전 수집을 cnt
# 단 직전에 수집한 동전 숫자보다 커야함

# 최대 이동 횟수는 12


# 이동 횟수, 마지막에 주운 동전 값, 주운 동전 개수

n = int(input())
coin_map = [[0 for _ in range(n)] for _ in range(n)]
# 빈공간 0
# start pos : -1
# end pos  : -2
START = -1
END = -2
start_pos = (-1,-1)
end_pos = (-1,-1)
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
            coin_map[i][j] = int(l[j])
            
            
#print(coin_map)
#print(start_pos, end_pos)

# 상 하 좌 우
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n


min_move_cnt = 13
def search_route(pre_pos, curr_pos, move_cnt, last_coin, coin_cnt):
    global min_move_cnt
    
    if curr_pos == end_pos:
        if coin_cnt >= 3:
            min_move_cnt = min(min_move_cnt, move_cnt)
        return
    
    if move_cnt >= 12:
        return
    
    for i in range(4):
        nx = curr_pos[0] + dx[i]
        ny = curr_pos[1] + dy[i]
        if in_range(nx,ny) and pre_pos != (nx,ny):
            #print(curr_pos, move_cnt, i, nx,ny)
            if coin_map[nx][ny] not in (0,-1,-2):
                if coin_map[nx][ny] > last_coin:
                    # 동전 줍기
                    #print(curr_pos, (nx,ny), move_cnt, coin_map[nx][ny], coin_cnt)
                    search_route(curr_pos, (nx,ny), move_cnt+1, coin_map[nx][ny], coin_cnt+1)
                
            # 동전 안줍기
            search_route(curr_pos, (nx,ny), move_cnt+1, last_coin, coin_cnt)


search_route(start_pos, start_pos, 0, 0, 0)

if min_move_cnt == 13:
    print(-1)
else:
    print(min_move_cnt)


