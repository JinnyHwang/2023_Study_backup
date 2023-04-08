
'''
https://www.acmicpc.net/problem/23288




'''

from collections import deque 

def map_print(game):
    for g in game:
        print(g)
    print()


N, M, K = map(int, input().split())

game = []

for _ in range(N):
    game.append(list(map(int, input().split())))
#map_print(game)


#       y  x  z
dice = [1, 3, 5]
'''
# 주사위 굴리는 방향에 따라서
dice = [(7-x), y, z] # 동
dice = [x, (7-y), z] # 서
dice = [(7-z), y, x] # 남
dice = [z, y, (7-x)] # 북
'''
# 동 남 서 북 (시계)
d = [(0,1),(1,0),(0,-1),(-1,0)]

def roll_dice():
    if di == 0: # 동
        return [7-dice[1], dice[0], dice[2]]
    elif di == 1: # 남
        return [7-dice[2], dice[1], dice[0]]
    elif di == 2: # 서
        return [dice[1], 7-dice[0], dice[2]]
    elif di == 3: # 북
        return [dice[2], dice[1], 7-dice[0]]
        
def find_same(x,y,num):
    cnt = 0
    visit = [[0 for _ in range(M)] for _ in range(N)]
    q = deque()
    q.append((x,y))
    visit[x][y] = 1
    while(q):
        qx,qy = q.pop()
        cnt += 1
        #print('qx, qy, cnt?', qx, qy, cnt)
        for dx,dy in d:
            nx, ny = qx+dx, qy+dy
            if 0 <= nx < N and 0 <= ny < M and game[nx][ny] == num and visit[nx][ny] == 0:
                q.append((nx,ny))
                visit[nx][ny] = 1
    return cnt


di = 0
r,c = 0,0
score = 0

for _ in range(K):

    nr, nc = r+d[di][0], c+d[di][1]

    if (0 <= nr < N and 0 <= nc < M) == False:
        di = (di+2)%4
        nr, nc = r+d[di][0], c+d[di][1]
    #print('r,c, nr, nc, di? ',r,c, nr, nc, di)
    # 점수얻기
    # 주사위 굴리기
    #print('before dice? ', dice)
    dice = roll_dice()
    #print('after dice? ', dice)
    
    # 개수 count
    gnum = game[nr][nc]
    gcnt = find_same(nr,nc,gnum)
    score += (gnum*gcnt)
    #print(k,'turn score? ', score)

    # 이동방향 정하기
    dice_num = 7-dice[0]
    
    # 이동방향 전환
    if dice_num > gnum:
        di = (di+1)%4
    elif dice_num < gnum:
        di = (di-1)%4
    
    r,c = nr,nc
    #print('dice_num, gnum, di? ', dice_num, gnum, di)

print(score)



