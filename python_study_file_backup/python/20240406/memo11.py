
# 제곱
#print(10**2)
#print(pow(10,2))

# 절대 값
#print(abs(-11))
'''
arr = [12, 41, 37, 81, 19, 25, 60, 20]

arr1 = sorted(arr)
arr1 = arr1[::-1] # 역순

arr2 = sorted(arr)
arr2 = list(reversed(arr2))

arr.sort()
arr.sort(reverse=True)
'''

'''
n = int(input())
arr = list(map(int, input().split()))

arr1 = sorted(arr)
arr2 = arr1[::-1]

for a1 in arr1:
    print(a1, end=' ')
print()
for a2 in arr2:
    print(a2, end=' ')
'''

'''
#string = 'banana'
string = list(input())
string.sort()
sort_str = ''.join(string)
print(sort_str)
'''

'''
n = int(input())
arr = [input() for _ in range(n)]

arr.sort()
for a in arr:
    print(a)
'''

'''
n, k = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
print(arr[k-1])
'''

'''
n = int(input())
# 동일 원소 여러개 없음
arr1 = set(map(int, input().split()))
arr2 = set(map(int, input().split()))
#print(arr1, arr2)
if arr1 == arr2 :
    print('Yes')
else:
    print('No')

# set으르 사용해서 통째로 비교하는 것보다
# 리스트 정렬해서 하나씩 비교하는게 덜 걸림
n = int(input())
# 동일 원소 여러개 없음
arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1.sort()
arr2.sort()

def equal():
    for el1, el2 in zip(arr1, arr2):
        if el1 != el2:
            return False
    return True

if equal():
    print('Yes')
else:
    print('No')
'''

'''
# 주어진 list로 n개 그룹 만들기
# 최댓값이 최소가 되도록
# 최댓값과 최솟값을 묶음
# 최댓값과 최솟값이 다른 그룹으로 떨어져있다면?
# 최댓값이 포함된 그룹과, 최솟값이 포함된 그룹은
# 최댓값, 최솟값이 함께 있는 그룹보다 격차가 커질 수 밖에 없다.
# M: 최댓값 , m: 최솟값
# [M,a] [m,b] a는 m보다 큼, b는 M보다 작음 이 그룹 간 격차는
# [M,m] [a,b]그룹의 격차보다 클 수 밖에 없다
# 이렇게 최대최소가 사라지고 남은 그룹의 최대최소를 묶으면서
# 격차가 작은 그룹만 만드는 것

# 최댓값, 최솟값이 포함된 그룹의 합을 출력하면 됨
n = int(input())
arr = list(map(int, input().split()))

arr.sort()

arr_max = -1
for i in range(n):
    arr_sum = arr[i] + arr[2*n-i-1]
    if arr_sum > arr_max:
        arr_max = arr_sum
print(arr_max)
'''
'''
arr1 = list(input())
arr2 = list(input())
arr1.sort()
arr2.sort()

if len(arr1) != len(arr2):
    print('No')
else:
    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            print('No')
            break
    else:
        print('Yes')
'''

'''
arr1 = input()
arr2 = input()

print('Yes' if sorted(arr1) == sorted(arr2) else 'No')
'''

'''
# 수행시간이 제일 빠름
import sys

# 문자를 아스키넘버를 index로해서 등장 횟수를 셈
ASCCI_NUM = 128

str1 = input()
str2 = input()
count = [0 for _ in range(ASCCI_NUM)]

for char1 in str1:
    count[ord(char1)] += 1

for char2 in str2:
    count[ord(char2)] -= 1


for c in count:
    if c != 0:
        print('No')
        sys.exit(0)
print('Yes')
'''

'''
n, k, word = input().split()
#print(n, k, word)
n, k = int(n), int(k)

word_len = len(word)
word_arr = []

for _ in range(n):
    input_str = input()
    if word == input_str[:word_len]:
        word_arr.append(input_str)

word_arr.sort()
print(word_arr[k-1])

'''

'''
n = int(input())
input_arr = list(map(int, input().split()))
new_arr = []

for i in range(n):
    new_arr.append(input_arr[i])
    if i%2 == 0:
        new_arr.sort()
        #print(new_arr, i, new_arr[i//2])
        print(new_arr[i//2], end=' ')
'''

