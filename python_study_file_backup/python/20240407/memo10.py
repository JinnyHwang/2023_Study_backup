'''
BLANK = 0

n = 6

arr = [[0 for _ in range(n)] for _ in range(n)]
temp = [[0 for _ in range(n)] for _ in range(n)]

col = 3
for row in range(n-1, -1, -1):
    temp[row][col] = BLANK

temp_row = n-1
for row in range(n-1, -1, -1):
    if arr[row][col] != BLANK:
        temp[temp_row][col] = arr[row][col]
        temp_row -= 1

for row in range(n):
    arr[row][col] = temp[row][col]
'''
'''
end_of_array = 6
arr = [0 for _ in range(6)]
temp = [0 for _ in range(6)]

end_of_temp_array = 0

for i in range(end_of_array):
    if arr[i] != BLANK:
        temp[end_of_temp_array] = arr[i]
        end_of_temp_array += 1

for i in range(end_of_temp_array):
    arr[i] = temp[i]

end_of_array = end_of_temp_array
'''

'''
n = int(input())
arr = []
for _ in range(n):
    num = int(input())
    arr.append(num)
#arr = arr[::-1]
#print(arr)

cmd = []
for _ in range(2):
    s, e = map(int, input().split())
    cmd.append([s-1, e-1])
#print(cmd)

for s, e in cmd:
    #print(arr[:s],arr[e+1:])
    new_arr = arr[:s]+arr[e+1:]
    #print(new_arr)
    arr = new_arr[:]

print(len(arr))
for a in arr:
    print(a)
'''

'''
n = int(input())
numbers = [int(input()) for _ in range(n)]
end_of_array = n

def cut_array(s, e):
    global numbers, end_of_array
    
    temp_arr = []
    
    for i in range(end_of_array):
        if i < s or i > e:
            temp_arr.append(numbers[i])
    
    end_of_array = len(temp_arr)
    for i in range(end_of_array):
        numbers[i] = temp_arr[i]


for _ in range(2):
    s,e = map(int, input().split())
    cut_array(s-1, e-1)

print(end_of_array)
for i in range(end_of_array):
    print(numbers[i])
'''

# end index+1 부터 n-1까지 원소들을 확인하면서
# 없애야하는 구간 길이만큼 앞당겨주기
n = int(input())
numbers = [int(input()) for _ in range(n)]
end_of_array = n


def cut_array(s, e):
    global numbers, end_of_array
    
    cut_len = e-s+1
    for i in range(e+1, end_of_array):
        numbers[i-cut_len] = numbers[i]
        
    end_of_array -= cut_len

for _ in range(2):
    s,e = map(int, input().split())
    cut_array(s-1, e-1)

print(end_of_array)
for i in range(end_of_array):
    print(numbers[i])








