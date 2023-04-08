# 부모class
class Animal():
    def walk(self):
        print("걷기")
    def eat(self):
        print("먹기")

# Animal 부모 class를 상속 받음
# 자식 class
class Human(Animal):
    def wave(self):
        print("손 흔들기")
        
class Dog(Animal):
    def wag(self):
        print("꼬리 흔들기")

person = Human()
person.walk()
person.eat()
person.wave()

dog = Dog()
dog.walk()
dog.eat()
dog.wag()
