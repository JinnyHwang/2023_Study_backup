
a = 0

print('카드 배열의 행을 입력하세요>>> ', end=' ')
row = int(input())

print('카드 배열의 열 입력하세요>>> ', end=' ')
col = int(input())

print(row , ' X ', col, ' 배열의 카드 번호 정보를 입력하세요')

card = list()
min_val = 0
max_val = 0
result_min = 0
result_max = 10001

for i in range(row) :
    #split(' ', col) -> 공백으로 입력받는데 colr 개수만큼만
    card_col = list(map(int, input().split(' ', col)))
    min_val = min(card_col)
    max_val = max(card_col)
    result_min = max(result_min, min_val)
    result_max = min(result_max, max_val)
#    for j in range(col) :
    card.append(card_col)

print(card)
print(result_min)
print(result_max)
