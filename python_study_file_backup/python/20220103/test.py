days_in_month = {"1월":31, "2월":28, "3월":31, "4월":30, "5월":31}

for key in days_in_month.keys():
    print(key)

for value in days_in_month.values():
    print(value)
    
for month, day in days_in_month.items():
    print("{} {}".format(month, day))

for i, key in enumerate(days_in_month):
    print('{} {} {}'.format(i+1, key, days_in_month[key]))


def check_and_clear(box):
    for key1 in box.keys():
        if key1 == '불량품':
            box.clear()
            return


box1 = {"불량품" : 10}
check_and_clear(box1)
# {}가 출력되어야합니다.
print(box1)

box2 = {"정상품": 10}
check_and_clear(box2)
# {"정상품": 10}가 출력되어야합니다.
print(box2)

# dictionary 합치기
products = {"풀":800, "딱풀":1200, "색종이":1000,"색연필":5000,"스케치북":3500}
catalog = {"겨울용 실내화":12000, "잠자리채":8000, "딱풀":1400}

products.update(catalog)

tuple1 = (1, 2, 3)
tuple2 = 1, 2, 3
list1 = [1, 2, 3]
tuple3 = tuple(list1)

if tuple1 == tuple2 == tuple3:
    print('yes')


tuple1 = (11, 22, 33)
for i in tuple1:
    print(i)
    
for i in range(len(tuple1)):
    print(tuple1[i])

for i, t in enumerate(tuple1):
    print('{} {} {}'.format(i, t, tuple1[i]))


a = 3
b = 5
c = a, b #튜플
print(c)
a, b = b, a
print(a, b)

products = {"풀" : 800, "색종이": 1000}

for key, value in products.items():
    print(key, value)
    
for i in products.items():
    print('{} {}'.format(*i))


numbers = [1,2,3]
length = len(numbers)
i = 0

while i < length:
    print(numbers[i])
    i = i+1


sizes = [33,35,34,37,32,35,39,32,35,29]

for i, s in enumerate(sizes):
    if s == 32:
        print('index : ',i)
        break

numbers = [(1, 2), (10, 0),(3,2)]

for a, b in numbers:
    if b == 0:
        print('nope')
        continue
    print(a/b)

try:
    print(3/0)
#except Exception:
except ZeroDivisionError:
    print('발생 : ZeroDivisionError')

try:
    print(3/0)
except Exception as ex:
    print('어떤에러?',ex)


shops = {
    "송일문방구": {"가위": 500, "크레파스": 3000},
    "알파문구": {"풀": 800, "도화지": 300, "A4용지": 8000},
    "다이소": {"풀": 500, "목공본드": 2000, "화분": 3000}
}

for k, v in shops.items():
    for item in v.keys():
        if item == '풀':
            print("{} 문구점에 {}이 {}원".format(k, item, v[item]))
print('\n')

try:
    for k1, v1 in shops.items():
        for k2, v2 in v1.items():
            if k2 == '풀':
                print('{} {} {}'.format(k1, k2, v2))
                raise StopIteration
                raise ZeroDivisionError

except ZeroDivisionError :
    print('풀 파는 곳 찾았으니까 끝')
except StopIteration :
    print('error2')
    
    
if []: #F
    print('T')
else:
    print('F')
    
if [1, 2, 3]: #T
    print('T')
else:
    print('F')
    
if {}: #F
    print('T')
else:
    print('F')
    
if {'A':22}: #T
    print('T')
else:
    print('F')
    
if 0: #F
    print('T')
else:
    print('F')

if 1: #T
    print('T')
else:
    print('F')
    
# or연산의 결과는 앞의 값이 True이면 앞의 값을,
# 앞의 값이 False이면 뒤의 값을 따릅니다.
a = 0 or 10
b = 1 or 10

print("a:{} b:{}".format(a, b))
    

def safe_index(list1, value1):
    
    try:
        return list1.index(value1)
    except Exception as ex:
        print('예외: ',ex)
        return None
    
print(safe_index([1,2,3,4,5], 5))
print(safe_index([1,2,3], 5))


list1 = [1, 2, 3, 4]

#list1의 1번째 자리에 8을 넣고 원래 있던 값은 오른쪽으로 밀어 보세요
list1.insert(0, 8)
print(list1)
    
#list1을 작은 수부터 큰 수로 정렬해 보세요
list1.sort()
print(list1)

list1.sort(reverse=True)
print(list1)

list1.sort()
list1.reverse()
print(list1)

    
    
    
    
    