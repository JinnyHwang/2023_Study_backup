
#검색할 데이터 개수가 100만개 이하일 경우 완전탐색 가능
#N시 59분 59초 까지의 모든 수를 문자열로 변환해서 탐색
#문자열 안에 숫자 3이 존재 하는지 확인

hour = int(input())

count = 0

for i in range(hour+1) :
    for j in range(60) :
        for k in range(60) :
            if '3' in str(i) + str(j) + str(k) :
                count += 1
            #print(str(i) + str(j) + str(k))

print(count)






