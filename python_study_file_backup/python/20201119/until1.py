
#n, k = int(input().split(' ', 2))

#n = int(input())
#k = int(input())


while True :
    n, k = map(int, input().split(' '))
    if (n>=2 and n<=100000) and (k>=2 and k<=100000):
        if n < k :
            print("앞에 입력하는 수는 뒤에 입력하는 수보다 커야합니다. 다시 입력하세요>>>", end=' ')
            continue
        print(n, '을 ', k, '로 나누거나 1을 빼는 연산 시작!!\n')
        break
    else :
        print("입력 숫자의 범위는 2 이상 100000 이하 입니다. 다시 입력하세요>>>", end=' ')
        n = 0
        k = 0

#count_1 = 0
#count_2 = 0
#copy_n = n
#copy_n2 = copy.deepcopy(n)

count = [0, 0]

#print(id(copy_n), ', ', id(copy_n2), ', ', id(n))
#id(copy_n)
#id(n)

while True :
    
    if n%k != 0 :
        print('1뺀다!')
        n -= 1
        print('n은?', n, '\n')
        count[0] += 1
    else :
        print('나눈다!')
        n = int(n/k)
        print('n은?', n, '\n')
        count[1] += 1
        
    if n == 1 :
        break


print(count[0], ', ', count[1], ', ', count[0] + count[1])


