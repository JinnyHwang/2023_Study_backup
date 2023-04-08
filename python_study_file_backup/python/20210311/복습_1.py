
while True :
    n, k = map( int, input().split(',', 2) )

    if (n >=2 and n <= 100000) and (k>=2 and k<=100000) :
        if n < k :
            print("앞에 입력하는 숫자가 더 커야함! 다시 입력~ ", end='')
            continue
        print('%d 을 %d 로 나누거나 빼는 연산 시작!' % (n, k) )
        break
    else :
        print(' 2 ~ 100000 사이 숫자를 입력하세요~ ', end='')
        n = 0
        k = 0
        continue

cal_count = [0, 0]

while True :

    if n%k != 0 :
        print('빼자')
        n -= 1
        cal_count[0] += 1
    else :
        print("나누자")
        n = int(n/k)
        cal_count[1] += 1

    if n == 1 :
        break

print('%d, %d, %d' % (cal_count[0],cal_count[1], cal_count[0]*cal_count[1]))
