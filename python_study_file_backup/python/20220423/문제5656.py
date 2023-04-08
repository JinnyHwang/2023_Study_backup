

# 시작점 (w,h)
def remove_brick(game, visited, visited_num, w, h, W, H):
        
        # range를 넘으면 break
        if w < 0 or w >= W or n < 0 or h >= H:
            return
        
        if visited[w][h] != 0:
            return
        
        # 방문 좌표 확인
        visited[w][h] = visited_num +1        
        num = game[w][h]
        
        #print('remove_brick w:{} h:{} visited[w][h]:{} num:{}'.format(w, h, visited[w][h], num) )
        
        if num == 0 or num == 1:
            return
        
        # 실제로 부순 벽돌 개수 확인
        #visited_num += 1
        #print('remove_brick visited_num:{}'.format(visited_num))
        
        for num_i in range(num):
            #print('remove_brick num_i:{} w+num_i:{} w-num_i:{} h+num_i:{}'.format(num_i, w+num_i, w-num_i, h+num_i))
            remove_brick(game, visited, visited[w][h], w+num_i, h, W, H)
            remove_brick(game, visited, visited[w][h], w-num_i, h, W, H)
            remove_brick(game, visited, visited[w][h], w, h+num_i, W, H)
                
                
def move_game(game, cnt_brick, W, H):
    # H-1 ~ 0 탐색
    for w in range(W):
        new_h = [ [0] for _ in range(H) ]
        cnt_h = H
        
        for h in range(H-1, -1, -1):
            if game[w][h] > 0:
                cnt_h -= 1
                cnt_brick += 1
                new_h[cnt_h] = game[w][h]
                
            # 값을 new_h에 복사하고 game[w]는 모두 0으로 초기화
            game[w][h] = 0
        
        # game[w]이 모두 0
        if cnt_h == H-1:
            continue
            
        for hh in range(cnt_h, H):
            game[w][hh] = new_h[hh]
            
        
    
T = int(input())

result = [ 0 for _ in range(T) ]

for t in range(T):
    
    N, W, H = map(int, input().split())
    #print(N, W, H)
    
    #game = [ [0]*W for _ in range(H)  ]
    game_input = [ list(map(int, input().split())) for _ in range(H) ]
    game = [ [0]*H for _ in range(W) ]
    
    for w in range(W):
        for h in range(H):
            game[h][w] = game_input[w][h]
            
    
    W, H = H, W
    
    for w in range(W):
        for h in range(H):
            print(game[w][h],end=' ')
        print('\n')
    
    print(game)
    
    for n in range(N):
        
        # 탐색 range 0 ~ W-1
        # 가장 많은 벽돌을 깼을 때
        # 각 회차에서 결과값
        # 없어질 벽돌 위치를 기억하자
        # -> 넓이 우선 탐색
        crash = [ [0]*W for _ in range(H) ]
        crash_num = 0
        
        print('n: ',n,'번째')
        
        # 넓이 우선 탐색을 가장 많이 실행한 회차 return
        # 벽돌 result 값이 아닌 넓이 우선 탐색 회차가 각장 큰것        
        for w in range(W):
            
            print('w: ',w,'번째')
            
            for h in range(H):
                print('game[w][h]: ', game[w][h])
                if game[w][h] != 0:
                    print('탐색할 h: ',h)
                    break
            else: # 탐색할 필요가 없는 w
                print('탐색할 h가 없음', h)
                continue
            
            visited = [ [0]*W for _ in range(H) ]
            visited_num = 0
            
            # visited를 채움
            remove_brick(game, visited, visited_num, w, h, W, H)
            
            #for w in range(W):
            #    for h in range(H):
            #        if game[w][h] == 1:
            #            visited_num += 1
            
            print('visited: ',visited_num, '\n',visited)
            
            if crash_num < visited_num:
                crash_num = visited_num
                crash = visited
            
            #print('crash: ',crash_num, '\n',crash)
                
                
        # game map 재구성
        for i in range(W):
            for j in range(H):
                if crash[i][j] == 1:
                    game[i][j] = 0
        
        # 한 칸씩 떨구기
        cnt_brick = 0
        move_game(game, cnt_brick, W, H)
        result[t] = cnt_brick
    

for i in range(T):
    print('#{} {}'.format(i+1, result[i]))










