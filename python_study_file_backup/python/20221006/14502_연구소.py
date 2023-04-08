'''
바이러스가 퍼질 수 없는 안전 영역의 최대 크기는?

벽은 빈칸에 세울 수 있다
벽을 세운 후 바이러스를 퍼트림
0의 영역이 가장 큰 최댓값을 구해라

1. 안전 영역 구하기
queue를 사용해 BFS 진행


'''

from collections import deque

N, M = map(int, input().split())

lab_map_org = [ list(map(int, input().split())) for _ in range(N) ]
#print(lab_map)

def show(arr):
    for a in arr:
        print(a)
    print('\n')
        

# 상 하 좌 우
d = [(-1,0),(1,0),(0,-1),(0,1)]


########################################################################
# 바이러스 퍼트리기
########################################################################
def spread_virous(lab_map):
    
    visited = [ [ 0 for _ in range(M) ] for _ in range(N)]
    
    while True:
        
        q = deque()
        
        virous_pos = find_num_pos(lab_map, visited, 2)
        if virous_pos:
            q.append(virous_pos)
            visited[virous_pos[0]][virous_pos[1]] = 1
        else:
            break
        
        while q:
            pos = q.pop()
            
            for i in range(4):
                ny = pos[0] + d[i][0]
                nx = pos[1] + d[i][1]
                
                if ny >= 0 and ny < N and nx >= 0 and nx < M:
                    if lab_map[ny][nx] == 0 and visited[ny][nx] == 0:
                        q.append([ny,nx])
                        visited[ny][nx] = 1
                        lab_map[ny][nx] = 2
                        
    #show(visited)
    #show(lab_map)
########################################################################

########################################################################
# 안전 영역 탐색해서 가장 큰 값 return 하는 함수
########################################################################
def find_num_pos(lab_map,visited,num):
    for y in range(N):
        for x in range(M):
            if lab_map[y][x] == num and visited[y][x] == 0:
                return [y,x]
    return []


def search_safe(lab_map):
    visited = [[ 0 for _ in range(M) ] for _ in range(N)]
    safe_size = 0
    
    while True:
        q = deque() 
        
        zero_pos = find_num_pos(lab_map, visited, 0)
        if zero_pos:
            q.append(zero_pos)
            visited[zero_pos[0]][zero_pos[1]] = 1
            safe_size += 1
        else:
            #print('No safety zone!')
            break
        
        while(q):
            pos = q.pop()
            
            for i in range(4):
                ny = pos[0] + d[i][0]
                nx = pos[1] + d[i][1]
                
                if ny >= 0 and ny < N and nx >= 0 and nx < M:
                    if lab_map[ny][nx] == 0 and visited[ny][nx] == 0:
                        q.append([ny,nx])
                        visited[ny][nx] = 1
                        safe_size += 1
                        
    return safe_size
########################################################################

########################################################################
# 3개 뱍을 세우는 모든 경우의 수
########################################################################
from itertools import combinations
import copy

safe_list = []

zero_zone = []
for y in range(N):
    for x in range(M):
        if lab_map_org[y][x] == 0:
            zero_zone.append([y,x])

#print(zero_zone)

combi = list(combinations(zero_zone,3))
#print(combi)

lab_map_cp = []

for c in combi:
    lab_map_cp = copy.deepcopy(lab_map_org)
    
    for c2 in c:
        lab_map_cp[c2[0]][c2[1]] = 1
        
    spread_virous(lab_map_cp)
    safe_list.append(search_safe(lab_map_cp))
    
    #print('\ncopy')
    #show(lab_map_cp)
    #print('\norg')
    #show(lab_map_org)
    
print(max(safe_list))
    
########################################################################

                        
    

#show(lab_map)
#print(search_safe(lab_map))


# 3개 벽을 세우는 모든 경우의 수 확인


#spread_virous(lab_map)
#safe_list.append(search_safe(lab_map))

#print(max(safe_list))



















