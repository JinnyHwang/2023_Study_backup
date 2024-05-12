
from collections import deque

# 기사의 이동
# 상하좌우 중 하나로 한 칸 이동할 수 있습니다
# 한 명이 이동하려하면 연쇄적으로 이동 진행
# 연쇄적 이동 할 때 범위를 벗어나거나, 벽이 있으면 이동하지 못함
# 이동 할 수 있다, 없다 확인

# 이동을 하게 된다면 체력 깍임
# 밀쳐진 기사들 중 이동한 위치에 함정이 있는지 확인

# 기사가 유효한 기사인가?
# 좌표값이 범위 안에 있는지, 체력이 남아있는지 확인
# 변하는 값 기사의 위치 정보, k, 받은 데미지의 합 -> 맨 처음 k를 알면 구할 수 있음
# 생존한 기사들이 총 받은 대미지의 합을 출력합니다.

# 체스판 밖도 벽으로 간주합니다.
# 체스판에서 사라진 기사



# 왕의 명령
# 기사 번호, 방향값
# 0 1 2 3
# 위 오 아 왼
dxs = [-1, 0, 1, 0]
dys = [0, 1, 0, -1]

# L: 체스판의 크기 (3≤L≤40)
# N: 기사의 수 (1≤N≤30)
# Q: 명령의 수 (1≤Q≤100)
# k: 기사의 체력 (1≤k≤100)

def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end= ' ')
        print()
    
L, N, Q = map(int, input().split())

grid = [list(map(int, input().split())) for _ in range(L)]
print_grid(grid)

# 기사 정보
knight_list = []
knight_grid = [[-1 for _ in range(L)] for _ in range(L)]
next_knight_list = []

move_all_knight_visited = [False for _ in range(N)]

def in_range(x, y):
    return 0 <= x < L and 0 <= y < L


def init_knight_pos_info():
    for i in range(L):
        for j in range(L):
            knight_grid[i][j] = -1
            

# 기사 정보 값을 보고 knight_grid를 초기화시키기 위함
def knight_grid_set(num, r, c, h, w, k):
    
    damage = 0
    
    #if k <= 0:
    #    return -1
    
    for i in range(r, r+h):
        for j in range(c, c+w):
            
            #if knight_grid[i][j] != -1:
            #    # 이거 출력되면 기사 이동부터 다시 생각하기
            #    print('knight_pos_info is Fail!!')
            #    
            #else:
            if k <= 0:
                knight_grid[i][j] = -1
            else:
                knight_grid[i][j] = num
                
            if grid[i][j] == 1:
                damage += 1
    return damage
  

# 기사 정보 값을 보고 기사가 다음 칸으로 갈 수 있을지 확인하기 위함
def knight_can_go(knight_num, knight_d):
    global next_knight_list
    
    r, c, h, w, _, _ = knight_list[knight_num]
    
    dx = dxs[knight_d]
    dy = dys[knight_d]
    print('[knight_can_go] r, c?', r, c)
    for i in range(r, r+h):
        for j in range(c, c+w):
            nx, ny = i+dx, j+dy
            print('[knight_can_go] nx, ny?', nx, ny)
            # 밀쳤는데 범위 밖을 벗어나면 이동을 못하는걸까
            # 아님 체스판에서 밀려난 기사가 되는걸까
            if not in_range(nx, ny):
                print('[knight_can_go] not in_range', knight_num, nx, ny)
                return False
            
            if grid[nx][ny] == 2:
                print('[knight_can_go] grid[nx][ny] is 2', knight_num, nx, ny)
                return False
            
    next_knight_list[knight_num][0] = r + dx
    next_knight_list[knight_num][1] = c + dy
    print('[knight_can_go] ', knight_list[knight_num], next_knight_list[knight_num])
    print('[knight_can_go] ', id(knight_list), id(next_knight_list))
    
    return True


def knight_collision(curr_knight_num, knight):
    
    #print('??', knight_list, knight_num)
    print('??', knight)
    r, c, h, w, _, _ = knight
    
    coll_list = []
    for i in range(r, r+h):
        for j in range(c, c+w):
            print('[knight_collision] ', i, j, knight_grid[i][j])
            if knight_grid[i][j] != -1 and curr_knight_num != knight_grid[i][j] and not knight_grid[i][j]  in coll_list:
                coll_list.append(knight_grid[i][j])
    
    print('knight_collision ', coll_list)
    return coll_list         



init_knight_pos_info()
print('knight_grid')
print_grid(knight_grid)

for ni in range(N):
    r, c, h, w, k = map(int, input().split())
    r, c = r-1, c-1
    # 시작위치, 높이/넓이정보, 현재 체력값, 초기 체력값
    # r, c, h, w, k, k
    # x, y = knight_list[i][0], knight_list[i][1]
    # h, w = knight_list[i][2], knight_list[i][3]
    # now_k = knight_list[i][4]
    # first_k = knight_list[i][5]
    knight_grid_set(ni, r, c, h, w, k)
    knight_list.append([r, c, h, w, k, k])

