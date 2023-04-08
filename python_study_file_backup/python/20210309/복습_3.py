
# 변수 개수보다 많이 입력하면?
# 답: ValueError 발생
n, m, k = map(int, input().split(","))

#, 로 구분하여 n개 data를 list 형태로초기화
data = list( map(int, input().split(',',n)) )

data.sort()
first = data[n-1]
second = data[n-2]
print('first : ', first, 'second : ', second)




print("행을 입력 : ", end='')
col = int(input())

print("열을 입력 : ", end='')
row = int(input())

card = list()
min_val = 0
max_val = 0
result_min = 0
result_max = 10001

# input().split(' ', col)
# 입력받는 숫자를 , 으로 구분하고 col개만큼 split함.

for x in range(row) :
    card_col = list( map( int, input().split(',', col) ) )
    print('[card_col] = ', card_col)
    min_val = min(card_col)
    max_val = max(card_col)
    result_min = max(min_val, result_min)
    result_max = min(max_val, result_max)
    card.append(card_col)

print(card)
print(result_min)
print(result_max)
