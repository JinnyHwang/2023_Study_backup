'''
행열의 끝에서 끝까지 갈 수 있는가?

경사로를 놓으면 1단차를 줄일 수 있다
경사로를 놓을 때 주의해야하는 점
1. 가로세로
2. 방향


1. 경사로가 놓였는지 표기, 뱡향도 중요
=> 길 체크할 때 1단차가 있는데, 경사로가 있으면 이어지는거로
=> 경사로가 좌->우 or 상->하 방향이면 1
=> 경사로가 우->좌 or 하->상 방향이면 -1



'''

N, L = map(int, input().split())

road = []
for _ in range(N):
    road.append(list(map(int, input().split())))
    
#print(road)

slide_col = [[0 for _ in range(N)] for _ in range(N)]
slide_row = [[0 for _ in range(N)] for _ in range(N)]
#print(slide_col) #가로
#print(slide_row) #세로


# 가로세로길체크
cnt_col = 0
for i in range(N):
    #print('i? ', i)
    for j in range(N-1):
        
        # 경사 맨 마지막은 탐색 과정 거친다
        if slide_col[i][j] != 0 and slide_col[i][j+1] != 0:
            #print('slide_col[i][j]? ', slide_col[i][j])
            if j == N-2:
                #print('endend!!')
                cnt_col += 1
            continue
        
        # 가로 road[i][j]
        if road[i][j] != road[i][j+1]: #평지
            #print('평지')
            #continue
            if abs(road[i][j] - road[i][j+1]) == 1: #1단차
                # 경사로 놓을 수 있는지 확인
                # 값이 더 큰 쪽에서 작은 쪽으로 방향 확인
                # 낮은 블록 개수가 L길이만큼 연속적인가?
                # 이미 블록이 쌓여있지는 않은가?
                if road[i][j] > road[i][j+1]: #1방향
                    if j+1+L <= N and slide_col[i][j+1 : j+1+L] == [0 for _ in range(L)] and road[i][j+1 : j+1+L] == [ road[i][j+1] for _ in range(L)]:
                        #print('road[i][j+1 : j+1+L]? ', road[i][j+1 : j+1+L])
                        slide_col[i][j+1:j+1+L] = [1 for _ in range(L)]
                        #print('slide_col[i]? ', slide_col[i])
                    else:
                        #print('1 out!!')
                        #if j+1+L <= N:
                            #print('j+1? ', j+1, '  j+1+L? ', j+1+L, 'road[i][j+1 : j+1+L]? ', road[i][j+1 : j+1+L])
                        slide_col[i] = [0 for _ in range(N)]
                        break
                else: #-1방향
                    if j-L+1 >= 0 and slide_col[i][j-L+1:j+1] == [0 for _ in range(L)] and road[i][j-L+1:j+1] == [road[i][j] for _ in range(L)]:
                        #print('road[i][j-L+1:j+1]? ', road[i][j-L+1:j+1])
                        slide_col[i][j-L+1:j+1] = [-1 for _ in range(L)]
                        #print('slide_col[i]? ', slide_col[i])
                    else:
                        #print('-1 out!!')
                        #if j-L >= 0:
                            #print('j-L+1? ', j-L+1, '  j+1? ', j+1, '  road[i][j-L+1:j+1]? ', road[i][j-L+1:j+1])
                        slide_col[i] = [0 for _ in range(N)]
                        break
                
                # 맨끝까지 탐색을 완료하면 slide_col값 유지, count+1  
                # 경사를 쌓을 수 없으면 break
                # 쌓았던 경사 초기화 slide_col
            else:
                slide_col[i] = [0 for _ in range(N)]
                break
        
        if j == N-2:
            #print('end!!')
            cnt_col += 1

#for s in slide_col:
    #print(s)
#print(cnt_col)
        
def silde_init_row(i):
    for n in range(N):
        slide_row[n][i] = 0

def check_row(a,b,i, value):
    for n in range(a,b):
        if slide_row[n][i] == 0 and road[n][i] == value:
            continue
        else:
            return False
    return True

def input_row(a,b,i,value):
    for n in range(a,b):
        slide_row[n][i] = value
        #print(slide_row[n][i], end=' ')
    #print('\n')

def print_row(a,b,i):
    print('[',end=' ')
    for n in range(a,b):
        print(road[n][i], end=' ')
    print(']')

#print('\n row start!')
cnt_row = 0
for i in range(N):
    for j in range(N-1):
        # 세로 road[j][i]
        
        if road[j][i] != road[j+1][i]:
            #print('평지')
            if abs(road[j][i] - road[j+1][i]) == 1:
                if road[j][i] > road[j+1][i]: #1방향
                    if j+1+L <= N and check_row(j+1, j+1+L, i, road[j+1][i]):
                        #print_row(j+1, j+1+L,i)
                        #print('road[j+1 : j+1+L][i]? ', road[j+1 : j+1+L][i])
                        input_row(j+1, j+1+L, i, 1)
                    else:
                        #print('1 out!!')
                        #if j+1+L <= N:
                            #print('j+1? ', j+1, '  j+1+L? ', j+1+L, 'road[j+1 : j+1+L][i]? ', road[j+1 : j+1+L][i])
                            #print('j+1? ', j+1, '  j+1+L? ', j+1+L, end=' ')
                            #print_row(j+1, j+1+L,i)
                        silde_init_row(i)
                        break
                        
                else: #-1방향
                    if j-L+1 >= 0 and check_row(j-L+1, j+1, i, road[j-L+1][i]):
                        #print_row(j-L+1, j+1,i)
                        #print('road[j-L+1:j+1][i]? ', road[j-L+1:j+1][i])
                        input_row(j-L+1, j+1, i, -1)
                    else:
                        #print('-1 out!!')
                        #if j-L >= 0:
                            #print('j-L+1? ', j-L+1, '  j+1? ', j+1, '  road[j-L+1:j+1][i]? ', road[j-L+1:j+1][i])
                            #print('j-L+1? ', j-L+1, '  j+1? ', j+1, end=' ')
                            #print_row(j-L+1, j+1,i)
                        silde_init_row(i)
                        break
            else:
                silde_init_row(i)
                break
        
        if j == N-2:
            #print('end!!')
            cnt_row += 1

#for s in slide_row:
    #print(s)
#print(cnt_row)

print(cnt_col+cnt_row)

# 가로, 세로 탐색 시 경사 겹치는 위치 있는가?
# 


# 경사로 놓기



