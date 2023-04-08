
dy = [0, 0, -1, 1]
dx = [1, -1, 0, 0]

N, K = map(int, input().split())

game_map = [ list(map(int, input().split())) for _ in range(N) ]

game_info = [ [[] for _ in range(N)] for _ in range(N) ]

horse = []
for i in range(K):
    y,x,d = map(int, input().split())
    horse.append( [y-1,x-1,d-1] )
    
for i, h in enumerate(horse):
    game_info[h[0]][h[1]].append(i)
    
    
cnt = 0
answer = -1

while(answer != cnt):
    
    cnt += 1
    if cnt > 1000:
        answer = -1
        break
    
    # 말 하나씩 순서대로 탐색
    for i, h in enumerate(horse):
        
        # 초기화
        horse_list = []
        hi = 0
        hl = []
        empty = []
        
        # 현재 말의 위치
        y = h[0]
        x = h[1]
        d = h[2]
        
        ny = y + dy[d]
        nx = x + dx[d]
                
        # 범위 밖이면 방향 변경
        if ny < 0 or ny > N-1 or nx < 0 or nx > N-1:
            if d == 0 or d == 2:
                d += 1
            elif d == 1 or d== 3:
                d -= 1
            ny = y + dy[d]
            nx = x + dx[d]
            
        # 범위 안벗어날 때 color 확인
        else:
            # 다음에 갈 체스판 색깔
            color = game_map[ny][nx]
            
            # 파란색  : 방향 변경
            if color == 2:
                if d == 0 or d == 2:
                    d += 1
                elif d == 1 or d== 3:
                    d -= 1
                ny = y + dy[d]
                nx = x + dx[d]
                
        # ny, nx range 확인
        # 가야할 체스판 색깔 확인
        # 진짜로 말을 옮길 차례
        
        # 이동 안함 : 가야하는 칸이 막다른 길
        if ny < 0 or ny > N-1 or nx < 0 or nx > N-1 :
            horse[i] = [y, x, d]
            continue
        # 이동 안함 : 파란색
        elif game_map[ny][nx] == 2:
            horse[i] = [y, x, d]
            continue
        
        # 이동
        else:
            color = game_map[ny][nx]
            hl = game_info[y][x]
            
            # 현재 말의 인덱스 확인
            hi = hl.index(i)
            
            #-------------------------------------------------------------------#
            # 빨간색 : 옮겨야 하는 말 순서 reverse
            if color == 1:
                if hi == 0:
                    horse_list = hl[::-1]
                else:
                    horse_list = hl[:hi-1:-1]
                
            # 흰색
            else:
                horse_list = hl[hi:]
            #-------------------------------------------------------------------#
                
            #남아있는 말 처리
            if hi == 0:
                game_info[y][x] = []
            else:
                game_info[y][x] = hl[:hi]
                
         # 이동
        game_info[ny][nx].extend(horse_list)
        
        if len(game_info[ny][nx]) >= 4:
            answer = cnt
            break
        
        # 옮긴 말 좌표 모두 바꿔주기
        if len(horse_list) > 1:
            for hh in horse_list:
                horse[hh][0:2] = [ny, nx]
            
        horse[i] = [ny, nx, d]
        
        
print(answer)
  