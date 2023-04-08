
'''
(r, c)는 격자의 r행 c열에 있는 바구니를 의미하고,
A[r][c]는 (r, c)에 있는 바구니에 저장되어 있는 물의 양을 의미한다.
바구니에 저장할 수 있는 물의 양에는 제한이 없다

맵은 이어져있다
nx = (x + di[0])//N
ny = (y + di[1])//N

비구름 위치: (N, 1), (N, 2), (N-1, 1), (N-1, 2)

1. 모든 구름이 di 방향으로 si칸 이동한다.
2. 각 구름에서 비가 내려 구름이 있는 칸의 바구니에 저장된 물의 양이 1 증가한다.
3. 구름이 모두 사라진다.

4. 2에서 물이 증가한 칸 (r, c)에 물복사버그 마법을 시전한다. 물복사버그 마법을 사용하면,
대각선 방향으로 거리가 1인 칸에 물이 있는 바구니의 수만큼
(r, c)에 있는 바구니의 물이 양이 증가한다.
=> 대각선 d[1], d[3], d[5], d[7] 좌표로 물바구니 개수 확인
=> 바구니 개수 만큼 (r, c) 물이 늘어남
(+) 이때는 이동과 다르게 경계를 넘어가는 칸은 대각선 방향으로 거리가 1인 칸이 아니다.
예를 들어, (N, 2)에서 인접한 대각선 칸은 (N-1, 1), (N-1, 3)이고,
(N, N)에서 인접한 대각선 칸은 (N-1, N-1)뿐이다.
==> nx = x + di[0] / ny = y + di[1] : 0 <= nx, ny < N 확인하기

5. 바구니에 저장된 물의 양이 2 이상인 모든 칸에 구름이 생기고, 물의 양이 2 줄어든다.
이때 구름이 생기는 칸은 3에서 구름이 사라진 칸이 아니어야 한다.
=> 구름이 사라진 칸에는 다시 생길 수 없고
=> 이전 turn에서 구름이 없었던 칸에만 생김

결과값
M번의 이동이 모두 끝난 후 바구니에 들어있는 물의 양의 합을 구해보자.
'''

from copy import deepcopy

# 방향 순서 ←, ↖, ↑, ↗, →, ↘, ↓, ↙ 0~7 (1~8)
di = [(0,-1),(-1,-1),(-1,0),(-1,1),(0,1),(1,1),(1,0),(1,-1)]

N, M = map(int, input().split())

# N*N map
magic_map = [ list(map(int, input().split())) for _ in range(N) ]

# 시도 횟수 M
magic_try = [ list(map(int, input().split())) for _ in range(M) ]

#print('N, M: ', N, M)
#print('magic_map\n', magic_map)
#print('magic_try\n', magic_try)

# 구름 정보를 담고 있는 리스트
# 초기 값은 (N, 1), (N, 2), (N-1, 1), (N-1, 2)
cloud_info = [[N-1,0],[N-2,0],[N-1,1],[N-2,1]]
new_cloud_info = []

for d,s in magic_try:
    
    # 구름 이동
    #print('1 cloud_info: ',cloud_info)
    for i, v in enumerate(cloud_info):
        nx = (v[0] + di[d-1][0]*s)%N
        ny = (v[1] + di[d-1][1]*s)%N
        cloud_info[i] = [nx,ny]
    #print('2 cloud_info: ',cloud_info)

    # 비 내리기(물 양 증가)
    #print('1 magic_map: ', magic_map)
    for x,y in cloud_info:
        #print('cloud_info x,y',x,y,'   magic_map[x][y]: ',magic_map[x][y])
        magic_map[x][y] += 1
    
    # 물복사
    visited = [ [0]*N for _ in range(N) ]
    for x,y in cloud_info:
        visited[x][y] = 1
        cnt = 0
        for i in range(1,8,2):
            nx = x + di[i][0]
            ny = y + di[i][1]
            if 0 <= nx < N and 0 <= ny < N:
                if magic_map[nx][ny] > 0:
                    cnt += 1
                    #print('i? ',i,'  nx,ny? ',nx,ny,'  cnt? ', cnt)
                
        magic_map[x][y] += cnt
        #print('x,y? ',x,y,'  magic_map[x][y]? ',magic_map[x][y])
    #print('2 magic_map: ', magic_map)
        

    # 구름 생성 후 물 양 감소, 기존 구름 삭제
    for x in range(N):
        for y in range(N):
            if magic_map[x][y] >= 2 and visited[x][y] == 0:
                #if not [x,y] in cloud_info:
                new_cloud_info.append([x,y])
                magic_map[x][y] -= 2
                    
    cloud_info = deepcopy(new_cloud_info)
    new_cloud_info = []

# M번 반복 끝난 후 물의 양 확인
result = 0
for m in magic_map:
    result += sum(m)
    
print(result)
