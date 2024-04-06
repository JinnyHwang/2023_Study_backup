
# 0 <-> 1 , 2 <-> 3
# 현재 방향에서 1을 xor
# xor은 bit 단위로 연산. 같은 숫자면 0, 다른 숫자면 1
# 00 01 10 11 을 xor하면 01 00 11 10
# d^1

# 0 <-> 3 , 1 <-> 2
# 숫자 3에서 현재 방향 빼주면 됨
# 3-0 3-3 3-1 2-1
# 3-d


n = int(input())
arr = [input() for _ in range(n)]
start_num = int(input())

# 시작위치, 방향구하기
# 아 간단하게 구할 수 있네...
def initialize(num):
    if num <= n:
        return 0, num-1, 0
    elif num <= 2*n:
        return num-n-1, n-1, 1
    elif num <= 3*n:
        return n-1, n-(num - 2*n), 2
    else:
        return n-(num -3*n), 0, 3


def in_range(x, y):
    return 0 <= x and x < n and 0 <= y and y < n

def move(x, y, next_dir):        
    dxs = [1, 0, -1, 0]
    dys = [0, -1, 0, 1]
    nx, ny = x + dxs[next_dir], y + dys[next_dir]
    return nx, ny, next_dir



def simulate(x, y, move_dir):
    move_num = 0
    
    # 이렇게 조건을 달면 break문이 따로 필요하지 않구나..
    while in_range(x,y):
        # 현재 위치와 변경되는 방향값을 주어 다음 위치 확인
        # / 는 SW 남서 , EN 동북  01 23
        if arr[x][y] == '/':
            x, y, move_dir = move(x, y, move_dir^1)
        # / 는 SW 남서 , EN 동북  12 03
        else:
            x, y, move_dir = move(x, y, 3-move_dir)
        
        move_num += 1
    
    return move_num



# 시작 위치와 방향
x, y, move_dir = initialize(start_num)

# 시뮬레이션 시작!
move_num = simulate(x, y, move_dir)
print(move_num)




