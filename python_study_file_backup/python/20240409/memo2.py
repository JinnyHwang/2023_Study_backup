'''
n, m = map(int, input().split())

# 터져야할 폭탄을 기록
bomb_list = []
for _ in range(n):
    bomb_list.append(int(input()))

bomb_list = bomb_list[::-1]


def make_explosion():
    global bomb_list
    nn = len(bomb_list)

    explosion = [0 for _ in range(nn)]

    bomb_index = 0
    bomb_cnt = 1
    bomb_num = bomb_list[0]
    for i in range(1, nn+1):
        if i == nn:
        
            if bomb_cnt >= m:
                explosion[bomb_index:] = [1 for _ in range(bomb_index,nn)]
            break
        
        if bomb_num != bomb_list[i]:
            # 지금까지 본 bomb개수 확인
            if bomb_cnt >= m:
                explosion[bomb_index:i] = [1 for _ in range(bomb_index,i)]
            bomb_index = i
            bomb_num = bomb_list[i]
            bomb_cnt = 1
        else:
            bomb_cnt += 1
    
       
    #print(bomb_list)
    #print(explosion)
    
    new_bomb_list = []
    for i in range(nn):
        if explosion[i] == 0:
            new_bomb_list.append(bomb_list[i])
    
    #print('?',bomb_list)
    #print(new_bomb_list)
    
    if new_bomb_list ==  bomb_list:
        return False
    
    bomb_list = new_bomb_list
    return True
    
    
while bomb_list:
    
    if not make_explosion():
        break

#print(bomb_list)
if bomb_list:
    print(len(bomb_list))
    for b in bomb_list[::-1]:
        print(b)
else:
    print(0)
'''

'''
# 해설 1
n, m = tuple(map(int, input().split()))
numbers = [int(input()) for _ in range(n)]


def get_end_idx_of_explosion(start_idx, curr_num):
    for end_idx in range(start_idx+1, len(numbers)):
        if numbers[end_idx] != curr_num:
            return end_idx-1
    return len(numbers)-1


while True:
    did_explode = False
    
    for curr_idx, number in enumerate(numbers):
        
        # 이미 터질 예정인 폭탄은 확인하지 않음
        if number == 0:
            continue
        
        end_idx = get_end_idx_of_explosion(curr_idx, number)
    
        if end_idx - curr_idx + 1 >= m:
            numbers[curr_idx:end_idx+1] = [0]*(end_idx - curr_idx + 1)
            did_explode = True
            
    # 0보다 큰 값만 남기기
    numbers = list(filter(lambda x : x > 0, numbers))
    
    if not did_explode:
        break

print(len(numbers))
for num in numbers:
    print(num)
'''

'''
# 해설2
# index를 잘 고려하고, 지금 터지는건지 잘 기억하면서 탐색
n, m = map(int, input().split())
numbers = [int(input()) for _ in range(n)]

def get_end_idx_of_explosion(start_idx, curr_num):
    for end_idx in range(start_idx+1, len(numbers)):
        if numbers[end_idx] != curr_num:
            return end_idx-1
    return len(numbers)-1

while True:
    did_explode = False
    curr_idx = 0
    
    # 반복문의 조건이 변동을 하는데 쓸 수 있나?
    while curr_idx < len(numbers):
        end_idx = get_end_idx_of_explosion(curr_idx, numbers[curr_idx])
        
        # 폭탄이 터지면 curr_idx 원소가 바뀌니까 지금 index 다시 탐색
        if end_idx - curr_idx + 1 >= m:
            del numbers[curr_idx:end_idx+1]
            did_explode = True
        else:
            # 폭탄이 터지지 않으면 현재 다음 index 탐색
            curr_idx += 1
    
    if not did_explode:
        break

print(len(numbers))
for n in numbers:
    print(n)
'''

# 해설3
n, m = tuple(map(int, input().split()))
numbers = [ int(input()) for _ in range(n)]

def get_end_idx_of_explosion(start_idx, curr_num):
    for end_idx in range(start_idx+1, len(numbers)):
        if numbers[end_idx] != curr_num:
            return end_idx-1
    return len(numbers)-1


while True:
    did_exploed = False
    curr_idx = 0
    
    while curr_idx < len(numbers):
        end_idx = get_end_idx_of_explosion(curr_idx, numbers[curr_idx])
        
        if end_idx - curr_idx + 1 >= m:
            del numbers[curr_idx:end_idx+1]
            did_exploed = True
        else:
            curr_idx = end_idx+1

    if not did_exploed:
        break


print(len(numbers))
for n in numbers:
    print(n)
