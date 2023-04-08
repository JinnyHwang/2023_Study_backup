
N = int(input())
c = [list(map(int, input().split())) for _ in range(N)]
#print(c)

# 해당 강의를 선택했을 때 들을 수 있는 강의의 수 누적
get_c = list()
visited = [ 0 for _ in range(N)]
max_c = -1

def cal_get_class(get_c, index, visited):
    global max_c
    # 마지막까지 탐색이 끝나면 강의 개수 확인하고 end
    if index >= N:
        print('!!!', get_c)
        if max_c < len(get_c):
            max_c = len(get_c)
        return
    
    flag = 0
    #print(get_c, index)
    for gc in get_c:
        # c[index][0] / c[index][1]
        # s: gc[0] / e:gc[1]
        #print('??',index,get_c,gc, c[index])
        if gc[0] <= c[index][0] < gc[1] or gc[0] < c[index][1] <= gc[1]:
            flag = 1
    
    # 포함할 수 있으면 포함시키고 다음 강의 탐색
    if flag == 0 and visited[index] == 0:
        visited[index] = 1
        get_c.append(c[index])
        cal_get_class(get_c, index+1, visited)
    else:
        # 포함안시키고 다음 강의 탐색
        cal_get_class(get_c, index+1, visited)
    


for i in range(N):
    get_c = []
    visited = [ 0 for _ in range(N)]
    # 현재 강의 무조건 듣는가 가정
    get_c.append(c[i])
    visited[i] = 1
    #print('start!',get_c)
    cal_get_class(get_c, i+1, visited)

print(max_c)







