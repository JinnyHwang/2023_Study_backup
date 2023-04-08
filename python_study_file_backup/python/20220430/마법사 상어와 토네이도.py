
# 반시계
def rotate(arr):
    new_arr = []
    for a in zip(*arr):
        new_arr.append(list(a))
    new_arr.reverse()
    return new_arr

# N*N 격자: N은 홀수
N = int(input())

# magic_map[][]: 모래의 양
magic_map = [ list(map(int, input().split())) for _ in range(N) ]

# 격자의 가운데 좌표
start_pos = [ (N-1)//2, (N-1)//2 ]
cur_pos = [ (N-1)//2, (N-1)//2 ]

visited = [ [0]*N for _ in range(N) ]
#visited[(N-1)//2][(N-1)//2] = 1

d = 0
# 방향 좌, 하, 우, 상
di = [(0,-1),(1,0),(0,1),(-1,0)]

move_sand = [[0,0,0.02,0],[0,0.1,0.07,0.01],[0.05,-1,-2,-3],[0,0.1,0.07,0.01],[0,0,0.02,0]]
move_sand_pos = [[2,2], [1,2], [2,1], [2,2]]

#print('cur_pos: ',cur_pos)
#print('magic_map\n',magic_map,'\n')
    
result_sand = 0
while True:
    
    visited[cur_pos[0]][cur_pos[1]] = 1
    # 그렇게 도착한 지점이 0,0이면 탐색 끝!
    if cur_pos == [0,0]:
        break
    
    # 현재 방향에 따라 한 칸 이동
    nx  = cur_pos[0] + di[d][0]
    ny  = cur_pos[1] + di[d][1]
    
    # x,y => nx,ny로 이동함에 따라 모래 뿌리기
    # 범위값일 때 탐색
    # 아니면 다음 칸으로 이동
    if 0 <= nx < N and 0 <= ny < N:
        # 흩뿌릴 모래
        now_sand = magic_map[nx][ny]
        magic_map[nx][ny] = 0 # 모든모래 탈탈 털고 0값
        
        # 이동할 좌표에 모래가 있을 경우에만 흩뿌리기
        # 모래 없으면 다음 칸으로 이동
        if now_sand != 0:
            # move_sand 내에서 y좌표 move_sand_pos[d]
            # 현재 y의 좌표 [nx,ny]
            # move_sand의 좌표 + [msx, msy]는 magic_map에서 접근할 좌표. 
            msx = nx - move_sand_pos[d][0]
            msy = ny - move_sand_pos[d][1]
            
            remain_sand = now_sand
            for mi in range(len(move_sand)): # 행
                for mj in range(len(move_sand[0])): # 열
                    # magic_map의 mi+msx, mj+msy 값이랑 매칭
                    if move_sand[mi][mj] > 0:
                        ss = int(now_sand*move_sand[mi][mj])
                        
                        # move_sand의 좌표 + [msx, msy]는 magic_map에서 접근할 좌표.
                        if 0 <= mi+msx < N and 0 <= mj+msy < N:
                            magic_map[mi+msx][mj+msy] += ss
                        # magic_map 좌표를 벗어나면 result에 넣어준다
                        else:
                            result_sand += ss
                        # 날아간 모래만큼 빼주기
                        remain_sand -= ss
                        
            # a좌표에 들어갈 남은 모래 처리
            ax = nx+di[d][0]
            ay = ny+di[d][1]
            # a좌표가 범위 안이면 남은 모래 넣어줌
            if 0 <= ax < N and 0 <= ay < N:
                magic_map[ax][ay] += remain_sand
            # magic_map 좌표를 벗어나면 result에 넣어준다
            else:
                result_sand += remain_sand
        
    
    # 다음 턴에서 방향을 틀까? 말까?
    nd = (d+1)%4
    # 지금 방향에서 틀었을 때 좌표가 방문한 적 없으면 튼다
    if visited[nx+di[nd][0]][ny+di[nd][1]] != 1:
        d = nd
        # 모래 좌표도 같이 틀어줌
        move_sand = rotate(move_sand)
    
    # 이동이 끝났으니 current position 값 초기화
    cur_pos = [nx,ny]
    
    #print('cur_pos: ',cur_pos)
    #print('magic_map\n',magic_map,'\n')


print(result_sand)


#d = 0
# 방향 좌, 하, 우, 상
#di = [(0,-1),(1,0),(0,1),(-1,0)]

# 모래 재분배
# 맨 처음 d == 0 방향으로
# d가 바뀌면 반시계로 rotate 시켜줌
# move_sand[2][3]는 y: -3
# move_sand[2][2]이 기준점 y: -2
# move_sand[2][1]은 매번 변경해야하는 값 a: -1
#move_sand = [[0,0,0.02,0],[0,0.1,0.07,0.01],[0.05,-1,-2,-3],[0,0.1,0.07,0.01],[0,0,0.02,0]]
#move_sand_pos = [[2,2], [1,2], [2,1], [2,2]]
#print(move_sand)
#d += 1
#move_sand = rotate(move_sand)
#print(move_sand)
#print(move_sand_pos[d])
#d += 1
#move_sand = rotate(move_sand)
#print(move_sand)
#print(move_sand_pos[d])
#d += 1
#move_sand = rotate(move_sand)
#print(move_sand)
#print(move_sand_pos[d])



#print(move_sand_pos[0]+di[1][0], move_sand_pos[1]+di[1][1])
#print(magic_map)
#print(rotate(magic_map))


# 격자 밖으로 나간 모래의 양은?


#sand = magic_map[nx][ny]








