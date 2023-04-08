# 부모class
class Animal():
    def walk(self):
        print("걷기")
    def eat(self):
        print("먹기")
    def greet(self):
        print("인사한다")
        

# Animal 부모 class를 상속 받음
# 자식 class
class Human(Animal):
    def wave(self):
        print("손 흔들기")
        
    #오버라이드 새로운 정의로 덮어씀
    def greet(self): 
        self.wave()
        
class Dog(Animal):
    def wag(self):
        print("꼬리 흔들기")
    def greet(self):
        self.wag()
        
class Cow(Animal):
    '''소'''


person = Human()
person.greet()

dog = Dog()
dog.greet()

cow = Cow()
cow.greet()

