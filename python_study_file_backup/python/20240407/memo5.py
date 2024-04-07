'''
# 격자 안에서 밀고 당기기
temp = a[n-1]
for i in range(n-1, 0, -1):
    a[i] = a[i-1]
a[0] = temp

temp = a[0][col]
for row in range(n-1):
    a[row][col] = a[row+1][col]
a[n-1][col] = temp
'''

'''
n, t = map(int, input().split())
#arr1 = list(map(int, input().split()))
#arr2 = list(map(int, input().split()))

#arr = arr1 + arr2
arr = list(map(int, input().split())) + list(map(int, input().split()))
#print(arr)
#print(arr[-1])
#print(arr[:2*n-1])

def move():
    global arr
    new_arr = [arr[-1]] + arr[:2*n-1]
    #print(new_arr)
    arr = new_arr

for _ in range(t):
    move()


for i in range(2*n):
    print(arr[i], end =' ')
    if i == n-1:
        print()
'''

'''
n, t = tuple(map(int, input().split()))
arr = list(map(int, input().split())) + list(map(int, input().split())) + list(map(int, input().split()))

def move():
    global arr
    new_arr = [arr[-1]] + arr[:3*n-1]
    arr = new_arr

for _ in range(t):
    move()

for i, a in enumerate(arr):
    print(a, end=' ')
    if (i+1)%n == 0:
        print()
'''

mapper = {'L':0, 'R':1}

n, m, q = tuple(map(int, input().split()))
#print(n, m, q)
arr = [list(map(int, input().split())) for _ in range(n)]
#print(arr)
command = []
for _ in range(q):
    row, cmd = list(input().split())
    command.append([int(row)-1, mapper[cmd]])
#print(command)

def move_L(row):
    global arr
    
    new_row = [arr[row][-1]] + arr[row][:m-1]
    #print(new_row)
    arr[row] = new_row
    
def move_R(row):
    global arr
    
    new_row = arr[row][1:m] + [arr[row][0]]
    #print(new_row)
    arr[row] = new_row

#move_L(2)
#print(arr)
#move_R(0)
#print(arr)
#move_L(2)
#print(arr)
#move_R(0)
#print(arr)

def row_in_range(row):
    return 0 <= row < n
    
def can_move_chk(row1, row2):
    if not row_in_range(row1) or not row_in_range(row2):
        return False
    
    for i in range(m):
        if arr[row1][i] == arr[row2][i]:
            return True
    return False



for row, cmd in command:
    if cmd == 0:
        move_L(row)
    elif cmd == 1:
        move_R(row)
    
    # 위쪽 탐색
    cmd1 = cmd^1
    for r1 in range(row-1,-1,-1):
        # 움직일 수 있는가?
        if not can_move_chk(r1, r1+1):
            break
        
        if cmd1 == 0:
            move_L(r1)
        elif cmd1 == 1:
            move_R(r1)
        
        cmd1 = cmd1^1
    
    # 아래쪽 탐색
    cmd2 = cmd^1
    for r2 in range(row+1,n):
        # 움직일 수 있는가?
        if not can_move_chk(r2, r2-1):
            break
        
        if cmd2 == 0:
            move_L(r2)
        elif cmd2 == 1:
            move_R(r2)
        
        cmd2 = cmd2^1


for a in arr:
    for aa in a:
        print(aa, end=' ')
    print()
        

