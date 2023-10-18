# 도둑이 2명
# 하나의 행에서 [idx][start:start+M]
# 두 도둑의 영역이 겹치면 안
# 한 도둑이 들 수 있는 최대 무게 C
# 가치는 훔친 물건들의 무게^2를 모두 합한 것


N, M, C = tuple(map(int, input().split()))
#print('N, M, C: ', N, M, C)
stuff_grid = []
for _ in range(N):
    stuff_grid.append(list(map(int, input().split())))
#print(stuff_grid)

max_val = 0

# [:end] end에 들어가는 값 range를 보기 위함으로 <= N
def in_range(idx):
    return 0 <= idx and idx <= N

# 물건의 가치
def stuff_value_hap(values):
    return sum( i*i for i in values )
#values = [8,7,1]
#print(stuff_value_hap(values))


# 영역 내 차지할 수 있는 물건
def pick_select_stuff(select_stuff):
    pick_stuff = []
    all_pick_stuff = []
    for sl in select_stuff:
        sl.sort(reverse=True)
        pick_stuff = []
        for ss in sl:
            if sum(pick_stuff)+ss > C:
                continue
            else:
                pick_stuff.append(ss)
        all_pick_stuff += pick_stuff
    
    return all_pick_stuff


def pick_select_stuff_max(stuff):
    pick_stuff = []
    pick_stuff_back = []
    cal_stuff = 0
    stuff.sort(reverse=True)
    for ss in stuff:
        if sum(pick_stuff)+ss > C:
            continue
        else:
            pick_stuff.append(ss)
            if cal_stuff < stuff_value_hap(pick_stuff):
                cal_stuff = stuff_value_hap(pick_stuff)
                pick_stuff_back = pick_stuff[:]
            
    #print('pick_stuff_back, cal_stuff: ', pick_stuff_back, cal_stuff)
    return cal_stuff

# 물건 선택할 수 있는 경우의 수 모두 확인
# curr_weight는 마지막에 확인
def find_max_sum(curr_idx, curr_weight, curr_val):
    global max_val
    
    if curr_idx == M:
        if curr_weight <= C:
            max_val = max(max_val, curr_val)
        return
    
    # 선택 안함
    find_max_sum(curr_idx+1, curr_weight, curr_val)
    
    # 선택
    find_max_sum(curr_idx+1, curr_weight+a[curr_idx], curr_val+(a[curr_idx]*a[curr_idx]))



def find_max():
    global max_val
    
    max_val = 0
    find_max_sum(0,0,0)
    return max_val


# 두 도둑의 영역선택
def select_zone(cnt, select_zone_pos, select_stuff):
    global ans, a
    
    if cnt == 2:
        chk = 0
        for st in select_stuff:
            a = st
            chk +=  find_max()
            ans = max(ans, chk)
        return
    
    '''
    if cnt == 2:
        chk = 0
        for st in select_stuff:
            chk +=  pick_select_stuff_max(st)
        if ans < chk:
            ans = chk
            print('\nchk, select_zone_pos, select_stuff: ',chk, select_zone_pos, select_stuff)
        return
    '''
    '''
    if cnt == 2:
        chk = 0
        for st in select_stuff:
            chk +=  pick_select_stuff_max(st)
        ans = max(ans, chk)
        return
    '''
    '''
    if cnt == 2:
        #print('\nselect_zone_pos, select_stuff: ',select_zone_pos, select_stuff)
        #select_stuff에서 훔칠 물건 선택
        pick_stuff = pick_select_stuff(select_stuff)
        #print('pick_stuff, stuff_value_hap_re: ',pick_stuff, stuff_value_hap_re)
        ans = max(ans, stuff_value_hap(pick_stuff))
        return
    '''
    '''
    if cnt == 2:
        #select_stuff에서 훔칠 물건 선택
        pick_stuff = pick_select_stuff(select_stuff)
        stuff_value_hap_re = stuff_value_hap(pick_stuff)
        if ans < stuff_value_hap_re:
            print('\nselect_zone_pos, select_stuff: ',select_zone_pos, select_stuff)
            print('pick_stuff, stuff_value_hap_re: ',pick_stuff, stuff_value_hap_re)
            ans = stuff_value_hap_re
        return
    '''
 
    for i in range(N):
        for j in range(N):
            # 훔치지 않은 구역
            if in_range(j+M):
                if select_zone_pos[i][j:j+M] == [0 for _ in range(M)]:
                    select_zone_pos[i][j:j+M] = [1 for _ in range(M)]
                    select_stuff.append(stuff_grid[i][j:j+M])
                                            
                    select_zone(cnt+1, select_zone_pos, select_stuff)
                    
                    select_zone_pos[i][j:j+M] = [0 for _ in range(M)]
                    select_stuff.pop()

#pcik_test = pick_select_stuff([[9, 5, 9, 4, 6], [9, 6, 6, 7, 8]])    
#print(stuff_value_hap(pcik_test))
#print(pick_select_stuff_max([9, 5, 9, 4, 6]), pick_select_stuff_max([9, 6, 6, 7, 8]))

ans = 0
select_zone_pos = [[0 for _ in range(N)] for _ in range(N)]
select_stuff = []
select_zone(0, select_zone_pos, select_stuff)
print(ans)
