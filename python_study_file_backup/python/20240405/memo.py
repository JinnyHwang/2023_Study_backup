
#a, b, c = input().split()
#print(a, b, c)
'''
dir_num = 2
x, y = 1,5
dx = [1,0,-1,0]
dy = [0,-1,0,1]

nx, ny = x+dx[dir_num], y+dy[dir_num]
'''

'''
dic = {'W':0,'S':1,'N':2,'E':3}
dx = [-1, 0, 0, 1]
dy = [0, -1, 1, 0]

cnt = int(input())

cx,cy = 0,0
for _ in range(cnt):
    d, a = input().split()
    nx = cx + (dx[dic[d]])*int(a)
    ny = cy + (dy[dic[d]])*int(a)
    cx, cy = nx, ny

print(cx,cy)
'''
'''
#90도 회전
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]

nd = (d + 1)%4
nx = x + dx[nd]
ny = y + dy[nd]
'''

'''
x, y, d = 0, 0, 0
mapper = {'L':-1, 'R':1, 'F':0}
# 북 동 남 서
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

input_str = input()
for s in input_str:
    nd = (d + mapper[s])%4
    if d == nd:
        nx = x + dx[nd]
        ny = y + dy[nd]
        x,y = nx,ny
    else:
        d = nd
    
print(x,y)
'''
'''
arr1 = [1, 2, 3]
arr2 = [4, 5, 6]
for elem1, elem2 in zip(arr1, arr2):
    print(elem1, elem2)


x, y = 2, 1
dxs, dys = [0, 1, 0, -1], [1, 0, -1, 0]

def in_range(x,y):
    return 0 <= x < 5 and 0 <= y < 5

cnt = 0
for dx, dy in zip(dxs, dys):
    nx, ny = x + dx, y + dy
    if in_range(nx,ny) and a[nx][ny] == 1:
        cnt += 1

print(cnt)
'''
'''
n = int(input())
map1 = [list(map(int, input().split())) for _ in range(n)]
#print(map1)

# 현재위치에서 상하좌우 확인
dxs = [1, -1, 0, 0]
dys = [0, 0, -1, 1]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

def chk_cnt(x,y):
    cnt = 0
    for dx, dy in zip(dxs,dys):
        nx, ny = x + dx, y + dy
        if in_range(nx,ny) and map1[nx][ny] == 1:
            cnt += 1
    return cnt >= 3

result = 0
for i in range(n):
    for j in range(n):
        if chk_cnt(i,j):
            result += 1

print(result)
'''

'''
# 반대로 뒤집기: 3- 현재방향
dx = [0, 1, -1, 0]
dy = [1, 0, 0, -1]

mapper = {'R':0, 'D':1, 'U':2, 'L':3}

# 방향바꾸면 움직이지는 않고 방향만 전환

n, t = map(int, input().split())
r, c, d1 = input().split()
x = int(r)-1
y = int(c)-1
d = mapper[d1]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < n

for _ in range(t):
    nx = x + dx[d]
    ny = y + dy[d]
    if in_range(nx,ny):
        x, y = nx, ny
    else:
        d = 3-d

print(x+1, y+1)
'''
'''

# 정답을 저장할 별도의 이차원 배열 활용
# 막혔을 땐 시계방향으로 90도 틀어주기
dxs = [0, 1, 0, -1]
dys = [1, 0, -1, 0]

# 격자를 벗어나거나, 이미 방문했었거나 : 방향 전환
# nd = (d+1)%4

n = 4
answer = [[0 for _ in range(n)] for _ in range(n)]

def in_range(x, y):
    return 0 <= x < n and 0 <= y < n

x, y, d = 0, 0, 0
answer[x][y] = 1

# n*n번 진행 : 격자 크기만큼 진행함
# i는 격자에 적을 숫자를 의미함
for i in range(2, n*n+1):
    nx, ny = x + dxs[d], y + dys[d]
    
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        d = (d+1)%4
        nx, ny = x + dxs[d], y + dys[d]
        
    x, y = nx, ny
    answer[x][y] = i
        
for i in range(n):
    for j in range(n):
        print(answer[i][j], end=" ")
    print()
'''

'''
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

n, m = map(int, input().split())

answer = [[0 for _ in range(m)] for _ in range(n)]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

x, y, d = 0, 0, 0
answer[x][y] = 1

for i in range(2, n*m+1):
    nx = x + dx[d]
    ny = y + dy[d]
    if not in_range(nx, ny) or answer[nx][ny] != 0:
        d = (d+1)%4
        nx = x + dx[d]
        ny = y + dy[d]

    x, y = nx, ny
    answer[x][y] = i

for aa in answer:
    for a in aa:
        print(a, end=' ')
    print()
'''

'''
mapper = {'W':0, 'S':1, 'N':2, 'E':3}
dx = [0, -1, 1, 0]
dy = [-1, 0, 0, 1]

x, y = 0, 0
time = 0

#N = int(input())
#for _ in range(N):
#    
#    dstr, cnt = input().split()
#    d = mapper[dstr]
#    cnt = int(cnt)
#    
#    for _ in range(cnt):
#        nx, ny = x+dx[d], y+dy[d]
#        if (nx, ny) == (0, 0):
#            print(time+1)
#            x,y = 0,0
#            break
#        else:
#            x, y = nx, ny
#            time += 1
#    if (x,y) == (0,0):
#        break
#else:
#    print(-1)


input_list = []
N = int(input())
for _ in range(N):
    dstr, cnt = input().split()
    input_list.append([mapper[dstr], int(cnt)])

#print(input_list)

for d, cnt in input_list:
    
    for _ in range(cnt):
        nx, ny = x + dx[d], y + dy[d]
        if (nx, ny) == (0, 0):
            x, y = 0, 0
            time += 1
            break
        else:
            x, y = nx, ny
            time += 1
    if (x,y) == (0,0):
        print(time)
        break
else:
    print(-1)
'''

'''
x, y = 0, 0
d = 0

mapper = {'L':-1, 'R':1, 'F': 0}
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

input_str = input()

time = 0
for s in input_str:
    nd = (d + mapper[s])%4
    if nd == d:
        x, y = x + dx[d], y + dy[d]
    else:
        d = nd
    time += 1
    if (x, y) == (0, 0):
        print(time)
        break
else:
    print(-1)
'''























