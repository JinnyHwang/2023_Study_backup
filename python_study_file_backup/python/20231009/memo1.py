
# 세로줄: 2 <= n <= 11
# 가로줄: 1 <= m <= 15
# 가로줄을 모두 사용했을 때 결과와 동일한 결과를 얻을 수 있는 최소한의 가로줄 수는?

MAX_M = 15
n, m = tuple(map(int, input().split()))
m_list = []
for _ in range(m):
    m_list.append(list(map(int, input().split())))
#print(m_list)

sub_m_list = []
max_result = []
grid = []
ans = m+1


def in_range(index):
    return 1 <= index and index <= n


# 사다리를 타고 결과를 확인하는 function
def check_result():
    result = [ 0 for _ in range(n)]
    for i in range(1,n+1):
        ans_num = i
        
        for mi in range(1,MAX_M+1):
            if grid[ans_num][mi]:
                ans_num = grid[ans_num][mi]
                '''
                print('ans_num, mi? ',ans_num, mi)
                # 좌우 확인
                if in_range(ans_num-1) and grid[ans_num-1][mi] == 1:
                    ans_num = ans_num-1
                    print('1 new ans_num?', ans_num)
                    continue
                
                if in_range(ans_num+1) and grid[ans_num+1][mi] == 1:
                    ans_num = ans_num+1
                    print('2 new ans_num?', ans_num)
                    continue
                '''
        
        result[i-1] = ans_num
        
    return result


# 주어진 선으로 사다리를 그리는 function
# n을 key, m을 value로 해서 오른쪽으로 가는지 왼쪽으로 가는지 확인
# dictionary... 불편해!
#def draw_ladder1():
#    global dic_ladder
#    dic_ladder = {}
#    for k, v in sub_m_list:
#        dic[k] = dic.get(k,[]) + [v]
#    
#    #for k,v in dic_ladder.items():
#    #for k in dic_ladder.keys():
#    #for v in dic_ladder.values():
#    # value가 오름차순으로 정렬됨
#    for k in dic_ladder.keys():
#        dic_ladder[k].sort()

    
def draw_ladder(ladder_list):
    global grid
    grid = [[0 for _ in range(MAX_M+1)] for _ in range(n+1)]
    for sn,sm in ladder_list:
        grid[sn][sm] = sn+1
        grid[sn+1][sm] = sn
        #print(sn,sm, grid)
    
    

# list 조합을 만드는 funtion
def make_list(cnt):
    global ans
    
    if cnt == m:
        # sub_m_list 안 data로 사다리 그리기
        #print()
        #print(sub_m_list)
        #print('1 : ',grid)
        draw_ladder(sub_m_list)
        #print('2 : ',grid)
        #sub_m_list_result = check_result()
        #print('3: ', sub_m_list_result)
        #print()
        # 사다리 결과 값이 일치하는지 확인
        if check_result() == max_result:
            ans = min(ans,len(sub_m_list))
        return
    
    sub_m_list.append(m_list[cnt])
    make_list(cnt+1)
    sub_m_list.pop()
    
    make_list(cnt+1)
    
       
#print('1 : ',grid)
draw_ladder(m_list)
#print('2 : ',grid)
max_result = check_result()
#print(max_result)

if max_result == [i for i in range(1,n+1)]:
    print(0)
else:
    make_list(0)
    print(ans)











