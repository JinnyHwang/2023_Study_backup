
N, M, C = tuple(map(int, input().split()))
stuff_grid = [ list(map(int, input().split())) for _ in range(N) ]
max_value_save = [[-1 for _ in range(N)] for _ in range(N)]

# 도둑1, 도둑2의 겹치지 않는 시작 좌표 정하기
# sx1, sy1 sx2, sy2

# 두 좌표가 주어졌을 때 영역이 겹치지 않는가? 어떻게 판별?
# overlap이면 False return
def overlap_check(sx1, sy1, sx2, sy2):
    
    # end position은?
    end_sy1 = sy1+M-1
    end_sy2 = sy2+M-1
    # end position이 격자를 벗어나면 안됨
    if end_sy1 >= N or end_sy2 >= N:
        return False
    
    # sx1, sx2 다름 괜춘
    if sx1 != sx2:
        return True
    
    # sy1 ~ end_sy1 과 sy2 ~ end_sy2가 겹치는지 확인
    return (sy2 > end_sy1 or sy1 > end_sy2)


# list의 길이가 M이므로 최대 M번 확인
def find_max_value(cnt, w, value):
    global range_list_amx_value
    
    if cnt == M:
        if w <= C:
            range_list_amx_value = max(range_list_amx_value, value)
        return
    
    # range_list[cnt] 선택
    find_max_value(cnt+1, w+range_list[cnt], value+(range_list[cnt]*range_list[cnt]))
    
    # range_list[cnt] 선택 안함
    find_max_value(cnt+1, w, value)
    
    


range_list = []
range_list_amx_value = 0
def find_max(sx, sy):
    global range_list, range_list_amx_value
    range_list = []
    range_list_amx_value = 0
    
    if max_value_save[sx][sy] != -1:
        return max_value_save[sx][sy]
    
    range_list = stuff_grid[sx][sy:sy+M]
    
    # range_list에서 만들 수 있는 가장 큰 value 찾기
    find_max_value(0,0,0)
    max_value_save[sx][sy] = range_list_amx_value
    
    return range_list_amx_value
    
    


ans = 0
#  sx1, sy1 sx2, sy2 모든 경우의 수 확인
for sx1 in range(N):
    for sy1 in range(N):
        for sx2 in range(N):
            for sy2 in range(N):
                if overlap_check(sx1, sy1, sx2, sy2):
                    #print('sx1, sy1, sx2, sy2? ', sx1, sy1, sx2, sy2)
                    ans = max(ans, find_max(sx1, sy1)+find_max(sx2, sy2))
                    
'''                    
ans = max([find_max(sx1, sy1)+find_max(sx2, sy2)
           for sx1 in range(N)
           for sy1 in range(N)
           for sx2 in range(N)
           for sy2 in range(N)
           if overlap_check(sx1, sy1, sx2, sy2)
           ])
'''
print(ans)


