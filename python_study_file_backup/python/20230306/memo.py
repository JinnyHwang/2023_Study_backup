
l1 = [1,2,3]
s1 = [set() for _ in range(3)]
print(l1)
print(s1)

s1[0].update(l1)
print(s1)

for l in l1:
    s1[1].add(l)
print(s1)


# https://www.daleseo.com/python-global-nonlocal/
'''
전역변수 global
일반 함수 내에서 전역변수 값을 함수 내부에서 변경하고 싶을 때

비지역변수 nonlocal
중첩 함수 내에서 비지역변수 값을 중첩 함수 내부에서 변경하고 싶을 때
'''

# outer(), inner() 입장에서 전역(global) 범위

global_var = '전역 변수'

def outer():
    # outer() 입장에서 지역(local) 범위
    # inner() 입장에서 비지역(nonlocal) 범위
    global global_var #global 없이 선언시 outer()의 지역변수로 생성됨
    
    nonlocal_var = '비전역 변수'
    print(global_var) #ok
    print(nonlocal_var) #ok
    
    def inner():
        # inner() 입장에서 지역(local) 범위
        global global_var
        nonlocal nonlocal_var #nonlocal 없이 선언 시 inner()의 지역변수로 생성됨
        
        local_var = '지역 변수'
        print(global_var) #ok
        print(nonlocal_var) #ok
        print(local_var) #ok
    
    print(local_var) #fail : not defined
        
print(nonlocal_var) #fail : not defined
print(local_var) #fail : not defined
        
        

'''
https://dojang.io/mod/page/view.php?id=2408

next() iter()

iter는 객체의 __iter__ 메서드 호출
next는 객체의 __next__ 메서드 호출
'''

'''
반복 가능한 객체에서 __iter__ 호출하고
이터레이터에서 __next__ 메서드 호출

iter()는 반복 가능한 객체에서 이터레이터를 반환
next()는 이터레이터에서 값을 차례대로 꺼냄
'''
it = iter(range(3))
print(next(it)) # 0
print(next(it)) # 1
print(next(it)) # 2
print(next(it)) # StopIteration


'''
iter()는 반복을 끝낼 값을 지정하면 특정 값이 나올 때 반복을 끝냄
이 경우 반복 가능한 객체 대신 호출 가능한 객체(callable)를 넣어줌
반복을 끝낼 값은 sentinel(감시병)

iter(호출가능한객체, 반복을끝낼값)
random.randint(0,5)를 사용해서 0~5 무작위 숫자 생성하면서 2가 나오면 반복을 끝내도록 설정 가능
'''
import random
it = iter(lambda:random.randint(0,5),2)
print(next(it)) # 0
print(next(it)) # 5
print(next(it)) # 0
print(next(it)) # 2 : StopIteration


'''
next() 기본값을 지정할 수 있음
기본값을 지정하면 반복이 끝나도 StopIteration 발생하지 않고 기본값 출력
반복할 수 있을 때는 해당 값을 출력,
반복이 끝나면 기본값 출력

next(반복가능한객체, 기본값)
'''
it = iter(range(3))
print(next(it, 10)) # 0
print(next(it, 10)) # 1
print(next(it, 10)) # 2
print(next(it, 10)) # 10
print(next(it, 10)) # 10


        
        

