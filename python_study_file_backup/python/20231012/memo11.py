


# 상:0 우:1 하:2 좌:3
dxs = [-1,0,1,0]
dys = [0,1,0,-1]
# 플레이어 이동
change_dir = { 0:2, 1:3, 2:0, 3:1 }
#nx, ny = x+p_dxs[d], y+p_dys[d]
#if not in_range(nx, ny):
#    nd = change_dir[d]
#    nx, ny = x+dxs[nd], y+dys[nd]

n, m, k = tuple(map(int, input().split()))
game_start_map = [list(map(int, input().split())) for _ in range(n)]
player_start_info = [list(map(int, input().split())) for _ in range(m)]

# game grid 위치 값을 1~n*n으로 잡아서 key값으로 쓰기
idx = 0
# key값으로 쓰일 grid
grid_key = [[0 for _ in range(n)] for _ in range(n)]
for i in range(n):
    for j in range(n):
        grid_key[i][j] = idx
        idx += 1
print(grid_key)

# 총 뺄 때
# gun_info_dic[key].sort()
# new_gun = gun_info_dic[key][-1]
# 변경 시 gun_info_dic[key].pop()
gun_info_dic = {}
for i in range(n):
    for j in range(n):
        if game_start_map[i][j] == 0:
            gun_info_dic[grid_key[i][j]] = gun_info_dic.get(grid_key[i][j], [])
        else:
            gun_info_dic[grid_key[i][j]] = gun_info_dic.get(grid_key[i][j], [game_start_map[i][j]])
print(gun_info_dic)

'''
gun_info_dic[3].append(100)
gun_info_dic[3].append(5)
print(gun_info_dic)

gun_info_dic[20].append(100)
print(gun_info_dic)

gun_info_dic[3].sort()
print(gun_info_dic)
print(gun_info_dic[3][-1])

gun_info_dic[3].pop()
print(gun_info_dic)
print(gun_info_dic[3][2])
'''
print(player_start_info)
# player_list의 index 정보
P_POS = 0 # player_list[idx][P_POS]
P_D = 1 # player_list[idx][P_D]
P_S = 2 # player_list[idx][P_S]
P_GUN = 3 # player_list[idx][P_GUN]
player_list = []
for i,(x,y,d,s) in enumerate(player_start_info):
    new_info = [(x-1,y-1),d,s,0]
    player_list.append(new_info)
print(player_list)

player_point = [0 for _ in range(m)]

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < n

# 한 플레이어를 움직여서 새로운 위치, 방향 return
def move(x,y,d):
    print('x,y,d',x,y,d)
    nx, ny = x+dxs[d], y+dys[d]
    if not in_range(nx, ny):
        nd = change_dir[d]
        nx, ny = x+dxs[nd], y+dys[nd]
        print('!! nx,ny,nd',nx,ny,nd)
    else:
        nd = d
        print('?? nx,ny,nd',nx,ny,nd)
    return (nx,ny,nd)

def chk_other_player(ci,cx,cy):
    
    for i,((x,y),_,_,_) in enumerate(player_list):
        if i == ci:
            continue
        if (cx,cy) == (x,y):
            return i
    return -1

# 현재 위치의 key값, 현재 플레이어의 총
def select_gun(g_key, p_gun):
    global gun_info_dic
    # 총 리스트에서 가장 쎈 총 확인
    gun_info_dic[g_key].sort()
    new_gun = gun_info_dic[g_key][-1]
    # 공격력이 가장 쎈 총을 return
    if new_gun > p_gun:
        gun_info_dic[g_key].pop()
        if p_gun != 0: # 들고있던 총 놓고가기
            gun_info_dic[g_key].append(p_gun)
        return new_gun
    else:
        return p_gun

def drop_gun(g_key, p_gun):
    global gun_info_dic
    
    if p_gun != 0:
        gun_info_dic[g_key].append(p_gun)

