
# 상 하 좌 우
# (3-d)%4

dir_map = {'U':0, 'D':1, 'L':2, 'R':3}

def print_grid(grid):
    for g in grid:
        for gg in g:
            print(gg, end= ' ')
        print()
    print()


def in_range(x, y):
    return 0 <= x < n and 0 <= y < n


def move(x, y, d):
    dxs = [-1, 1, 0, 0]
    dys = [0, 0, -1, 1]
    
    nx, ny = x+dxs[d], y+dys[d]
    if in_range(nx, ny):
        return (nx, ny, d)
    else:
        # 방향을 바꾸는 작업에는 1초의 시간이 소요
        return (x, y, (5-d)%4)



def move_all(n, marbles):
    
    next_marbles = []
    next_marbles_cnt = [[0 for _ in range(n)] for _ in range(n)]
    
    print('move_all')
    print_grid(marbles)
    
    for r, c, d in marbles:
        nx, ny, nd = move(r, c, d)
        next_marbles.append((nx, ny, nd))
        next_marbles_cnt[nx][ny] += 1
    
    print('next_marbles')
    print_grid(next_marbles)
    
    marbles = []
    for r, c, d in next_marbles:
        if next_marbles_cnt[r][c] == 1:
            marbles.append((r,c,d))
            
    print('move_all end')
    print_grid(marbles)
    return marbles
    
              


# 아주 오랜시간이 흐른 후
def simulate(n, marbles, visited):
    
    while True:
        print('simulate')
        print(marbles)
        marble_cnt = len(marbles)
        
        if marble_cnt == 0 or marble_cnt == 1:
            print('end ??')
            return marbles
        
        # 해당 칸에 동일한 방향값을 가진 구슬이 n회 이상 방문했다면 break
        for r, c, d in marbles:
            visited[r][c][d] += 1
            print('??', r, c, d, visited[r][c][d])
            if visited[r][c][d] >= n:
                print('end end ??', r, c, d, visited[r][c][d])
                return marbles
                
        marbles = move_all(n, marbles)



T = int(input())
for _ in range(T):
    n, m = map(int, input().split())
    #grid = [[-1 for _ in range(n)] for _ in range(n)]
    marbles = []
    visited = [[[0 for _ in range(4)] for _ in range(n)] for _ in range(n)]
    
    for _ in range(m):
        r, c, cmd = input().split()
        r = int(r)-1
        c = int(c)-1
        d = dir_map[cmd]
        marbles.append((r, c, d))
        #grid[r][c] = d
    print(marbles)
        
    marbles = simulate(n, marbles, visited)
    
    
    print(len(marbles))


