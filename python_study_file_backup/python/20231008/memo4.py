
# 재귀 종료조건, 재귀호출부분
# 재귀를 사용하면 순열,조합을 만들 때 모든 조합을 만들지 않아도 답을 도출할 수 있음

# n이 주어지고 n자리의 2진수를 전부 출력
# 원하는 2진수 조합을 모두 만들자
n = 3
ans = []
def print_answer():
    for a in ans:
        print(a,end='')
    print()
    

def choose(curr_num):
    
    if curr_num == n+1:
        print_answer()
        return
    
    # 0
    ans.append(0)
    choose(curr_num+1)
    ans.pop()
    
    # 1
    ans.append(1)
    choose(curr_num+1)
    ans.pop()
    
    return

choose(1)





