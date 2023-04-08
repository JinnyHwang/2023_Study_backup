
class Human():
    '''인간'''
    # __func__ : 특별한 함수
    # 인스턴스 생성시 자동 실행
    def __init__(self, name, weight):
        '''초기화 함수'''
        print('__init__실행')
        self.name = name
        self.weight = weight
        print('이름 : {}, 몸무게 : {}'.format(name, weight))
        
    #인스턴스를 print할 때 어떤 포맷으로 정보를 표시해줄지 정의
    def __str__(self):
        '''문자열화 함수'''
        return "{} (몸무게 {}kg)".format(self.name, self.weight)
        
#    def create(name, weight):
#        person = Human()
#        person.name = name
#        person.weight = weight
#        return person
    
    #인스턴스가 자동으로 첫번째 self에 적용
    def eat(self):
        self.weight += 0.1
        print('[eat] {}는 {}가 되었다.'.format(self.name, self.weight))

    def walk(self):
        self.weight -= 0.1
        print('[walk] {}는 {}가 되었다.'.format(self.name, self.weight))
        
    def speak(self, message):
        print(message)

person = Human('Jin', 60)
print(person)
print(person.name)
print(person.weight)