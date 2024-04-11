'''
# 검은 곳 위치
# (x1 != x2 and y1 != y2) and (abs(x1 - x2) + abs(y1 - y2) == 3)
#dxs = [2, 1, -2, -1, 2, 1, -2, -1]
#dys = [1, 2, -1, -2, -1, -2, 1, 2]
dxs = [-1, -2, -2, -1, 1, 2, 2, 1]
dys = [-2, -1,  1,  2, 2, 1, -1, -2]

#for dx, dy in zip(dxs, dys):
#    nx, ny = 2 + dx, 2 +dy
#    print((nx,ny), end = ' ')
#print()


#import collections
from collections import deque

n = int(input())
visited = [[0 for _ in range(n)] for _ in range(n)]
step = [[0 for _ in range(n)] for _ in range(n)]

r1, c1, r2, c2 = map(int, input().split())
#r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1
start_pos = (r1-1, c1-1)
target_pos = (r2-1, c2-1)


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

if start_pos == target_pos:
    print(0)
else:
    q = deque()

    min_dis = n*n
    #print(min_dis)

    q.append((r1-1, c1-1, 0))
    #print(q)
    while q:
        x, y, dis = q.popleft()
        visited[x][y] = 1
        #print('x, y, dis? ', x, y, dis)
        print(x, y, dis, q)
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x + dx, y +dy
            if in_range(nx, ny) and visited[nx][ny] == 0:
                if (nx, ny) == target_pos:
                    #print('target_pos? ', (x, y), (nx, ny), dis)
                    min_dis = min(min_dis, dis+1)
                    break
                    #return
                else:
                    visited[nx][ny] = 1
                    if dis < step[nx][ny]:
                        step[nx][ny] = dis
                    q.append((nx,ny,dis+1))
                    #print('append?', nx, ny)
                    #print(q)
                    
    if min_dis == n*n:
        print(-1)
    else:
        print(min_dis)
'''



# 해설
import sys
from collections import deque

INT_MAX = sys.maxsize

n = int(input())
r1, c1, r2, c2 = map(int, input().split())
r1, c1, r2, c2 = r1-1, c1-1, r2-1, c2-1

q = deque()
visited = [[0 for _ in range(n)] for _ in range(n)]
step = [[0 for _ in range(n)] for _ in range(n)]

ans = INT_MAX


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

def can_go(x,y):
    return in_range(x, y) and not visited[x][y]

def push(nx, ny, new_step):
    q.append((nx, ny))
    visited[nx][ny] = 1
    step[nx][ny] = new_step
    
def find_min():
    global ans
    
    while q:
        # 가장 먼저 들어온 원소를 뺌
        x, y = q.popleft()
        #print(x, y, step[x][y], q)

        dxs = [-1, -2, -2, -1, 1, 2, 2, 1]
        dys = [-2, -1,  1,  2, 2, 1, -1, -2]
        
        for dx, dy in zip(dxs, dys):
            nx, ny = x+dx, y+dy
            
            if can_go(nx,ny):
                push(nx, ny, step[x][y]+1)

    if visited[r2][c2]:
        ans = step[r2][c2]


push(r1, c1, 0)
find_min()

if ans == INT_MAX:
    ans = -1

print(ans)
















