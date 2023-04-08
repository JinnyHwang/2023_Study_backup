
from collections import deque
import copy

N, M = map(int, input().split())
lab_map = [ list(map(int, input().split())) for _ in range(N) ]

# 상 하 좌 우
d = [(-1,0),(1,0),(0,-1),(0,1)]


def find_num_pos(lab_map,visited,num):
    for y in range(N):
        for x in range(M):
            if lab_map[y][x] == num and visited[y][x] == 0:
                return [y,x]
    return []


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

max_safe_count = 0

# https://mentha2.tistory.com/24
# 벽 3개를 세우는 방법
def select_wall(start, count):
    global max_safe_count
    # 벽 3개 선택 완료
    if count == 3:
        #벽이 선택 된 map 복사
        lab_map_cp = copy.deepcopy(lab_map)
        spread_virous(lab_map_cp)
        safe_count = sum(lm.count(0) for lm in lab_map_cp)
        max_safe_count = max(max_safe_count, safe_count)
        return
    
    # 벽 선택하기
    else:
        # 모든 행,열 탐색
        for i in range(start, N*M):
            y1 = i//M
            x1 = i%M
            if lab_map[y1][x1] == 0:
                lab_map[y1][x1] = 1 #벽 쌓기
                select_wall(i, count+1) # 다음 벽 탐색
                lab_map[y1][x1] = 0 #벽 깨기


select_wall(0,0)
print(max_safe_count)

