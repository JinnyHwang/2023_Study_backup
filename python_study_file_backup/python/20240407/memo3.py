'''
# 두 개 직사각형 만들기
# 완전 탐색으로 영역 2개 만들기

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
grid_visited1 = [[0  for _ in range(m)] for _ in range(n)]
grid_visited2 = [[0  for _ in range(m)] for _ in range(n)]

def in_range(x,y):
    return 0 <= x < n and 0 <= y < m

#def can_make_square(x, y, len1, len2):
#    global grid_visited
#    
#    for i in range(x, x+len1):
#        for j in range(y, y+len2):
#            # 범위를 벗어나거나, 이미 방문했거나
#            if not in_range(i,j) or grid_visited[i][j]:
#                return False
#            grid_visited[i][j] = 1
#    print(grid_visited)
#    return True

def print_grid():
    for i in range(n):
        for j in range(m):
            if grid_visited1[i][j] or grid_visited2[i][j]:
                print(1, end=' ')
            else:
                print(0, end=' ')
        print()


def can_make_square1(x, y, len1, len2):
    global grid_visited1
    
    for i in range(x, x+len1):
        for j in range(y, y+len2):
            # 범위를 벗어나거나, 이미 방문했거나
            if not in_range(i,j):
                return False
            grid_visited1[i][j] = 1
    #print('grid_visited1: ', grid_visited1)
    return True

def can_make_square2(x, y, len1, len2):
    global grid_visited2
    
    for i in range(x, x+len1):
        for j in range(y, y+len2):
            # 범위를 벗어나거나, 이미 방문했거나
            if not in_range(i,j) or grid_visited1[i][j]:
                return False
            grid_visited2[i][j] = 1
    #print('grid_visited2?: ', grid_visited2)
    return True


def grid_sum():
    #print('grid_visited1: ', grid_visited1, 'grid_visited2?: ', grid_visited2)
    return sum([
            grid[i][j]
            for i in range(n)
            for j in range(m)
            if grid_visited1[i][j] == 1 or grid_visited2[i][j] == 1
        ])

            
max_sum = -1e9
for i in range(n):
    for j in range(m):
        for len1 in range(1, n+1):
            for len2 in range(1, m+1):
                #print('sq 1?')
                if can_make_square1(i, j, len1, len2):
                    # 두 번째 사각형 탐색
                    for i2 in range(n):
                        for j2 in range(m):
                            for len11 in range(1, n+1):
                                for len22 in range(1, m+1):
                                    #print('sq 2?')
                                    if can_make_square2(i2, j2, len11, len22):
                                        cal_sum = grid_sum()
                                        #print(cal_sum)
                                        max_sum = max(max_sum, cal_sum)
                                        #if cal_sum > max_sum:
                                            #print(cal_sum)
                                            #print('grid_visited1: ', grid_visited1, 'grid_visited2?: ', grid_visited2)
                                            #print_grid()
                                        
                                    #else:
                                    #    print('sq 2 is fail')
                                    grid_visited2 = [[0  for _ in range(m)] for _ in range(n)]
                #else:
                #    print('sq 1 is fail')
                grid_visited1 = [[0  for _ in range(m)] for _ in range(n)]
                
                    
print(max_sum)           
        
'''

# 해설
# 두 직사각형이 겹쳐지는가?
# 가능한 모든 2개의 직사각형 쌍을 잡아보기
import sys

INT_MIN = -sys.maxsize

# 변수 선언 및 입력:
n, m = tuple(map(int, input().split()))
grid = [
    list(map(int, input().split()))
    for _ in range(n)
]
board = [
    [0 for _ in range(m)]
    for _ in range(n)
]


def clear_board():
    for i in range(n):
        for j in range(m):
            board[i][j] = 0

            
def draw(x1, y1, x2, y2):
    for i in range(x1, x2 + 1):
        for j in range(y1, y2 + 1):
            board[i][j] += 1

            
def check_board():
    # 동일한 칸을 2개의 직사각형이 모두 포함한다면
    # 겹치게 됩니다.
    for i in range(n):
        for j in range(m):
            if board[i][j] >= 2:
                return True
    return False


# (x1, y1), (x2, y2) 그리고
# (x3, y3), (x4, y4) 로 이루어져있는
# 두 직사각형이 겹치는지 확인하는 함수
def overlapped(x1, y1, x2, y2, x3, y3, x4, y4):
    clear_board()
    draw(x1, y1, x2, y2)
    draw(x3, y3, x4, y4)
    return check_board()


def rect_sum(x1, y1, x2, y2):
    return sum([
        grid[i][j]
        for i in range(x1, x2 + 1)
        for j in range(y1, y2 + 1)
    ])


# 첫 번째 직사각형이 (x1, y1), (x2, y2)를 양쪽 꼭지점으로 할 때
# 두 번째 직사각형을 겹치지 않게 잘 잡아
# 최대 합을 반환하는 함수
def find_max_sum_with_rect(x1, y1, x2, y2):
    max_sum = INT_MIN
    
    # (i, j), (k, l)을 양쪽 꼭지점으로 하는
    # 두 번째 직사각형을 정하여
    # 겹치지 않았을 때 중
    # 최댓값을 찾아 반환합니다.
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    if not overlapped(x1, y1, x2, y2, i, j, k, l):
                        max_sum = max(max_sum, 
                                      rect_sum(x1, y1, x2, y2) +
                                      rect_sum(i, j, k, l))
    
    return max_sum


# 두 직사각형을 잘 잡았을 때의 최대 합을 반환하는 함수
def find_max_sum():
    max_sum = INT_MIN
    
	# (i, j), (k, l)을 양쪽 꼭지점으로 하는
    # 첫 번째 직사각형을 정하여
    # 그 중 최댓값을 찾아 반환합니다.
    for i in range(n):
        for j in range(m):
            for k in range(i, n):
                for l in range(j, m):
                    max_sum = max(max_sum,
                                  find_max_sum_with_rect(i, j, k, l))
    return max_sum


ans = find_max_sum()
print(ans)



