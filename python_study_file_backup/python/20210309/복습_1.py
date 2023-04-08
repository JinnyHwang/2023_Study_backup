cycle = int(input("반복 횟수? "))
print("\n")

for i in range(0, cycle) :
    change = int(input("거스름돈? "))
    print("\n")

    #크기가 4인 배열 선언
    count_list = [0 for i in range(4)]
    #result = [x*y for x in range(2,10) for y in range(1,10)]
    #print(result)

    count_index = 0

    coin_types = [500, 100, 50, 10]

    for coin in coin_types :
        count_list.insert(count_index, int(change/coin))
        count_index += 1
        change %= coin
        if change == 0 :
            break

    print("[1] \n\t500 : %d \n\t100 : %d \n\t50 : %d \n\t10 : %d \n" %(count_list[0], count_list[1], count_list[2], count_list[3]) )
    print("[2]", "500 : ", count_list[0], "100 : ", count_list[1], "50 : ", count_list[2], "10 : ", count_list[3], sep = "\t")
    print("거스름돈 동전 개수? ", sum(count_list), "\n" )
    
print("거스름돈 계산 끝! %d 번 반복! \n" %cycle, end = '')
print("Test\n")
