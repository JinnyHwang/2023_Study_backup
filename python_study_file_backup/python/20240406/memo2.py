
# N개의 줄
# 거울 모양 \ /
# N, E, S, W  북, 동, 남, 서
# \ 는 NW 북서 , ES 동남
# / 는 SW 남서 , EN 동북
# 레이저의 방향 값을 보고 거울에 따라 전환해줘야함

# S, W, N, E
dxs = [1, 0, -1, 0]
dys = [0, -1, 0, 1]
#dxs = [0, -1, 0, 1]
#dys = [1, 0, -1, 0]
# \ 12 03 합이 3 : -3
#1-3 -2 2
#2-3 -1 1
#0-3 -3 3
#3-3 0 0

# / 01 23 합이 5 : -5
#0-5 -5 5%4
#1-5 -4 4
#2-5 -3 3
#3-5 -2 2

# 레이저를 쏘는 위치 숫자로 주어짐

mapper = {'/':-5, '\\':-3}

N = int(input())
grid = [[0 for _ in range(N)] for _ in range(N)]
#print(grid)

for i in range(N):
    s = input()
    for j in range(N):
        grid[i][j] = mapper[s[j]]

#print(grid)

# k 값으로 시작위치와 방향 값 구함
k = int(input())
k = k-1
#print(k)

mok = k//N
na = k%N
#print(mok, na)
d = mok

if mok == 0:
    x = 0
    y = na
elif mok == 1:
    x = na
    y = N-1
elif mok == 2:
    x = N-1
    y = (na-(N-1))*(-1)
elif mok == 3:
    x = (na-(N-1))*(-1)
    y = 0



def in_range(x,y):
    return 0 <= x < N and 0 <= y < N

cnt = 0
while(True):
    #print('cnt: ',cnt, 'd, x, y: ', d, x, y)
    cnt += 1
    nd = ((d+grid[x][y])*(-1))%4
    nx, ny = x + dxs[nd], y + dys[nd]
    #print('cal?: ',grid[x][y], 'nd, nx, ny: ', nd, nx, ny)
    
    if not in_range(nx, ny):
        #print('end: ', nd, nx, ny)
        break
    
    d, x, y = nd, nx, ny
    
print(cnt)





'''
# k 값으로 시작위치와 방향 값 구함
k = int(input())
print(k)

mok = k//N
na = k%N
print(mok, na)
d = mok

if mok == 0 or mok == 2:
    x = mok
    y = (na+(N-1))%N
elif mok == 1 or mok == 3:
    x= (na+(N-1))%N
    y = N-mok

print(d, x, y)

#nd = (d+grid[r][c])%4



for _ in range(N*4):
        
    # k 값으로 시작위치와 방향 값 구함
    k = int(input())
    k = k-1
    #print(k)

    mok = k//N
    na = k%N
    print(mok, na)
    d = mok

    if mok == 0:
        x = mok
        y = na
    elif mok == 1:
        x = na
        y = N-mok
    elif mok == 2:
        x = mok
        y = (na-(N-1))*(-1)
    elif mok == 3:
        x = (na-(N-1))*(-1)
        y = N-mok

    print(d, x, y)
'''






