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

lab_map = [ list(map(int, input().split())) for _ in range(N) ]
#print(lab_map)

def show(arr):
    for a in arr:
        print(a)
    print('\n')
        
            

def find_zero(lab_map,visited):
    for y in range(N):
        for x in range(M):
            if lab_map[y][x] == 0 and visited[y][x] == 0:
                return [y,x]
    return []

# 상 하 좌 우
d = [(-1,0),(1,0),(0,-1),(0,1)]
count_list = []

def search_safe(lab_map):
    visited = [[ 0 for _ in range(M) ] for _ in range(N)]
    
    q = deque() 
    
    zero_pos = find_zero(lab_map, visited)
    if zero_pos:
        q.append(zero_pos)
        visited[zero_pos[0]][zero_pos[1]] = 1
    else:
        print('No safety zone!')
        return
    
    count = 0
    
    while(q):
        pos = q.pop()
        
        for i in range(4):
            ny = pos[0] + d[i][0]
            nx = pos[1] + d[i][1]
            
            if ny >= 0 and ny < N and nx >= 0 and nx < M:
                if lab_map[ny][nx] == 0 and visited[ny][nx] == 0:
                    q.append([ny,nx])
                    visited[ny][nx] = 1
                    count += 1
                elif lab_map[ny][nx] != 0 and visited[ny][nx] == 0:
                    visited[ny][nx] = lab_map[ny][nx]
                    
    
    show(visited)
    count_list.append(count)
        


show(lab_map)
search_safe(lab_map)
print(count_list)





