
l1 = [1, 20, 4, 11, 25]
l2 = sorted(l1, key=lambda x:str(x)[0])
print(l1)
print(l2)

numbers1 = [6, 10, 2]
numbers = [3, 30, 34, 5, 9]
numbers2 = [3, 30, 34, 5, 9, 20, 222, 1]
numbers3 = [3, 30, 34, 5, 9, 21, 10, 2]

# 1번째 자리 기준으로 배열 정렬
numbers.sort(key = lambda x : str(x)[0] , reverse=True)
print(numbers)

cnt = 0
numbers_len = len(numbers)

while cnt < numbers_len:
    if str(numbers[cnt])[0] == str(numbers[cnt+1])[0]:
        # 앞자리 같은 것끼리 정렬
        
# 아냐 완전 다르게 풀어보자







'''
# 반복문 제어하기 위한 변수
cnt = 0
numbers_len = len(numbers)
while cnt < numbers_len:
    print('?', cnt, numbers[cnt])
    # 앞자리가 똑같은 원소가 있는지 확인
    for ni2 in range(cnt+1, numbers_len):
        if str(numbers[cnt])[0] == str(numbers[ni2])[0]:
            continue
        else:
            break
    if cnt == ni2-1:
        print(numbers[cnt])
        answer += str(numbers[cnt])
        cnt += 1
    else:
        # 우선순위 정하기
        for i in range(cnt, ni2):
            print(numbers[i])
        cnt = ni2
print('!', cnt, numbers[cnt])



# 반복문 제어하기 위한 변수
cnt = 0
numbers_len = len(numbers)
while cnt < numbers_len :
    print('?', cnt, numbers[cnt])
    # 앞자리가 똑같은 원소가 있는지 확인
    for ni2 in range(cnt+1, numbers_len):
        if str(numbers[cnt])[0] == str(numbers[ni2])[0]:
            continue
        else:
            break
    print('what?', cnt, ni2)
    if cnt == ni2-1:
        print('??', numbers[cnt])
        answer += str(numbers[cnt])
        cnt += 1
    else:
        # 우선순위 정하기
        for i in range(cnt, ni2):
            print(numbers[i])
        cnt = ni2
print('!', cnt, numbers[cnt])
        

'''     

