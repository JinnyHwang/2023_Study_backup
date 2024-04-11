'''
# 해설1
n, m, k = map(int, input().split())
apple = [[False for _ in range(n+1)] for _ in range(n+1)]
snake = [(1,1)]
mapper = {
    'D': 0,
    'U': 1,
    'R': 2,
    'L': 3
}
ans = 0

def can_go(x,y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def is_twisted(new_head):
    return new_head in snake

def push_front(new_head):
    if is_twisted(new_head):
        return False
    
    snake.insert(0, new_head)
    return True

def pop_back():
    snake.pop()
    

def move_snake(nx, ny):
    
    if apple[nx][ny]:
        apple[nx][ny] = False
        if not push_front(nx, ny):
            return False
    else:
        pop_back()
        if not push_front(nx, ny):
            return False
        
    return True


def move(move_dir, num):
    global ans
    
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    
    for _ in range(num):
        ans += 1
        
        (head_x, head_y) = snake[0]
        nx = head_x + dxs[move_dir]
        ny = head_y + dys[move_dir]
        
        if not can_go(nx, ny):
            return False
        
        if not move_snake(nx, ny):
            return False
    
    return True
    



for _ in range(m):
    x, y = map(int, input().split())
    apple[x][y] = True

for _ in range(k):
    move_dir, num = tuple(input().split())
    num = int(num)
    
    if not move(mapper[move_dir], num):
        break

print(ans)
'''

'''
# 해설2
# 뱀의 상태를 이중연결리스트 DoublyLinkedList를 통해 관리
# deque 덱 double ended queue
# stack, queue를 모두 지원하는 자료구조
# 양 끝에서 삽입, 삭제가 가능함
# append()/appendleft()
# pop()/popleft()
# extend()/extendleft()

import collections

n, m, k = map(int, input().split())
apple = [[False for _ in range(n+1)] for _ in range(n+1)]
snake = collections.deque([1,1])

mapper = {
    'D': 0,
    'U': 1,
    'R': 2,
    'L': 3
}

ans = 0


# (x, y)가 범위 안에 들어가는지 확인합니다.
def can_go(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n


# 뱀이 꼬였는지 확인합니다.
def is_twisted(new_head):
    return new_head in snake


def push_front(new_head):
    
    if is_twisted(new_head):
        return False
    
    snake.appendleft(new_head)
    
    return True


def pop_back():
    snake.pop()
    
   
def move_snake(nx, ny):
    
    if apple[nx][ny]:
        apple[nx][ny] = False
        if not push_front((nx,ny)):
            return False
        
    else:
        pop_back()
        if not push_front((nx,ny)):
            return False
    
    return True
        

def move(move_dir, num):
    global ans
    
    dxs = [1, -1, 0, 0]
    dys = [0, 0, 1, -1]
    
    for _ in range(num):
        ans += 1
        
        (head_x, head_y) = snake[0]
        nx = head_x + dxs[move_dir]
        ny = head_y + dys[move_dir]
        
        if not can_go(nx, ny):
            return False
        
        if not move_snake(nx, ny):
            return False
    
    return True
    
# 사과가 있는 위치를 표시합니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    apple[x][y] = True

# K개의 명령을 수행합니다.
for _ in range(K):
    # move_dir 방향으로 num 횟수 만큼 움직여야 합니다.
    move_dir, num = tuple(input().split())
    num = int(num)
    
    # 움직이는 도중 게임이 종료되었을 경우
    # 더 이상 진행하지 않습니다.
    if not move(mapper[move_dir], num):
        break

print(ans)
'''

# 해설3
# 뱀의 상태를 DoublyLinkedList로 관리
# HashSet으로 뱀을 이루는 block 위치가 겹치지 않고 한 번만 나왔는지 확인

import collections

n, m, k = map(int, input().split())
apple = [[False for _ in range(n+1)] for _ in range(n+1)]

snake = collections.deque()
snake.appendleft((1,1))
snake_pos = set()
snake_pos.append((1,1))



mapper = {
    'D': 0,
    'U': 1,
    'R': 2,
    'L': 3
}

ans = 0


# (x, y)가 범위 안에 들어가는지 확인합니다.
def can_go(x, y):
    return 1 <= x and x <= n and 1 <= y and y <= n

def is_twisted(new_head):
    return new_head in snake_pos

# 새로운 머리를 추가합니다.
def push_front(new_head):
    # 몸이 꼬이는 경우
    # false를 반환합니다.
    if is_twisted(new_head):
        return False
    
    # 새로운 머리를 추가하고
    snake.appendleft(new_head)
    # HashSet에 새로운 좌표를 기록합니다.
    snake_pos.add(new_head)
            
    # 정상적으로 머리를 추가했다는 의미로
    # True를 반환합니다.
    return True


# (nx, ny)쪽으로 뱀을 움직입니다.
def move_snake(nx, ny):
    # 머리가 이동할 자리에 사과가 존재하면
    # 사과는 사라지게 되고
    if apple[nx][ny]:
        apple[nx][ny] = False
        # 꼬리는 사라지지 않고 머리만 늘어납니다.
        # 늘어난 머리때문에 몸이 꼬이게 된다면
        # False를 반환합니다.
        if not push_front((nx, ny)):
            return False
    else:
        # 사과가 없으면 꼬리는 사라지게 되고
        pop_back()
        
        # 머리는 늘어나게 됩니다.
        # 늘어난 머리때문에 몸이 꼬이게 된다면
        # False를 반환합니다.
        if not push_front((nx, ny)):
            return False
    
    # 정상적으로 뱀이 움직였으므로
    # True를 반환합니다.
    return True


# 뱀을 move_dir 방향으로 num번 움직입니다.
def move(move_dir, num):
    global ans
    
    dxs, dys = [1, -1, 0, 0], [0, 0, 1, -1]
    
    # num 횟수만큼 뱀을 움직입니다.
    # 한 번 움직일때마다 답을 갱신합니다.
    for _ in range(num):
        ans += 1
        
        # 뱀의 머리가 그다음으로 움직일
        # 위치를 구합니다.
        (head_x, head_y) = snake[0]
        nx = head_x + dxs[move_dir]
        ny = head_y + dys[move_dir]
        
        # 그 다음 위치로 갈 수 없다면
        # 게임을 종료합니다.
        if not can_go(nx, ny):
            return False
        
        # 뱀을 한 칸 움직입니다.
        # 만약 몸이 꼬인다면 False를 반환합니다.
        if not move_snake(nx, ny):
            return False
    
    # 정상적으로 명령을 수행했다는 의미인 True를 반환합니다.
    return True



# 사과가 있는 위치를 표시합니다.
for _ in range(m):
    x, y = tuple(map(int, input().split()))
    apple[x][y] = True

# K개의 명령을 수행합니다.
for _ in range(k):
    # move_dir 방향으로 num 횟수 만큼 움직여야 합니다.
    move_dir, num = tuple(input().split())
    num = int(num)
    
    # 움직이는 도중 게임이 종료되었을 경우
    # 더 이상 진행하지 않습니다.
    if not move(mapper[move_dir], num):
        break

print(ans)




