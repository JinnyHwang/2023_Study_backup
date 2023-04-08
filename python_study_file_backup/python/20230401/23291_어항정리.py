
# https://www.acmicpc.net/problem/23291

N, K = map(int, input().split())
port = list(map(int, input().split()))

port_map = [[0 for _ in range(N)] for _ in range(N/2)]
port_map2 = [[0 for _ in range(N/2)] for _ in range(N/2)]

cnt = 0
while(True):
    
    cnt += 1

    # 물고기 추가
    min_fish = min(port)
    for n in range(N):
        if port[n] == min_fish:
            port[n] += 1


    # 어항 쌓기
    #port_map = [[0 for _ in range(N)] for _ in range(N/2)]
    port_map[N/2-1] = port # 맨 아래줄에 물고기 넣기


    # 인접어항 물고기 비교해서 재분배
    d = [(0,1),(0,-1),(-1,0),(1,0)] # 동 서 남 북
    port_map_cal = [[0 for _ in range(N)] for _ in range(N/2)]
    for i in range(N/2):
        for j in range(N):
            port_map[i][j] != 0:
                for di in d:
                    ni = i+di[0]
                    nj = j+di[1]
                    if 0 <= ni < N/2 and 0 <= nj < N and port_map[ni][nj] > 0:
                        mok = abs(port_map[i][j] - port_map[ni][nj])//5
                        if mok > 0:
                            if port_map[i][j] > port_map[ni][nj]:
                                port_map_cal[i][j] -= mok
                                port_map_cal[ni][nj] += mok
                            else:
                                port_map_cal[i][j] += mok
                                port_map_cal[ni][nj] -= mok
                                
    for i in range(N/2):
        for j in range(N):
            if port_map[i][j] != 0:
                port_map[i][j] += port_map_cal[i][j]
                                
            

    # 어항 해체
    # 열을 고정 행을 N-1부터 0까지 확인해서 재배열
    pi = 0
    for j in range(N):
        for i in range(N/2-1, 0, -1):
            if port_map[i][j] > 0:
                port[pi] = port_map[i][j]
                pi += 1
                port_map[i][j] = 0
            else: # 0을 만나면 바로 다음 열로
                break


    # 어항 접기1
    #port_map2 = [[0 for _ in range(N/2)] for _ in range(N/2)]


    # 어항 접기2


    # 어항 해체: 위랑 규칙 똑같음
    pi = 0
    for j in range(N/2, N/4):
        for i in range(N/2):
            port[pi] = port_map2[i][j]
            pi += 1
            port_map2[i][j] = 0
            
            
    # 어항 정리 끝 확인
    if max(port) - min(port) < K:
        break


print(cnt)



