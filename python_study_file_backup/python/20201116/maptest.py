
#map test
#testlist = [1.1, 2.2, 3.3, 4.4]
#testlist2 = list()
#map으로 list 생성 시 list() 따로 생성하지 않아도 생긴다.
#testlist2 = list( map(int, testlist) )
#print(testlist2)


print("입력할 data 개수, 더할 횟수, 연속될 수 있는 횟수")

n, m, k = map(int, input().split(","))

print('입력할 data 개수 : ', n, ' / 더할 횟수 : ', m, ' / 연속될 수 있는 횟수 : ',k , '\n' )
#n = int( input() )

#data = list()

#print(n, '개 숫자를 입력하세요')

#for i in range(0, n) :
    #data[i] = int(input())
#    data.append( int(input()) )

print(n, '개 숫자를 입력하세요 (구분자 : ,)')
data = list(map(int, input().split(',', n)))

print(data, '\n')

data.sort()
연속될 수 있는 횟수
first = data[n-1]
second = data[n-2]

m2 = m

#초기화 해주기
result = 0

while True :
    for j in range(k) :
        if m == 0 :
            break
        result += first
        m -= 1
    if m == 0 :
        break
    result += second
    m -= 1

print('결과 값 : ', result , '\n')

result2 = 0

count_f = int(m2/(k+1))
result2 += count_f*k*first
#print(count_f, ', ', result2, '\n')

count_s = int(m2 - (count_f*k))
result2 += count_s*second
#print(count_s, ', ', result2, '\n')
    
print('결과 값 : ', result2 , '\n')


#data.sort()
#data[n - 1]
#data[n - 2]



