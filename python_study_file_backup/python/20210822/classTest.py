
class Human():
    '''인간'''
    def create(name, weight):
        person = Human()
        person.name = name
        person.weight = weight
        return person
    
    #인스턴스가 자동으로 첫번째 self에 적용
    def eat(self):
        self.weight += 0.1
        print('[eat] {}는 {}가 되었다.'.format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print('[walk] {}는 {}가 되었다.'.format(self.name, self.weight))
        
    def speak(self, message):
        print(message)


person = Human.create('지은', 56.5)
person.eat()
person.walk()
person.speak('Hi')


