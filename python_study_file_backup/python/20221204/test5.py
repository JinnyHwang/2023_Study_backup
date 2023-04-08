
# 강의가 끝나는 시간을 기준으로 sort:O(NlogN) + 강의 개수:O(N)
# 강의가 끝나는 시간을 기준으로 sort? 강의가 빨리 끝날수록 배정할 수 있는 강의 수 커짐
N = int(input())
c = [list(map(int, input().split())) for _ in range(N)]
#print(c)
c.sort(key = lambda x : (x[1], x[0]))
#print(c)

# 해당 강의를 선택했을 때 들을 수 있는 강의의 수 누적
get_c = list()
visited = [ 0 for _ in range(N)]
max_c = -1

def cal_get_class(get_c, index):
    global max_c
    if index >= N:
        #print("!!", get_c)
        if max_c < len(get_c):
            max_c = len(get_c)
        return
    
    flag = 0
    for gc in get_c:
        if c[index][0] < gc[1]:
            flag = 1
    
    if flag == 0 and visited[index]==0 :
        visited[index] = 1
        get_c.append(c[index])
        cal_get_class(get_c, index+1)
    else:
        cal_get_class(get_c, index+1)
        
           
get_c.append(c[0])
visited[0] = 1
cal_get_class(get_c, 1)

print(max_c)
