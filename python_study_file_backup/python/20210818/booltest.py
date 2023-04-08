print('1 : ',bool(0))
print('2 : ',bool(1))
print('3 : ',bool(-1))
print('4 : ',bool(-1523))
print('5 : ',bool([]))
print('6 : ',bool([0]))
print('7 : ',bool(None))
print('8 : ',bool(''))
print('9 : ',bool('hi'))

value = input('입력 : ') or '잉'
print(value)

a = 1 or 10 #1이 True로 1이 들어감
b = 0 or 10 #0이 false로 or 다음인 10도 확인 10이 true로 10 들어감
print('a:{}, b:{}'.format(a,b))
