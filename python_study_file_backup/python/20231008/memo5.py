
boom1 = [(0,0),(-1,0),(-2,0),(1,0),(2,0)]
boom2 = [(0,0),(1,0),(-1,0),(0,-1),(0,1)]
boom3 = [(0,0),(-1,-1),(-1,1),(1,1),(1,-1)]
booms = [boom1]+[boom2]+[boom3]
print(booms)


# 1이상 4이하의 숫자로 이루어져 있음
# 아름다운 수 : 해당 숫자만큼 연달아 같은 숫자가 나오는 숫자
# n자리 아름다운 수는? 1 <= n <= 10

# 1~4로 이루어진 모든 숫자를 만들어낸 후 아름다운 수를 세는 것

n = int(input())
ans = 0
seq = []

def is_beautiful():
    # 탐색 인덱스
    idx = 0
    
    while idx < n:
        # 길이 조건은 충족하는지 확인
        # 최소한 나와야하는 숫자보다 길이가 짧으면 False
        if idx+seq[idx]-1 >= n:
            return False
        
        # 연속하여 해당 숫자만큼 같은 숫자가 있는지 확인
        for j in range(idx, idx+seq[idx]): # seq[idx]값만큼 길이 체크
            if seq[idx] != seq[j]:
                return False
        # 확인이 끝나면 다음 index 확인
        idx += seq[idx]
    
    #print(seq)
    return True


# 숫자 만들기
def make_num(index):
    global ans
    
    if index == n:
        if is_beautiful():
            ans += 1
        return
    
    for num in range(1,5):
        seq.append(num)
        make_num(index+1)
        seq.pop()

make_num(0)
print(ans)

