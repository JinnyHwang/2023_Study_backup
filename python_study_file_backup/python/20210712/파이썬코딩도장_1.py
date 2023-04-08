
# 한 줄에 여러 구문 작성 시 세미콜론 활용
print('Test'); print('Test2')

# 파이썬 들여쓰기 방법
a = 1
if a == 1 :
  print('a1 : ', a) # 공백 2칸

a = 2
if a == 2 :
    print('a2 : ', a) # 공백 4칸
    print('a3 : ', a) # tab
else :
    print('a is not 2')
print('end')


# 파이썬 자료형
# int(정수), float(실수), complex(복소수)

# 거듭제곱
print('2^10(2**10) : ', 2**10)

# 객체의 자료형 확인
print('5/2 = ', 5/2, '\t\t type(5/2) : ', type(5/2))
print('5/2.0 = ', 5/2.0, '\t\t type(5/2.0) : ', type(5/2.0))
print('5//2 = ', 5//2, '\t\t type(5//2) : ', type(5//2))
print('5//2.0 = ', 5//2.0, '\t\t type(5//2.0) : ', type(5//2.0))
print('5.0//2.0 = ', 5.0//2.0, '\t\t type(5.0//2.0) : ', type(5.0//2.0))


# 몫과 나머지 함께 구하기
print('divmod(5, 2) : ', divmod(5, 2))


# 2진수, 8진수, 16진수
print('2진수 : ', 0b110); print('8진수 : ', 0o10); print('16진수 : ', 0xF)


# 실수 값의 오차 https://dojang.io/mod/page/view.php?id=2171
print('4.3 - 2.7 = ', 4.3 - 2.7 )

# https://dojang.io/mod/page/view.php?id=2466
# 파이썬은 부동소수점 방식을 사용
print("0.1 + 0.2 : ", 0.1 + 0.2)













