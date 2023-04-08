
str1 = "오늘은 날씨가 흐림"

# split()
str_list = str1.split()
print(str_list)

words = str1.split()

position = words.index('흐림')
print(position)

words[position] = '맑음'

restr = ' '.join(words)
print(restr)

# slice
txt = 'hello world'
print(txt[1:4])
print(txt[5:])
print(txt[:7])
print(txt[:])

rainbow = ["빨", "주", "노", "초", "파", "남", "보"]
red_colors = rainbow[:3]
print(red_colors)

blue_colors = rainbow[4:]
print(blue_colors)

def substring(str, start, end):
    try:
        return str[start:end]
    except Exception as ex:
        return 'ERROR : {}'.format(ex)

my_text = "Hello world"
between_2_5 = substring(my_text, 2, 5)
print(between_2_5)

between_fail = substring(my_text, 15.5, 5)
print(between_fail)


# step을 이용해서 slice한 값의 범위에서 step을 주어 건너뛰기
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(list1[::3])
print(list1[2:8:2])

# 0~19 list 생성
list1 = list(range(20))
print(list1)

new_list = list1[5:15:3]
print(new_list)

reverse_list = list1[17:4:-4]
print(reverse_list)

list1 = list(range(6))
print(list1)

# list1의 1부터 3까지를 slice를 이용해서 각각 11, 22, 33으로 바꿔보세요.
# 바꾸고 나면 list1은 [0, 11, 22, 33, 4, 5]가 되어야 합니다.
list1[1:4] = [11, 22, 33]
print(list1)

list2 = list(range(6))
print(list2)
# list2의 1부터 3까지를 del과 slice를 이용해서 지워보세요
# 바꾸고 나면 list2은 [0, 4, 5]가 되어야 합니다.
del(list2[1:4])
#list2.remove(100) #remove() 인자값을 삭제
print(list2)


# 자료형 확인
# type(변수명) 사용
s = 'Hello'
f = 3.14
i = 28
l = []
print(type(s))
print(type(f))
print(type(i))
print(type(l))

print(isinstance(3, int))
print(isinstance(3.0, int))
print(isinstance(3.14, float))

#isinstance() arg 2 must be a type or tuple of types
#위 error는 str로 변수 선언 같은걸 해서
#str 이름으로 로컬 변수에 할당된 변수가 존재
#type str로 인식하는 것이 아닌
#로컬변수 str로 인식
print(isinstance("HJE", str))


my_list = [1, 2, 3]
my_dict = {"풀": 800, "색연필": 3000}
my_tuple = (1, 2, 3)
number = 10
real_number = 3.141592

print(type(my_list)) #<class 'list'>
print(type(my_dict)) #<class 'dict'>
print(type(my_tuple)) #<class 'tuple'>
print(type(number)) #<class 'int'>
print(type(real_number)) #<class 'float'>


#클래스와 인스턴스 차이

characters = list('hello')
print(characters)

