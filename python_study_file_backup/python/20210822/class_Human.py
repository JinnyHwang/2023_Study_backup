
class Human():
    '''인간'''

def create_human(name, weight):
    person = Human()
    person.name = name
    person.weight = weight
    return person

#Human class에 function 추가
Human.create = create_human

person = Human.create('지은', 55)

def eat(person):
    person.weight += 0.1
    print('[eat] {}는 {}가 되었다.'.format(person.name, person.weight))

def walk(person):
    person.weight -= 0.1
    print('[walk] {}는 {}가 되었다.'.format(person.name, person.weight))

Human.eat = eat
Human.walk = walk

person.walk()
person.walk()
person.walk()
person.eat()


