
n = int(input())
line = [0 for _ in range(1001)]

ans = 0
input_lines = []
select_lines = []

for _ in range(n):
    input_lines.append(list(map(int, input().split())))
#print(input_lines)


# 선택 line이 겹치는지 확인
# 겹치면 Ture
def line_cross(ll):
    line = [0 for _ in range(1001)]
    for li in ll:
        x1, x2 = input_lines[li]
        for xx in range(x1,x2+1):
            if line[xx] != 0:
                return True
            else:
                line[xx] = 1
    return False

def possible1():
    line = [0 for _ in range(1001)]
    for x1, x2 in select_lines:
        for xx in range(x1,x2+1):
            if line[xx] != 0:
                return False
            else:
                line[xx] = 1
    return True
        
def overlapped(seg1, seg2):
    (ax1, ax2), (bx1,bx2) = seg1, seg2
    
    return (ax1 <= bx1 and bx1 <= ax2) or (ax1 <= bx2 and bx2 <= ax2) or \
            (bx1 <= ax1 and ax1 <= bx2) or (bx1 <= ax2 and ax2 <= bx2)


def possible():
    for i, seg1 in enumerate(select_lines):
        for j, seg2 in enumerate(select_lines):
            if i<j and overlapped(seg1, seg2):
                return False
    return True



# 조합 만들기. 현재 선택 or 선택안함
def find_max_lines(cnt):
    global ans
    
    if cnt == n:
        if possible():
            ans = max(ans, len(select_lines))
        return
    
    # 현재 line을 선택한 경우
    select_lines.append(input_lines[cnt])
    find_max_lines(cnt + 1)
    select_lines.pop()
    
    # 현재 line을 선택하지 않은 경우
    find_max_lines(cnt + 1)


select_lines = []

def find_max_lines(cnt):
    
    if cnt == n:
        return
    
    # 포함 시키는가? 안시키는가? 조합 만들기
    
    # cnt index의 data를 선택
    select_lines.append(input_lines[cnt])
    find_max_lines(cnt+1)
    select_lines.pop()
    
    # cnt index의 data를 패스
    find_max_lines(cnt+1)





find_max_lines(0)
print(ans)



