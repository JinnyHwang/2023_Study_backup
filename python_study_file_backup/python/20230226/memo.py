
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

next()

iter()

'''










        
        

