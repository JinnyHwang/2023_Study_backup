m = int(input("반복할 횟수는? "))
print('\n')
for i in range(0, m) :    
    n = int(input("거스름돈은? "))
    print('\n')

    #크기가 미리 지정된 list를 선언 시
    #for문을 이용하여 원하는 배열 개수 만큼 0으로 초기화 시켜준다.
    #0 for i in range(n)
    count = [0 for i in range(4)]

    count_index = 0

    coin_types = [500, 100, 50, 10]
 
    for coin in coin_types :
    #    print(coin)
        count.insert(count_index, int(n/coin))
        count_index += 1
    #    print(count)
        n %= coin
    #    print(n)
        if n == 0 :
            break

    print('====거스름돈 각 동전의 개수 ====\n500: %d \n100: %d \n50: %d \n10: %d\n' % (count[0], count[1], count[2],count[3]))
    print("거스름돈 동전 개수는?", sum(count), "\n")
    print("500원 짜리는?", count[0],"이만큼!" )
    print("50원 짜리는? %d 이만큼!\n\n" % count[2])

print("반복문 %d번 끝났다~~\n" %m)
