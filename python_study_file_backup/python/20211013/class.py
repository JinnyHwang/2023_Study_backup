class Human():
    def walk(self):
        print("걷기")
    def eat(self):
        print("먹기")
    def wave(self):
        print("손 흔들기")
        
class Dog():
    def walk(self):
        print("걷기")
    def eat(self):
        print("먹기")
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