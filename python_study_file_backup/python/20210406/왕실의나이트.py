
#나이트가 이돌할 수 있는 step 경우의 수
#(2, 1) (1, 2)

#ord('a') -> 97 : 문자의 아스키 코드 값을 return하는 method
#chr(97) -> 'a' : 아스키 코드 값을 보고 문자를 return하는 method

# 1*1 ~ 8*8
input_data = input()
row = int( input_data[1] )
col = int( ord(input_data[0]) - ord('a') ) + 1

steps = [(-2, -1), (-2, 1), (-1, -2), (-1, 2), (1, -2), (1, 2), (2, -1), (2, 1)]

count = 0

for step in steps :
    next_row = row + step[0]
    next_col = col + step[1]

    if next_row >= 1 and next_row <= 8 and next_col >= 1 and next_col <= 8 :
        count += 1

print(count)
