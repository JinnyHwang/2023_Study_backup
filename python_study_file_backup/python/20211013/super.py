# 부모 동작 그대로하면서 새로운 동작 끼워넣기

# 부모class
class Animal():
    def __init__(self, name):
        self.name = name
        
    def walk(self):
        print("걷기")
    def eat(self):
        print("먹기")
    def greet(self):
        print("{}이/가 인사한다".format(self.name))
        

# Animal 부모 class를 상속 받음
# 자식 class
class Human(Animal):
    def __init__(self, name, hand):
        super().__init__(name)
        self.hand = hand
    
    def wave(self):
        print("{}손 흔들기".format(self.hand))
        
    #오버라이드 새로운 정의로 덮어씀
    def greet(self): 
        self.wave()
        super().greet()
        
person = Human("에이", "왼")
person.greet()
