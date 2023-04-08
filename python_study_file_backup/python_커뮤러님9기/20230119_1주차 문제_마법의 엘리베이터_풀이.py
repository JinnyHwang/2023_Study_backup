'''
처음에 이 문제를 해결하려 했을 때
주어진 자리수를 신경쓰면서 재귀를 진행함

2554가 2560? or 2550?
2550이 2600? or 2500? / 2560이 2600? or 2500?
위와 같은 방법으로 자리수를 신경쓰면서 버튼 누르기를 진행

그러나 해설에서 말한 것처럼
 
2554가 256 or 255
255가 25 or 26
이렇게 count만 하는 용도이기 때문에 자릿수를 신경쓰지 않아도 됨!

//10 => 다음에 탐색할 값 구하기
%10 => count할 횟수 구하기

'''
min_cnt = 1e9
def cal_storey_min(storey, total_cnt): # 해설만 보고 직접 세운 code. 통과!
    global min_cnt
    #print('!! {}  {}'.format(storey, total_cnt))
    
    if storey == 0 or storey == 1:
        min_cnt = min(total_cnt+storey, min_cnt) # 마지막 단계까지 더해주기!
        return
    
    next_storey = storey//10
    next_cnt = storey%10
    #print('? {} {} {} {}'.format(next_storey, next_cnt, next_storey+1, (10-next_cnt)))
    
    cal_storey_min(next_storey, total_cnt+next_cnt)
    cal_storey_min(next_storey+1, total_cnt+(10-next_cnt))
    
def solution1(storey):
    global min_cnt

    cal_storey_min(storey, 0)
    #print(min_cnt)
    
    return min_cnt


# 해설 code. 별도의 재귀함수를 만들지 않고 한 function에서 해결 가능
def solution(storey):
    
    if storey <= 1:
        return storey
    
    # 몫, 나머지를 구하는 내장함수!
    q, r = divmod(storey, 10)
    
    return min( solution(q)+r, solution(q+1)+(10-r) ) 


def solution2(storey):
    
    if storey <= 0:
        return storey
    
    mok, na = divmod(storey, 10)
    
    return min( solution2(mok)+na , solution2(mok+1)+(10-na) )



print(solution1(16))
print(solution(16))
print(solution2(16))
