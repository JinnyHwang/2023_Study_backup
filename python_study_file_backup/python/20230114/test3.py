
cnt_min = 1e9
max_len = 0

# 문자열, 탐색index, min값
def num_cal(storey, si, cnt, edir):
    global cnt_min
    global max_len
    
    print('\n??', storey, si, cnt, edir)
    '''
    if si == 4:
        cnt_min = min(cnt_min, cnt)
        return
    '''
    
    if si == max_len:
        cnt += int(str(storey%(10**si))[0])
        print('last cnt? ', cnt)
        cnt_min = min(cnt_min, cnt)
        return
    
    curr_num = int(str(storey%(10**si))[0])
    
    storey -= curr_num*(10**(si-1))
    
    if edir == 0:
        # +방향
        storey += (10**si)
        num_cal( storey, si+1, cnt+(10-curr_num), 0)
        num_cal( storey, si+1, cnt+(10-curr_num), 1)
        print('(+) storey?', storey, ' si? ', si, ' curr_num? ', (10-curr_num))
    elif edir == 1:
        #-방향
        num_cal( storey, si+1, cnt+curr_num, 0)
        num_cal( storey, si+1, cnt+curr_num, 1)
        print('(-) storey?', storey, ' si? ', si, ' curr_num? ', curr_num)
        
    #print('!!', storey, si, cnt, edir)
    #num_cal( storey, si+1, cnt+curr_num, 0)
    #num_cal( storey, si+1, cnt+curr_num, 1)
    
    

def solution(storey):

    # 정수값 범위가 너무 넓다.. 완전탐색하면 바로 끝남
    # c는 0 ~ 8
    # 민수가 현재층에서 0층으로 가기 위해 최소한의 마법의 돌 개수는?
    # 값이 0보다 작으면 엘베 안움직인다 => 내려가기 위해서 나머지 자릿수를 0으로 만들어야함
    # 0으로 가는 경우의 수 중 min값 찾기
    
    global cnt_min
    global max_len
    
    #storey = 2554
    #storey = 16
    storey = 0
    
    storey_str = str(storey)
    max_len = len(str(storey))

    
    # 각 자리수에서 +방향 -방향 경우의 수를 확인
    # +방향인 경우에는 앞자리 +1
    num_cal(storey, 1, 0, 0)
    num_cal(storey, 1, 0, 1)
    print(cnt_min)


    answer = 0
    return answer

print(solution(0))
