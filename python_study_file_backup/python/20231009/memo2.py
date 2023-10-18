
# backtracking을 이용하기
# 가로줄 M개 중 사용할 가로줄 조합을 모두 만들어보기

n, m = tuple(map(int, input().split()))

lines = []
selected_lines = []
ans = m

for _ in range(m):
    a,b = tuple(map(int, input().split()))
    lines.append((b,a-1))
lines.sort()
# n의 범위 0~n-1
# m값을 기준으로 m 1~15 line중 n값이 있는 list
#print(lines)

def possible():
    
    # 시작 숫자 셋팅 0~n-1
    num1, num2 = [i for i in range(n)], [i for i in range(n)]
    
    # 위에서부터 순서대로 적혀있는 가로줄에 대해 양쪽 번호에 해당하는 숫자를 바꿔줌
    # 사다리 선에 따라 변경되는 n기둥의 목적지를 num1 value를 섞어가면서 표현함
    for _,idx in lines:
        num1[idx], num1[idx+1] = num1[idx+1], num1[idx]
    #print('1: ', lines, num1)
        
    for _,idx in selected_lines:
        num2[idx], num2[idx+1] = num2[idx+1], num2[idx]
    #print('2: ', selected_lines, num2)
    
    if num1 != num2:
        return False
    
    return True


def find_min_lines(cnt):
    global ans
    
    if cnt == m:
        if possible():
            ans = min(ans, len(selected_lines))
        return
    
    selected_lines.append(lines[cnt])
    find_min_lines(cnt+1)
    selected_lines.pop()
    
    find_min_lines(cnt+1)
    




find_min_lines(0)
print(ans)






