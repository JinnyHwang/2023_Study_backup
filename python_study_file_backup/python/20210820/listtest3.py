
str = "오늘은 날씨가 흐림"

#list()로 하지 않아도 list type으로
str_list = str.split()
print(str_list)
print(type(str_list))

position = str_list.index('흐림')

str_list[position] = '맑음'
print("문자열의 {} 위치의 값은 {}".format(position, str_list[position]))

str = " ".join(str_list)
print(str)