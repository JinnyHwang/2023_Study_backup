
print((1-0)%8)

l = [[1,2],[1,2],[3,4]]
print(l)

l = [0,0,0]
l[0] = [1,2]
print(l)

'''
모든 경우의 수를 계산해본 뒤 원하는 결과 값을 찾는 방식
표준 라이브러리 없이 구현해보기
조합
순열
중복조합
중복순열
'''

'''
순열 : 주어진 수열에서 순서에 따라 결과가 달라지는 방식
순서가 존재하는 열
(1,2,3),(2,3,1),(3,1,2) : 모두 다른 것

조합: 순서 상관 없음. 구성을 봄
(1,2,3),(2,3,1),(3,1,2) : 모두 같은 것

중복조합
(1,2) == (2,1) 동일하게 보는 것은 똑같음
그런데 (1,1) (2,2) 이렇게 한 숫자가 여러번 나오는 것 허용

'''
max = 5
sel = [0 for _ in range(max)]
arr = [1,2,3,4,5]

def print_arr():
    for i in range(max):
        if sel[i] == 1:
            print(arr[i], end=' ')
    print()

def DFS1(idx, cnt):
    
    if cnt == 3:
        print_arr()
        return
    
    for i in range(idx, max):
        if sel[i] == 1:
            continue
        
        sel[i] = 1
        DFS1(i, cnt+1)
        sel[i] = 0
        
sel2 = [0 for _ in range(3)]
def DFS2(idx, cnt):
    
    if cnt == 3:
        for s in sel2:
            print(s,end=' ')
        print()
        return
    
    for i in range(idx, max):
        sel2[cnt] = arr[i]
        DFS2(i, cnt+1)
        
'''
print('\nDFS1')      
DFS1(0,0)
print('\nDFS2')
DFS2(0,0)
'''


'''
순열 
'''

sel3 = [0 for _ in range(max)] # 숫자 중복 없게 하려고 사용
soon = []

# 순열
def DFS3(cnt):
    
    if cnt == 3:
        for s in soon:
            print(s,end=' ')
        print()
        return
    
    for i in range(max):
        if sel[i] == 1:
            continue
        
        sel[i] = 1
        soon.append(arr[i])
        DFS3(cnt+1)
        sel[i] = 0
        soon.pop()
        
# 중복순열
sel4 = [0 for _ in range(3)]
def DFS4(cnt):
    
    if cnt == 3:
        for s in sel4:
            print(s,end=' ')
        print()
        return
    
    for i in range(max):
        sel4[cnt] = arr[i]
        DFS4(cnt+1)
        
'''
print('\nDFS3')
DFS3(0)
print('\nDFS4')
DFS4(0)
'''
# for문 진행 시 i ~ max-1(조합) or 0 ~ max-1(순열)
# 상 좌 하 우
sd = [(-1,0),(0,-1),(1,0),(0,1)]

M, S = map(int, input().split())
mat_fish = [[list() for _ in range(4)] for _ in range(4)]
for _ in range(M):
    r, c, d = map(int, input().split())
    mat_fish[r-1][c-1].append(d-1)
    #fish.append([r-1, c-1, d-1])
print(mat_fish)
sr,sc = map(int, input().split())
shark = [sr-1,sc-1]
print(shark)

s_move_d = [-1 for _ in range(3)]
eat_fish = -1

s_move_point = set() #원소로 리스트 사용할 수 없음!!
s_move_point_test = [[] for _ in range(3)]

def DFS_shark(cnt, cur, eat_move):
    
    global s_move_d, max_fish, shark
    
    if cnt == 3:
        eat_fish = 0
        v_check = []
        for sr, sc in s_move_point_test:
            if [sr,sc] not in v_check:
            #print('!!',sr,sc,len(mat_fish[sr][sc]))
                eat_fish += len(mat_fish[sr][sc])
                v_check.append([sr,sc])
        print('?' , eat_fish, eat_move, s_move_point, s_move_point_test)
        if max_fish <= eat_fish:
            max_fish = eat_fish
            shark = cur
            print('!!' , eat_fish, eat_move, s_move_point, s_move_point_test, cur)
        return
        
    for i in range(4):
        nr = cur[0]+sd[i][0]
        nc = cur[1]+sd[i][1]
        if 0 <= nr < 4 and 0 <= nc < 4:
            
            eat_move[cnt] = i
            #s_move_point.add([nr,nc])
            s_move_point_test[cnt] = [nr,nc]
            
            DFS_shark(cnt+1, [nr,nc], eat_move)
            
            s_move_point.discard((nr,nc))
            
    
'''
for _ in range(1):
    
    max_fish = -1
    s_move_d = [-1 for _ in range(3)]
    DFS_shark(0, shark, [0,0,0])
    print(max_fish, shark)
'''