'''
n = int(input())
input_arr = list(map(int, input().split()))

for i in range(n):
    if i%2 == 0:
        # i index로 확인하고 있으므로 비교가 필요한 때 해당 원소들을 sort하면됨
        sorted_arr = sorted(input_arr[:i+1])
        print(sorted_arr[i//2], end =' ')
'''
'''
완전탐색
n = 5
grid = [
    [0, 0, 0, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 1, 0, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 1, 0]
]

def get_num_of_gold(row, col_s, col_e):
    num_of_gold = 0
    for col in range(col_s, col_e+1):
        num_of_gold += grid[row][col]
    return num_of_gold

max_gold = 0
for i in range(n):
    for j in range(n):
        if j+2 >= n:
            continue
        
        num_of_gold = get_num_of_gold(i,j,j+2)
        max_gold = max(max_gold, num_of_gold)

print(max_gold)
'''
'''
n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

def sum_coin(x,y):
    coin = 0
    for x1 in range(x,x+3):
        for y1 in range(y,y+3):
            coin += arr[x1][y1]
    return coin
            
    
max_coin = 0
for i in range(n):
    if i+2 <n:
        for j in range(n):
            if j+2 >= n:
                continue
            coins = sum_coin(i,j)
            max_coin = max(max_coin, coins)
print(max_coin)
'''            

'''
# 행복한 수열 개수 세기
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

happy = 0

# 행 탐색
for i in range(n):
    cnt = 0
    before = 0
    for j in range(n):
        #print(i, j, arr[i][j], cnt, before)
        if j == 0:
            before = arr[i][j]
            cnt = 1
            if cnt >= m:
                #pritn('?')
                happy += 1
                break
        else:
            if before == arr[i][j]:
                cnt += 1
                if cnt >= m:
                    #print('!')
                    happy += 1
                    break
            else:
                before = arr[i][j]
        
#print(happy)

# 열 탐색
# 행 탐색
for i in range(n):
    for j in range(n):
        if j == 0:
            before = arr[j][i]
            cnt = 1
            if cnt >= m:
                happy += 1
                break
        else:
            
            if before == arr[j][i]:
                cnt += 1
                if cnt >= m:
                    happy += 1
                    break
            else:
                before = arr[j][i]
            
print(happy)
'''

'''
n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]
seq = [0 for _ in range(n)]

def is_happy_sequence():
    max_ccnt, consecutive_cnt = 1,1
    for i in range(1,n):
        if seq[i-1] == seq[i]:
            consecutive_cnt += 1
        else:
            consecutive_cnt = 1
            
        max_ccnt = max(max_ccnt, consecutive_cnt)
    return max_ccnt >= m

num_happy = 0

for i in range(n):
    seq = grid[i][:]
    if is_happy_sequence():
        num_happy += 1

for i in range(n):
    for j in range(n):
        seq[j] = grid[j][i]
    if is_happy_sequence():
        num_happy += 1
        
print(num_happy)
'''

# 블럭을 회전, 뒤집 가능한 모양은 총 6개
# 가능한 모든 모양을 적고 격자를 순회함
# 3*3 블럭 6개 준비
# 그리고 블럭을 최대한 (0,0)에 붙여서 틀을 만들어야
# 격자를 벗어나지 않는데 못세는 경우를 방지할 수 있다.
shapes = [
    [[1, 0, 0],
     [1, 1, 0],
     [0, 0, 0]],
    
    [[1, 1, 0],
     [0, 1, 0],
     [0, 0, 0]],
    
    [[0, 1, 0],
     [1, 1, 0],
     [0, 0, 0]],
    
    [[1, 1, 0],
     [1, 0, 0],
     [0, 0, 0]],
    
    [[1, 1, 1],
     [0, 0, 0],
     [0, 0, 0]],
    
    [[1, 0, 0],
     [1, 0, 0],
     [1, 0, 0]]
]

n, m = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(n)]

def get_max_sum(x,y):
    max_sum = 0
    for i in range(6):
        sum_flag = True
        now_sum = 0
        for sx in range(3):
            for sy in range(3):
                if shapes[i][sx][sy] == 0:
                    continue
                # range 안인지
                if x+sx >= n or y+sy >= m:
                    sum_flag = False
                else:
                    now_sum += grid[x+sx][y+sy]
        if sum_flag:
            max_sum = max(max_sum, now_sum)
    return max_sum
                
ans = 0
for i in range(n):
    for j in range(m):
        ans = max(ans, get_max_sum(i,j))

print(ans)






























