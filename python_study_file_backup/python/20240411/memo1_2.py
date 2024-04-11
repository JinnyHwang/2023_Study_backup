
BLANK = -1
WILL_EXPLODE = 0

n, m, k = tuple(map(int, input().split()))
numbers_2d [list(map(int, input().split())) for _ in range(n)]
numbers_1d = [0 for _ in range(n)]


# 주어진 시작점에 대하여
# 부분 수열의 끝 위치를 반환합니다.
def get_end_idx_of_explosion(start_idx, curr_num):
    for end_idx in range(start_idx + 1, len(numbers_1d)):
        if numbers_1d[end_idx] != curr_num:
            return end_idx - 1
        
    return len(numbers_1d) - 1


def explode():
    while True:
        did_explode = False
        curr_idx = 0
        
        while curr_idx < len(numbers_1d):
            end_idx = get_end_idx_of_explosion(curr_idx, numbers_1d[curr_idx])
        
            if end_idx - curr_idx + 1 >= m:
                # 연속한 숫자의 개수가 m개 이상이면
                # 폭탄이 터질 수 있는 경우 해당 부분 수열을 잘라내고
                # 폭탄이 터졌음을 기록해줍니다.
                del numbers_1d[curr_idx:end_idx + 1]
                did_explode = True
            else:
                # 주어진 시작 원소에 대하여 폭탄이 터질 수 없는 경우
                # 다음 원소에 대하여 탐색하여 줍니다.
                curr_idx = end_idx + 1

        if not did_explode:
            break





def copy_column(col):
    global numbers_1d
    
    numbers_1d = [
        numbers_2d[row][col]
        for row in range(n)
        if numbers_2d[row][col] != BLANK
    ]
    
def copy_result(col):
    for row in range(n - 1, -1, -1):
        numbers_2d[row][col] = numbers_1d.pop() if numbers_1d else BLANK


def simulate():
    for col in range(n):
        copy_column(col)
        explode()
        copy_result(col)


def rotate():
    global numbers_2d
    
    temp = [[BLANK for _ in range(n)] for _ in range(n)]
    
    for i in range(n-1, -1, -1):
        curr_idx = n-1
        for j in range(n-1, -1, -1):
            if numbers_2d[i][j] != BLANK:
                temp[curr_idx][n-i-1] = numbers_2d[i][j]
                curr_idx -= 1
    
    numbers_2d = temp



# 동작의 마무리는 폭발!
simulate()
for _ in range(k):
    rotate()
    simulate()






