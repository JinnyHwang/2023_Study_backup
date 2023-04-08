
'''
맨 처음 접했던 코테 문제ㅋㅋㅋㅋㅋㅋ
지금은 풀 수 있을 것인가?

 0 ≤ x ≤ 100, 0 ≤ y ≤ 100만 유효한 좌표

드래곤 커브의 개수 N
드래곤 커브의 정보는 네 정수 x, y, d, g
x와 y는 드래곤 커브의 시작 점, d는 시작 방향, g는 세대
(0 ≤ x, y ≤ 100, 0 ≤ d ≤ 3, 0 ≤ g ≤ 10)

방향 d 우상좌하
d = [(0,1),(-1,0),(0,-1),(1,0)]

'''
di = [(0,1),(-1,0),(0,-1),(1,0)]

N = int(input())

dragon = []
for _ in range(N):
    dragon.append( list(map(int, input().split())) )

connect = [ [] for _ in range(N) ]


# 드래곤 커브 돌렸을 때 생기는 선분들 저장
num = 0
# 0~100이니까 101개 필요함
arr = [ [0]*101 for _ in range(101) ]
for y, x, d, g in dragon:
    connect[num].append(d)
    for _ in range(g):
        # 그냥 reversed()로 받으면
        # list_reverseiterator object를 반환하기 때문에
        # list로 형변환 필요
        re = list(reversed(connect[num]))
        for r in re:
            connect[num].append((r+1)%4)
        
    print(connect)
    
    arr[y][x] = 1
    for c in connect[num]:
        #세대 수 만큼 반복
        nx = x + di[c][1]
        ny = y + di[c][0]
        if 0 <= nx <= 100 and 0 <= ny <= 100:
            arr[ny][nx] = 1
        print('nx,ny? ',nx,ny, ' arr? ',arr[nx][ny],'\n')
        
    num += 1

result = 0
# 정보를 보고 사각현 개수 세는 부분
# 우,하로 탐색하기 때문에 index 100번은 생략
for i in range(10):
    for j in range(10):
        #print(arr[i][j],arr[i+1][j] ,arr[i][j+1] ,arr[i+1][j+1] )
        if arr[i][j] and arr[i+1][j] and arr[i][j+1] and arr[i+1][j+1]:
            result += 1
            
print(result)











