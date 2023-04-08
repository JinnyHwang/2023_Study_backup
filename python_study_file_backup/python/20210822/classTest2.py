class Car():
    '''자동차'''
    def create(name):
        car = Car()
        car.name = name
        return car
        
    def run(self):
        print("{}가 달립니다.".format(self.name))

taxi = Car.create("택시")
#taxi.name = "택시"
taxi.run()