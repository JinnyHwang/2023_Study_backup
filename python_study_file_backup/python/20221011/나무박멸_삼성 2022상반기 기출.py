
# https://www.codetree.ai/frequent-problems/tree-kill-all/description

'''
1. 나무 성장
인접나무 개수만큼

2. 나무 번식
벽, 제초제가 없는 빈칸에 번식
현 개체는 유지
현 개체 값//번식할 수 있는 수 가 번식 나무의 값

3. 제초제 뿌리기
제초제를 뿌렸을 때 가장 많은 나무를 없앨 수 있는 위치에서 뿌리기
제초제는 대각선 방향으로 K만큼 퍼지는데,
벽, 나무가없는 칸을 만나면 더이상 퍼지지 않는다 (제초제 뿌려져 있는데는 상관 없나?)

제초제가 뿌려진 칸에는 나무가 없어지고,
없어진 나무의 수를 결과값에 누적

제초제는 c년만큼 유지됨
만약 이미 제초제가 뿌려져있는 칸에 제초제가 다시 뿌려지면
다시 c년만큼 count

m년동안 반복
'''

def show(l):
    for ll in l:
        print(ll)
    print('\n')

import copy

n, m, k, c = map(int, input().split())

# 나무 그루 수 저장
tree_map = [ list(map(int, input().split())) for _ in range(n) ]

# 제초제 map
toxic_map = [ [ 0 for _ in range(n) ] for _ in range(n) ]

tree_list = []

for y in range(n):
    for x in range(n):
        if tree_map[y][x] > 0:
            tree_list.append([y,x])

# 상 하 좌 우
d = [(-1,0),(1,0),(0,-1),(0,1)]

# 좌상 좌하 우상 우하
d2 = [(-1,-1),(1,-1),(-1,1),(1,1)]

# y,x에서 시작했을 때 없앨 수 있는 나무들 확인
def find_toxic_pos(y, x, tree_map, k):
    
    remove_tree = tree_map[y][x]
    
    for di2 in d2:
        for num in range(1,k+1):
            ny = y + di2[0]*num
            nx = x + di2[1]*num
            if 0 <= ny < n and 0 <= nx < n:
                if tree_map[ny][nx] > 0:
                    remove_tree += tree_map[ny][nx]
                elif tree_map[ny][nx] == 0 or tree_map[ny][nx] == -1:
                    break
                    
    return remove_tree


def find_remove_tree(y, x, tree_map, toxic_map, k, c, tree_list):
    
    tree_map[y][x] = 0
    toxic_map[y][x] = c
    tree_list.remove([y,x])
    
    for di2 in d2:
        for num in range(1,k+1):
            ny = y + di2[0]*num
            nx = x + di2[1]*num
            if 0 <= ny < n and 0 <= nx < n:
                if tree_map[ny][nx] > 0:
                    tree_map[ny][nx] = 0
                    toxic_map[ny][nx] = c
                    tree_list.remove([ny,nx])
                elif tree_map[ny][nx] == 0 or tree_map[ny][nx] == -1:
                    toxic_map[ny][nx] = c
                    break


total_remove_tree = 0
turn = m
while turn:
    
    '''
    print('start! ',turn,'year')
    
    print('tree_map')
    show(tree_map)
    print('toxic_map')
    show(toxic_map)
    print('\ntree_list ',tree_list)
    '''
    
    # 나무 성장
    for tl in tree_list:
        cnt = 0
        for di in d:
            ny = tl[0] + di[0]
            nx = tl[1] + di[1]
            if 0 <= ny < n and 0 <= nx < n:
                if [ny,nx] in tree_list:
                    cnt += 1
        if cnt > 0:
            tree_map[tl[0]][tl[1]] += cnt
    
    
    #print('grow tree_map')
    #show(tree_map)
    
    
    # 나무 번식
    tree_map_copy = copy.deepcopy(tree_map)
    new_tree_list = []
    for tl in tree_list:
        next_tree = []
        for di in d:
            ny = tl[0] + di[0]
            nx = tl[1] + di[1]
            if 0 <= ny < n and 0 <= nx < n:
                if toxic_map[ny][nx] == 0 and tree_map_copy[ny][nx] == 0:
                    next_tree.append([ny,nx])
        
        #print('what tree? ',tl)
        #print('what next_tree? ',next_tree)
        
        for nt in next_tree:
            if tree_map_copy[tl[0]][tl[1]]//len(next_tree) > 0:
                tree_map[nt[0]][nt[1]] += tree_map_copy[tl[0]][tl[1]]//len(next_tree)
                if [nt[0],nt[1]] not in new_tree_list:
                    new_tree_list.append([nt[0],nt[1]])
                
    tree_list.extend(new_tree_list)
    #new_tree_list = []
    
    #print('spread tree_map')
    #show(tree_map)
    #print('\ntree_list ',tree_list)
    
    
    # 가장 많은 나무를 없앨 수 있는 좌표는?
    max_tree = -1e9
    max_pos = [n+1,n+1]
    for tl in tree_list:
        change_flag = 0
        y = tl[0]
        x = tl[1]
        
        remove_tree = find_toxic_pos(y, x, tree_map, k)
        
        if max_tree < remove_tree:
            change_flag = 1
            
        elif max_tree == remove_tree:
            if max_pos[0] > y: # remove_tree의 행이 더 작은 경우
                change_flag = 1
                
            elif max_pos[0] == y:
                if max_pos[1] > x: # remove_tree의 열이 더 작은 경우
                    change_flag = 1
                    
        if change_flag:
            max_tree = remove_tree
            max_pos = [y,x]
            
    #print('max_tree? ', max_tree)
    #print('max_pos? ', max_pos)
    
    
    for y in range(n):
        for x in range(n):
            if toxic_map[y][x] > 0:
                toxic_map[y][x] -= 1
            
    
    # max_tree, max_pos
    find_remove_tree(max_pos[0], max_pos[1], tree_map, toxic_map, k, c, tree_list)
    total_remove_tree += max_tree
    
    turn -= 1
    '''
    print('tree_map')
    show(tree_map)
    print('toxic_map')
    show(toxic_map)
    print('\ntree_list ',tree_list)
    '''              
    

    
print(total_remove_tree)

