'''
상하좌우
#dx = [0, 0, -1, 1]
#dy = [-1, 1, 0, 0]


체스판게임

크기 N*N

N, K = map(int, input().split())
0은 흰색, 1은 빨간색, 2는 파란색
game = [ list(map(int, input().split())) for _ in range(N) ]
game_info = [ []*N for _ in range(N) ]


0 ~ K-1 말
horse = [ list(map(int, input().split())) for _ in range(K) ]



game[y][x]
가려는 칸 색깔
흰색 0 : 이동. 해당 칸에 있는 말 가장 위에 쌓음
빨강 1 : 이동. 이동하는 말이 쌓인 순서를 역순으로 reverse [n1:n2:-1] n1부터 n2-1까지 역순으로 바꾼 다음에 쌓음
파랑 2 , 체스판 경계선 : 이동 안함. 방향을 바꿔서 이동. 만약 가려는 곳이 파랑 또는 막힌곳이면 이동 안함.


이동방향
방향 인덱스 값 i는 0,1
(i+1)%2
상하  da = [(0,-1),(0,1)]
좌우  db = [(-1,0), (1,0)]
==> 패쓰



dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]


말 개수 k개


필요한 정보
1. 말 순서 : 말 리스트의 순서
2. 말의 위치, 방향
3. 각 칸에 쌓여있는 말 : game_info list 정보 저장 추가는 append 맨 끝에 추가
삭제 방법 append, remove(value) or pop(index) or del[aindex:bindex] or clear()모두삭제
'''

'''
1. 말 정보 확인
y,x,d = horse[i]

ny = y + dy[d-1]
nx = x + dx[d-1]
nd = d



가야할 체스판 색깔 확인
만약 파란색이거나 벽이면 방향바꾸기
방향 바꾸기
if d == 1 or 3 return nd += 1
else d == 2 or 4 return nd-= 1

확정방향
파란색이나 벽이면 이동 없음 동작 끝


빨간색
game_info 확인, 역순으로 list에 저장
l = game_info[y][x][horse.index(k)::-1]

흰색
game_info 확인, list에 저장
l = game_info[y][x][horse.index(k):]

game_info[y][x].del[horse.index(k):]
game_info[ny][nx].extend(l)

if len(game_info[ny][nx]) >= 4 end

hores[i] = [ny, nx, nd]


그 값이 1,000보다 크거나
turn count 횟수 > 1000
or
절대로 게임이 종료되지 않는 경우...???
'''


# https://www.acmicpc.net/problem/17837

N, K = map(int, input().split())

game_map = [ list(map(int, input().split())) for _ in range(N) ]
print('game_map\n', game_map)

'''
game_info = [ [[]]*N for _ in range(N) ]
이렇게 만들 경우 내부적으로 포함된 N개 리스트가
모두 동일 객체에 대한 N개의 레퍼런스로 인식함!
game_info[n][0], game_info[n][1], game_info[n][2], game_info[n][3] 모두 똑같은 객체
game_info
 [[[], [], [], []], [[0, 2], [0, 2], [0, 2], [0, 2]], [[1], [1], [1], [1]], [[3], [3], [3], [3]]]
'''

# 컴프리헨션 사용!
game_info = [ [[] for _ in range(N)] for _ in range(N) ]


        
print('game_info\n', game_info)

horse = []
for i in range(K):
    #horse.append(list(map(int, input().split())))
    y,x,d = map(int, input().split())
    horse.append( [y-1,x-1,d-1] )
    
print('horse\n', horse)


for i, h in enumerate(horse):
    game_info[h[0]][h[1]].append(i)
    #print('i: ', i, '\n y, x', h[0]-1, h[1]-1)
    #print('[1] game_info\n',game_info)
    #print('[1] game_info[y][x]\n',game_info[h[0]-1][h[1]-1])
    #game_info[h[0]-1][h[1]-1].append(i)
    #horse[i] = [h[0]-1, h[1]-1, h[2]-1]
    #print('[2] game_info\n',game_info)
    #print('[2] game_info[y][x]\n',game_info[h[0]-1][h[1]-1])

print('game_info\n', game_info)

























