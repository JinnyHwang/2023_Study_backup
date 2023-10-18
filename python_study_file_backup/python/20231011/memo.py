
# n개 점 중 m개 선택 : 조합만들기
# 선택한 점 중 거리가 가장 먼 것의 값을 저장
# 결과에는 조합 return값중 최솟값을 저장, return

n, m = tuple(map(int, input().split()))
dot_list = []
for _ in range(n):
    i,j = map(int, input().split())
    dot_list.append((i,j))


# 길이 m
combi = []

def cal_dist(dot1,dot2):
    (x1,y1),(x2,y2) = dot1,dot2
    return (x1-x2)**2 + (y1-y2)**2

#print(cal_dist((1,3),(1,1)))
#print(cal_dist((4,4),(1,1)))
#print(cal_dist((4,4),(3,5)))

def cal_max_dist():
    max_dist = 0
    
    # dot_list에서 2개를 선택해서 만들 수 있는 모든 조합
    for i in range(m-1):
        for j in range(i+1,m):
            curr_dist = cal_dist(combi[i],combi[j])
            max_dist = max(max_dist,curr_dist)

    return max_dist


def calc():
    return max([cal_dist(combi[i],combi[j]) for i in range(m-1) for j in range(i+1,m)])



min_combi = 1e9
def make_combi(idx, cnt):
    global min_combi
    
    if cnt == m:
        #print(combi, cal_max_dist())
        #min_combi = min(min_combi, cal_max_dist())
        min_combi = min(min_combi, calc())
        return
    
    if idx == n:
        return
    
    # idx dot 포함
    combi.append(dot_list[idx])
    make_combi(idx+1, cnt+1)
    combi.pop()
    
    # idx dot 미포함
    make_combi(idx+1, cnt)
    
    
make_combi(0,0)  
print(min_combi)  
    
    
    
    
    


