
'''
4*4 격자

몬스터의 초기 위치와 팩맨의 초기 위치는 같을 수도 있습니다

1. 몬스터 복제 시도
monster 똑같은
monster_egg 만들기


2. 몬스터 이동
monster는 한 칸 이동
몬스터 시체가 있거나
팩맨이 있는 경우거나
격자를 벗어나는 방향일 경우
반시계 45도 회전
else 만약 모든 방향 다 탐색했는데 갈 수 없으면 움직이지 않는다


3. 팩맨 이동
3칸을 이동. 현재칸 포함하지 않음.
이동 시 몬스터를 가장 많이 먹을 수 있는 방향으로 진행
만약 경우의 수가 다양하다면
방향의 우선순위로 결정
상 좌 하 우

탐색할 때마다 진행 방향 index와 먹은 몬스터 수를 저장

경우의 수가 다양하면 진행방향 pd_1, pd_2, pd_3을 비교해서 값이 작은거로 선택


진행방향이 정해지면 진행하면서 있는 몬스터를 시체로 만든다
monster 리스트에서 빼기
monster_die에 추가, 3인자값 함께 추가(현재 turn 추가)


4. 몬스터 시체 소멸
monster_die안에 있는 모든 몬스터의 [2] 인자값 -1


5. 몬스터 복제 완성
monster_egg에 있던 리스트
monster extend


'''

def show(l):
    for ll in l:
        print(ll)
    print('\n')

#       ↑,     ↖,      ←,     ↙,   ↓,   ↘,    →,    ↗  
md = [(-1,0),(-1,-1),(0,-1),(1,-1),(1,0),(1,1),(0,1),(-1,1)]

# 상 좌 하 우
pd = [(-1,0),(0,-1),(1,0),(0,1)]

# 우 하 좌 상
#pd = [(0,1),(1,0),(0,-1),(-1,0)]


m, t = map(int, input().split())

# 팩맨 초기 위치
r, c = map(int, input().split())
packman_pos = [r-1, c-1]

monster = []
for _ in range(m):
    r, c, d = map(int, input().split())
    monster.append([r-1,c-1,d-1])
                  
monster_die = []

packman_eat_max = -1

packman_move_d_max = [-1 for _ in range(3)]
#next_packman_pos = [-1,-1]

def func_find_moster_cnt(y,x):
    global monster
    eat_moster_cnt = 0
    for m in monster:
        if [y,x] == m[:2]:
            eat_moster_cnt += 1
            #print('eat monster?',m)
    return eat_moster_cnt
    

def func_move_packman1(y,x,cnt,eat, packman_move_d, visited):
    global packman_move_d_max
    global packman_eat_max
    
    if cnt == 3:
        # 탐색을 우선순위 순서대로 하기 때문에
        # 가장 나중에 추가된 최대값이 가장 우선순위가 높은 것
        #print('\nsearch end cnt:{}, eat:{}, packman_move_d:{}'.format(cnt, eat, packman_move_d), end='')
        #print('change max', packman_eat_max, packman_move_d_max)
        if packman_eat_max < eat:
            packman_eat_max = eat
            # 초기화
            for i in range(3):
                packman_move_d_max[i] = packman_move_d[i]
                
            #next_packman_pos[0] = y
            #next_packman_pos[1] = x
                
            #packman_move_d_max = packman_move_d
            print('change max', packman_eat_max, packman_move_d_max)
        return
    
    for di in range(4):
        ny = y + pd[di][0]
        nx = x + pd[di][1]
        #if [ny,nx] == [2,2]:
            #print('visited[ny][nx]', visited[ny][nx])
        if 0 <= ny < 4 and 0 <= nx < 4 and visited[ny][nx] != 1:
            packman_move_d[cnt] = di
            visited[ny][nx] = 1
            #print('\ncnt?',cnt,'packman_move_d?',packman_move_d,'ny,nx?',ny,nx)
            #neat = func_find_moster_cnt(ny,nx)
            #print('func_find_moster_cnt? ',neat)
            func_move_packman(ny,nx,cnt+1,eat+func_find_moster_cnt(ny,nx),packman_move_d, visited)
            packman_move_d[cnt] = -1
            visited[ny][nx] = 0
        #else:
            #continue
            
def func_move_packman():
    max_cnt = -1
    best_route = [-1, -1, -1]
    
    # 우선순위 순서대로 진행
    for i in range(4):
        for j in range(4):
            for k in range(4):
                m_cnt = get_killed_num(i, j, k)
                
                if m_cnt > max_cnt:
                    max_cnt = m_cnt
                    best_route = [i, j, k]
    
    return best_route


