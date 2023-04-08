
# https://www.acmicpc.net/problem/14500

def show(l):
    for li in l:
        print(li)

N, M = map(int, input().split())

te_map = [ list(map(int, input().split())) for _ in range(N) ]
#print(N, M)
#show(te_map)

visited = [ [0 for _ in range(M)] for _ in range(N) ]

max_data = -1

# 상 하 좌 우
d = [(-1,0),(1,0),(0,-1),(0,1)]

def find_max_1(i, j, tsum, cnt):
    global max_data
    if cnt == 4:
        max_data = max(max_data, tsum)
        #show(visited)
        #print('\n')
        return
    
    for di in d:
        ni = i + di[0]
        nj = j + di[1]
        
        if ni>=0 and ni<N and nj>=0 and nj<M:
            if visited[ni][nj] == 0:
                visited[ni][nj] = 1
                find_max_1(ni,nj,tsum+te_map[ni][nj],cnt+1)
                visited[ni][nj] = 0
    
# 현재 좌표에서 3개 방향 값 더하기
def find_max_2(i, j):
    global max_data
    for cnt in range(4):
        tsum = te_map[i][j]
        for sum_i in range(3):
            # 012 123 230 301
            di = (cnt+sum_i)%4
            ni = i + d[di][0]
            nj = j + d[di][1]
            # 블록을 못만드는 경우
            if not (ni>=0 and ni<N and nj>=0 and nj<M):
                break
            tsum += te_map[ni][nj]
        else:
            max_data = max(max_data, tsum)



for i in range(N):
    for j in range(M):
        visited[i][j] = 1
        find_max_1(i, j, te_map[i][j], 1)
        visited[i][j] = 0
        
        find_max_2(i, j)
        
print(max_data)