# 싸움 결과 return과 player_point획득
def fight_player(ci, oi):
    curr_player = player_list[ci]
    other_player = player_list[oi]
    print('ci? ', ci, 'curr_player? ', curr_player)
    print('oi? ', oi, 'other_player? ', other_player)
    
    curr_pwr = curr_player[P_S]+curr_player[P_GUN]
    other_pwr = other_player[P_S]+other_player[P_GUN]
    
    if curr_pwr > other_pwr:
        player_point[ci] += (curr_pwr - other_pwr)
        print('player_point[ci]? ', player_point[ci])
        return (ci,oi)
    
    elif curr_pwr < other_pwr:
        player_point[oi] += (other_pwr - curr_pwr)
        print('player_point[oi]? ', player_point[oi])
        return (oi,ci)
    
    else: # 같은 경우
        # 각 플레이어의 초기 능력치는 모두 다릅니다
        curr_pwr = curr_player[P_S]
        other_pwr = other_player[P_S]
        
        if curr_pwr > other_pwr:
            return (ci,oi)
        
        else:
            return (oi,ci)



def player_move_dir_90(x,y,d,ci):
    # 현재위치부터 확인
    for i in range(4):
        nd = (d+i)%4
        nx, ny = x+dxs[nd], y+dys[nd]
        print('x,y,d,nx,ny,nd',x,y,d,nx,ny,nd)
        # 격자 안이고, 플레이어가 없을 때 return
        if in_range(nx,ny) and chk_other_player(ci,nx,ny) == -1:
            return (nx,ny,nd) #새로운 좌표, 방향
    return (-1,-1,-1) # 제자리에있기? #아마 이런 경우 없을 것


def lose_player_do(lose_i):
    global player_list
    
    ((x,y),d,s,gun) = player_list[lose_i]
    
    print((x,y),d,s,gun)
    # 총 있으면 두고감
    if gun != 0:
        print('drop gun?')
        g_key = grid_key[x][y]
        print('gun_info_dic', gun_info_dic, ' g_key', g_key)
        drop_gun(g_key, gun)
        player_list[lose_i][P_GUN] = 0
        print('after drop gun?')
        print('gun_info_dic', gun_info_dic, ' player_list[lose_i]', player_list[lose_i])
        
    gun = player_list[lose_i][P_GUN]
    
    # 90도 회전하면서 위치 찾음
    (nx,ny,nd) = player_move_dir_90(x,y,d,lose_i)
    
    # 이동함
    player_list[lose_i][P_POS] = (nx,ny)
    player_list[lose_i][P_D] = nd
    
    # 총 선택함
    g_key = grid_key[nx][ny]
    if gun_info_dic[g_key]:
        # 현재 플레이어 총 획득
        new_gun = select_gun(g_key, gun)
        player_list[lose_i][P_GUN] = new_gun
        
        
    
def win_player_do(win_i):
    global player_list
    
    ((x,y),d,s,gun) = player_list[win_i]
    
    # 이긴 플레이어 총 들고감
    g_key = grid_key[x][y]
    if gun_info_dic[g_key]:
        new_gun = select_gun(g_key, gun)
        player_list[win_i][P_GUN] = new_gun
         


# 순차적으로 플레이어를 움직인다
def move_all_player():
    global player_list
    for i,((x,y),d,s,gun) in enumerate(player_list):
        print('turn ', i, player_list[i])
        print('gun_info_dic', gun_info_dic)
        nx,ny,nd = move(x,y,d)
        player_list[i][P_POS] = (nx,ny)
        player_list[i][P_D] = nd
        
        # 플레이어 있는지 확인
        oi = chk_other_player(i, nx, ny)
        # 다른 플레이어 없음
        if oi == -1:
            print('\nno player')
            g_key = grid_key[nx][ny]
            if gun_info_dic[g_key]:
                # 현재 플레이어 총 획득
                new_gun = select_gun(g_key, gun)
                player_list[i][P_GUN] = new_gun
            print(player_list[i])
                
        #다른 플레이어 있음
        else:
            print('\nyes player')
            print('i, oi', i, oi)
            (win_i,lose_i) = fight_player(i, oi)
            print('win', win_i, player_list[win_i])
            print('lose', lose_i, player_list[lose_i])
            
            # 진 플레이어 행동
            lose_player_do(lose_i)
            
            # 이긴 플레이어 행동
            win_player_do(win_i)
            
            print('\nafter fight')
            print('win', player_list[win_i])
            print('lose', player_list[lose_i])
            print('player_point', player_point)
            
        print('player_list', player_list)
        print('gun_info_dic', gun_info_dic)
        print()
            


def simulate():
    
    for ki in range(k):
        print('K? ', ki)
        # 모든 플레이어 움직임
        move_all_player()
    
    for pp in player_point:
        print(pp,end=' ')
    
    
simulate()   
    
    
    
    
    
    