print('knight_grid')
print_grid(knight_grid)
print('knight_list', knight_list)


# 왕의 명령
cmd_list = []
for _ in range(Q):
    num, d = map(int, input().split())
    cmd_list.append((num-1, d))

print(cmd_list)



def move_all_knight(knight_num, knight_d):
    global move_all_knight_visited
    #r, c, h, w, now_k, first_k = curr_knight
    q = deque()
    q.append(knight_num)
    move_all_knight_visited = [False for _ in range(N)]
    move_all_knight_visited[knight_num] = True
    
    while q:
        curr_knight_num = q.popleft()
        print('[move_all_knight] curr_knight_num', curr_knight_num)
        #r, c, h, w, _, _ = knight_list[ki]
        #print(r, c, h, w, now_k, first_k)
        #break
        
        if not knight_can_go(curr_knight_num, knight_d):
            return False
        
        # knight_can_go() True면
        # knight_num의 새로운 x, y 좌표가 next_knight_list에 update됨
        # collision_knight_num = knight_collision(next_knight_list[curr_knight_num])
        collision_knight_list = knight_collision(curr_knight_num, next_knight_list[curr_knight_num])
        print('[move_all_knight] collision_knight_list? ', collision_knight_list)
        if collision_knight_list:
            for ckl in collision_knight_list:
                if not move_all_knight_visited[ckl]:
                    q.append(ckl)
                    move_all_knight_visited[ckl] = True
    
    


# knight_list에서 기사들의 번호로 접근할 수 있고,
# 이동하려는데 다른 기사가 있는지는 knight_grid를 통해 알 수 있다
# knight_grid에 적힌 기사 번호를 보고 knight_list에서 기사를 이동시키면 됨

# 기사들을 이동시킬 때 next_knight_list에 새로운 정보를 넣어가며 초기화 시켜주고
# 이동 실패하면 knight_list / 이동 성공하면 next_knight_list를 사용

# 기사들의 이동이 있을 때 이동 완료 후 knight_grid_set()으로 knight_grid를 초기화해줌
# knight_grid_set()의 return 값을 받으면 현재 기사가 받은 데미지 값도 알 수 있다

for cmd in cmd_list:
    knight_num, knight_d = cmd
    
    
    # 체스판을 벗어난 기사
    #if not in_range(knight_list[knight_num][0], knight_list[knight_num][1]):
    #    continue
    
    
    # 체력이 끝난 기사
    if knight_list[knight_num][4] <= 0:
        continue
    
    
    # 기사들이 이동하면 사용 할 next_knight_list를 초기화
    next_knight_list = []
    for r, c, h, w, now_k, first_k in knight_list:
        #next_knight_list.append(knight_info)
        next_knight_list.append([r, c, h, w, now_k, first_k])
    print('next_knight_list 복사')
    print(knight_list, id(knight_list), id(knight_list[0]))
    print(next_knight_list, id(next_knight_list), id(next_knight_list[0]))
    
    # 시작위치, 높이/넓이정보, 현재 체력값, 초기 체력값
    # r, c, h, w, k, k
    #curr_knight = knight_list[knight_num]
    #r, c, h, w, now_k, first_k = knight_list[knight_num]
    
    # knight_list[knight_num]을 시작으로 기사들을 연쇄적으로 이동시킴
    if move_all_knight(knight_num, knight_d) == False:
        print('기사들의 이동 없이 진행')
        continue
    
    # 기사들이 이동
    #knight_list = next_knight_list[:]
    knight_list = []
    for r, c, h, w, now_k, first_k in next_knight_list:
        #next_knight_list.append(knight_info)
        knight_list.append([r, c, h, w, now_k, first_k])
    print('knight_list', knight_list)
    print('knight_list 복사')
    print(knight_list, id(knight_list), id(knight_list[0]))
    print(next_knight_list, id(next_knight_list), id(next_knight_list[0]))
    print('move_all_knight_visited? ', move_all_knight_visited)
    
    init_knight_pos_info()
    for klnum, (r, c, h, w, now_k, first_k) in enumerate(knight_list):
        # 현재 존재하는 기사만 표기
        if now_k > 0:
            damage = knight_grid_set(klnum, r, c, h, w, now_k)
            if move_all_knight_visited[klnum] and klnum != knight_num:
                next_k = now_k - damage
                if next_k <= 0:
                    # 더이상 존재하지 않게된 기사이므로 다시 grid 초기화
                    knight_grid_set(klnum, r, c, h, w, now_k)
            else:
                next_k = now_k
            knight_list[klnum] = [r, c, h, w, next_k, first_k]
                
    print('knight_grid')
    print_grid(knight_grid)
    print('knight_list', knight_list)
    

output_result = 0
# 살아있는 기사들이 받은 데미지의 합
for _, _, _, _, now_k, first_k in knight_list:
    if now_k > 0:
        re_damage = first_k - now_k
        output_result += re_damage
         
print(output_result)