def get_killed_num(dir1, dir2, dir3):
    y, x = packman_pos[0], packman_pos[1]
    killed_num = 0

    # 방문한적이 있는지를 기록합니다.
    v_pos = []

    for move_dir in [dir1, dir2, dir3]:
        ny, nx = y + pd[move_dir][0], x + pd[move_dir][1]
        # 움직이는 도중에 격자를 벗어나는 경우라면, 선택되면 안됩니다.
        if not (0 <= ny < 4 and 0 <= nx < 4):
            return -1
        # 이미 계산한 곳에 대해서는, 중복 계산하지 않습니다.
        if (ny, nx) not in v_pos:
            killed_num += func_find_moster_cnt(ny,nx)
            v_pos.append((ny, nx))
        
        y, x = ny, nx
        
    return killed_num
    




    

turn = 1
while turn <= t:
    
    # 1. 몬스터 복제 시도
    monster_egg = [[0 for _ in range(3)] for _ in range(len(monster))]
    for y in range(len(monster)):
        for x in range(3):
            monster_egg[y][x] = monster[y][x]
            
    print('monster')
    show(monster)
    
    print('monster_egg')
    show(monster_egg)
            
    print('packman pos?',packman_pos)
    #print([2,0] == packman_pos)
    

    # 2. 몬스터 이동
    for mi, m in enumerate(monster):
        for i in range(8):
            nd = (m[2]+i)%8
            ny = m[0] + md[nd][0]
            nx = m[1] + md[nd][1]
            
            # 격자를 벗어나는 방향일 경우
            if not (0 <= ny < 4 and 0<= nx < 4):
                continue
            
            monster_die_flag = 0
            # 몬스터 시체가 있거나
            for md_num in monster_die:
                if [ny,nx] == md_num[:2]:
                    monster_die_flag = 1
                    break
                    
            if monster_die_flag == 1:
                continue
            
            # 팩맨이 있는 경우거나
            if [ny,nx] == packman_pos:
                continue
            
            # 몬스터 이동
            monster[mi] = [ny,nx,nd]
            break
        
        #모든 방향 다 탐색했는데 갈 수 없으면 움직이지 않는다
        else:
            monster[mi] = [m[0], m[1], m[2]]
            #continue
        
    print('monster')
    show(monster)
    
    #print('monster_egg')
    #show(monster_egg)
    
    print('pack man pos?', packman_pos)
    
    # 3. 팩맨 이동
    visited = [[0 for _ in range(4)] for _ in range(4)]
    #visited[packman_pos[0]][packman_pos[1]] = 1
    packman_move_d = [-1 for _ in range(3)]
    packman_eat_max = -1
    packman_move_d_max = [-1 for _ in range(3)]
    #func_move_packman(packman_pos[0],packman_pos[1],0,0, packman_move_d, visited)
    packman_move_d_max = func_move_packman()
    print('packman move?', packman_move_d_max)
    #print('next_packman_pos?',next_packman_pos)
    
    monster_copy = [[0 for _ in range(3)] for _ in range(len(monster))]
    for y in range(len(monster)):
        for x in range(3):
            monster_copy[y][x] = monster[y][x]
    
    # 가장 우선순위가 높은 팩맨 방향값
    sy = packman_pos[0]
    sx = packman_pos[1]
    for pmd in packman_move_d_max:
        ny = sy + pd[pmd][0]
        nx = sx + pd[pmd][1]
        sy = ny
        sx = nx
        print('pd[pmd][0], pd[pmd][1]',pd[pmd][0],pd[pmd][1])
        print('ny,nx?',ny,nx)
        for m in monster:
            if [ny,nx] == m[:2]:
                #print('??')
                if m in monster_copy:
                    monster_copy.remove(m)
                    monster_die.append([ny,nx,3])
    
    packman_pos[0] = ny
    packman_pos[1] = nx
    #print('next_packman_pos?',next_packman_pos)
    print('packman_pos?',packman_pos)
    
    print('현재 몬스터 수:{}, 없어질 수:{}, return되는 몬스터 수:{}'.format(len(monster), packman_eat_max, len(monster) - packman_eat_max+len(monster_egg)))
    
    monster = monster_copy
    
    print('after pack man eat monster')
    show(monster)
    
    print('die monster?')
    show(monster_die)
    
    # 4. 몬스터 시체 소멸
    if monster_die:
        for i in range(len(monster_die)):
            monster_die[i][2] -= 1
    
    monster_die_copy = []
    for mdie in monster_die:
        if mdie[2] != 0:
            monster_die_copy.append(mdie)
            
    monster_die = monster_die_copy
    
    print('remove monster?')
    show(monster_die)
    
    
    # 5. 몬스터 복제 완성
    monster.extend(monster_egg)
    
    print('end monster')
    show(monster)
    
    turn += 1
    print('몬스터 수?',len(monster))


print(len(monster))
    


