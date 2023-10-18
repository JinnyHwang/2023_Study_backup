
# 안전영역 구하기
n, m = tuple(map(int, input().split()))
home_map = [list(map(int,input().split())) for _ in range(n)]
k = max(hh for h in home_map for hh in h)
min_k = min(hh for h in home_map for hh in h)
#print(min_k)
#print(n,m,k)
#print(home_map)

def chk_safe_zone(k):
    
    for i in range(n):
        for j in range(m):
            if safe_zone[i][j] and home_map[i][j] <= k:
                safe_zone[i][j] = 0

def in_range(x,y):
    return 0 <= x and x < n and 0 <= y and y < m


def can_go(x,y):
    
    if not  in_range(x,y):
        return False
    
    if not safe_zone[x][y] or visited[x][y]:
        return False
    
    return True

    
def find_safe_zone(x,y):
    
    dxs = [-1,1,0,0]
    dys = [0,0,-1,1]
    
    visited[x][y] = 1
    
    for dx,dy in zip(dxs,dys):
        nx = x + dx
        ny = y + dy
        if can_go(nx,ny):
            find_safe_zone(nx,ny)

# 안전영역 1로 표시
safe_zone = [[1 for _ in range(m)] for _ in range(n)]
visited = []
chk_k_zone = [-1 for _ in range(k+1)]
# 1~k-1 탐색. k일 땐 어차피 0
# 끝까지 탐색! index1에 값이 0인경우 있다!!
for ki in range(min_k,k+1):
    #safe_zone = [[0 for _ in range(m)] for _ in range(n)]
    # 잠기는 집 표기
    chk_safe_zone(ki)
    print('safe_zone',safe_zone)

    visited = [[0 for _ in range(m)] for _ in range(n)]
    zone_cnt = 0
    # 영역 개수 구하기
    for i in range(n):
        for j in range(m):
            if can_go(i,j):
                find_safe_zone(i,j)
                zone_cnt += 1
    
    chk_k_zone[ki] = zone_cnt
    
    if ki == k or zone_cnt < chk_k_zone[ki-1]:
        print(chk_k_zone)
        print(ki-1,chk_k_zone[ki-1])
        break
    

#print(chk_k_zone)
#max_k = max(chk_k_zone[1:])
#print(max_k)
# 초기값은 나올 수 없는 수로!
'''
max_k = -1
max_ki = -1
for i in range(min_k,k+1):
    if chk_k_zone[i] > max_k:
        max_ki,max_k = i,chk_k_zone[i]
print(max_ki, max_k)
'''