
# 도망자 방향
#방향: 좌우(오른쪽시작) , 상하(아래쪽시작)
do_d = [[(0,1),(0,-1)],[(1,0),(-1,0)]]

n = 5
m = 3
sul_pos = [0,0]

def show(l):
    for ll in l:
        print(ll)
    print('\n')
    
    
def func_do_move(y,x,di1,di2):
    
    ny = y + do_d[di1][di2][0]
    nx = x + do_d[di1][di2][1]
    
    if 0 <= ny < n and 0 <= nx < n:
        if sul_pos is [ny,nx]:
            return [y,x,di1,di2]
        else:
            return [ny,nx,di1,di2]
    else:
        ndi2 = (di2+1)%2
        ny = y + do_d[di1][ndi2][0]
        nx = x + do_d[di1][ndi2][1]
        if sul_pos != [ny,nx]:
            return [ny,nx,di1,ndi2]
        else:
            return [y,x,di1,ndi2]


do_list = []     
    
for _ in range(m):
    y, x, d = map(int, input().split())
    # do_d[do_list[n][2]][do_list[n][3]]
    # do_list[n][2] : do_d[0]좌우 do_d[1]상하 선택
    # do_list[n][3] : do_d[n][0]좌/우  do_d[n][1]상/하 선택
    if d == 1:
        do_list.append([y-1,x-1,0,0])
    elif d == 2:
        do_list.append([y-1,x-1,1,0])
        
        
    

for i in range(10):
    
    print('turn ', i)
    
    print('before move do_list?')
    show(do_list)
    
    list_before = [[0 for _ in range(n)] for _ in range(n)]
    list_after = [[0 for _ in range(n)] for _ in range(n)]
    
    # 도망자 움직임
    for i, do in enumerate(do_list):
        list_before[do[0]][do[1]] = i+1
        # 술래와의 거리 확인 3이하일 때만 움직일 수 있음
        #if abs(do[0]-sul_pos[0])+abs(do[1]-sul_pos[1]) <= 3:
        next_do = func_do_move(do[0],do[1],do[2],do[3])
        do_list[i] = next_do
        list_after[next_do[0]][next_do[1]] = i+1
        
    print('before?')
    show(list_before)
    
    print('after?')
    show(list_after)
    
    print('after move do_list?')
    show(do_list)


