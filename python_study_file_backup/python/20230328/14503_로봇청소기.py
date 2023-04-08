
'''
N*M 행열
r,c 행열

반시계방향으로 90도
index -1씩

북동남서(시계방향)
d = [(-1,0),(0,1),(1,0),(0,-1)]
'''

# 4가지 방향 탐색, 회전 모두에 사용
d = [(-1,0),(0,1),(1,0),(0,-1)]

# 북 서 남 동
#d = [(-1,0),(0,-1),(1,0),(0,1)]

clean_cnt = 0
N, M = map(int, input().split())

# r,c는 항상 빈칸
r,c,di = map(int, input().split())

#  0: 청소안된빈칸 / 1:벽 / 가장자리는 모두 벽
# -1: 청소한칸
room = [ list(map(int, input().split())) for _ in range(N)]


direct = lambda di : di-1 if di>0 else 3

def clean_room(r,c,di):
    global clean_cnt
    
    # 방청소
    if room[r][c] == 0:
        clean_cnt += 1
        room[r][c] = -1
    
    # 주변칸확인
    for _ in range(4):
        # 4가지 방향 탐색. 반시계90도
        #print('11 di? ', di)
        di = direct(di)
        #print('22 di? ', di)
        nr, nc = r+d[di][0], c+d[di][1]
        if 0 <= nr < N and 0 <= nc < M:
            if room[nr][nc] == 0:
                return (nr,nc, di)
        
    # 4방향 모두 탐색. 청소할 칸이 없음
    dii = (di+2)%4 #후진
    nr,nc = r+d[dii][0], c+d[dii][1]
    if 0 <= nr < N and 0 <= nc < M and room[nr][nc] != 1:
        return (nr,nc, di)
    else: # 작동 멈춤
        return (r,c, di)
    
    
#print(N,M)
#print(r,c,di)

#for rr in room:
#    print(rr)


while(True):
    
    #print('1? ',r,c, di)
    nr, nc, di = clean_room(r,c, di)
    #print('2? ', nr,nc, di)
    
    if (r,c) == (nr,nc):
        break
    else:
        r,c = nr,nc
    
print(clean_cnt)










