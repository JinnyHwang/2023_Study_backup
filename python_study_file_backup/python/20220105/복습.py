
list1 = list('Hello')
list2 = list('Hello')

print(isinstance(list1, list))
print(isinstance(list2, list))

print(list1 == list2) # 값 비교
print(list1 is list2) # 인스턴스 비

list3 = list1
print(list3 is list1)

list1 = list(range(10))
list2 = [1, 2, 3]

if isinstance(list1, list) and isinstance(list2, list):
    print('YES')


class Human():
    '''사람'''
    
person1 = Human()
person2 = Human()

print(type(person1))

# 각 instance의 language attribute 정의
person1.language = 'Kor'
person2.language = 'Eng'

# person : object
# .language : attribute
def speak(person):
    try:
        print("{} 말하기".format(person.language))
    except Exception as ex:
        print('? : ',ex)

speak(person1)
speak(person2)
speak(list1)

# class method 정의
Human.speak = speak
person1.speak()

'''
https://kongdols-room.tistory.com/48

class : data와 기능을 함께 묶는 방법을 제공함
new class를 만드는 것 : 객체의 new type을 만들어서
해당 type의 new instance를 만들 수 있도록 함
각 class instance는 상태를 유지하기 위해, attribute, method를 가질 수 있음

attribute : 클래스내부의 변수나 함수에 접근
ClassName.AttributeName

instance : 클래스 type의 객체
InstanceName = ClassName # 선언 방법

'''

class Exam:
    # 닥스트링(Docstring)
    ''' Class Example '''
    
    # 클래스 객체와 인스턴스 객체가 동일한 주소를 가지는 변수, 리스트 객체
    a = 'class global variable'
    list1 = []
    
    # 인스턴스 객체를 만들 때 인자 값 2개를 입력받아
    # 인스턴스 객체 변수에 할당하도록 설정
    def __init__(self, input1, input2):
        '''Initialize some variables'''
        self.b = input1
        self.c = input2
        self.d = 5
        self.list2 = []

    # 클래스의 메서드 선언
    # 클래스에서 각 매서드의 처음 입력값은 self로 고정되어 있다
    # self는 인스턴스를 받아들인다는 의미
    # 문법적으로는 self를 사용하지 않아도 무방하지만,
    # 가독성 측면에서 사용하는 것 권장
    def list_append_method(self,v1,v2):
        '''Two lists are appended'''
        self.list1.append(v1)
        self.list2.append(v2)
        
'''클래스 __init__ 에서 정의한 attribute or 새로 선언한 attribute
사용법과 의미 숙지하기'''

class Car():
    '''Car'''

taxi = Car()
taxi.name = 'car1'























