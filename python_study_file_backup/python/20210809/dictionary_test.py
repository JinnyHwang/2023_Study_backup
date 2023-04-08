wintable = {
    '가위':'보',
    '바위':'가위',
    '보':'바위'
    }

#print(wintable['가위'])

def rsp(mine, yours) :
    if mine == yours :
        return 'draw'
    elif wintable[mine] == yours :
        return 'win'
    else :
        return 'lose'

result = rsp('가위', '보')

messages = {
    'win':'이겼다!',
    'lose':'졌다..ㅠ',
    'draw':'비겼다'
    }

print(messages[result])


#                ↓ 이름표는 문자열 또는 숫자를 주로 사용하지만
dict = {     "이름표"    :    [1,2,3] }
#                                ↑ 값은 리스트를 포함해서 무엇이든 올 수 있습니다.


numdict = { 'one':1, 'two':2}
numdict['four']=4
print(numdict)

del(numdict['two'])
print(numdict)

numdict.pop('one')
print(numdict)

#딕셔너리와 반복문
ages = {
    'Tod':35,
    'Jane':23,
    'Paul':62
    }

#keys()
for key in ages.keys() :
#    print(key)
    print('{}의 나이 : {}'.format(key, ages[key]))

#values()
for value in ages.values() :
    print(value)

#items()
for key, value in ages.items() :
    print('{}의 나이 : {}'.format(key, value))


dict1 = {1:100, 2:200}
dict2 = {1:10, 3:300}
#dict1.update(dict2)
#print(dict1)
dict2.update(dict1)
print(dict2)


tuple1 = (1, 2, 3)
print(type(tuple1))

list11 = [1, 2, 3]

tuple2 = tuple(list11)
print(tuple2)

tuple3 = 1, 2, 3
print(tuple3)

#튜플은 값을 변경하지 못한다

#packing , unpacking

a, b = 1, 2 #이것도 튜플이라 볼 수 있음
print('a : {}, b : {}'.format(a, b))

c = (3, 4)

#unpacking
d, e = c
print('c : {}, d : {}, e : {}'.format(c, d, e))

#packing
f = d, e
print('d : {}, e : {}, f : {}'.format(d, e, f))


x = 5
y = 10

# 두 값을 swap하려면?
x,y = y,x
print('x : {}, y : {}'.format(x, y))


x,y = y,x
print('x : {}, y : {}'.format(x, y))


def tuple_func():
    return 1, 2

q, w = tuple_func()
print('q : {}, w : {}'.format(q, w))


#함수의 리턴값으로 튜플 paking, unpackin 이용하기
list12 = [1, 2, 3, 4, 5]

for i, v in enumerate(list12):
    print('i:{}, v:{}'.format(i, v))

for a in enumerate(list12):
    print('i:{}, v:{}'.format(a[0], a[1]))


ages = {
    'Tod':35,
    'Jane':23,
    'Paul':62
    }

#튜플 key, value로 unpacking
for key, value in ages.items():
    print('{} 나이 : {}'.format(key, value))

#튜플 a로 packing
for a in ages.items():
    print('{} 나이 : {}'.format(*a))

