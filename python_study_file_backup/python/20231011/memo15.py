
# BFS
# queue로 지금까지 방문한 노드를 관리함
# 시작점으로부터 연결된 모든 정점 전부 장문
# 이미 방문한 정점은 다시 방문하지 않음
'''
def bfs():
    while q:
        curr_v = q.popleft()
        
        for next_v in range(1, VERTICES_NUM+1):
            if graph[curr_v][next_v] and not visited[next_v]:
                print(next_v)
                visited[next_v] = True
                q.append(next_v)
'''

# BFS는 queue가 empty상태가 되기 전까지 계속 탐색을 반복
# DFS는 함수의 인자값으로 현재 위치를 반환해줌
# BFD는 현재 queue에서 가장 앞에 있는 원소를 현재 위치로 설정해줘야함

def push(x,y):
    global order
    
    answer[x][y] = order
    order += 1
    visited[x][y] = 1
    q.append((x,y))
    

def bfs():
    dxs = [1,0]
    dys = [0,1]
    
    while q:
        x,y = q.popleft()
        
        for dx,dy in zip(dxs,dys):
            nx, ny = x+dx, y+dy
            if can_go(nx,ny):
                push(nx,ny)



