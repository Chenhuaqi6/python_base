class CarStore(object):

    def __init__(self):
        self.factory = Factory()

    def order(self,car_type):
        return self.factory.your_car(car_type)
class Factory(object):
    def your_car(self,car_type):
        if car_type == "保时捷":
            return Baoshijie()
        elif car_type == "宝马":
            return Bmw("宝马")
        elif car_type == "ix35":
            return Ix35()


class Car(object):
    def __init__(self,new_name):
        self.name = new_name

    def move(self):
        print(self.name,"在移动...")
    def music(self):
        print(self.name,"在播放音乐")
    def stop(self):
        print(self.name,"正在停下")
class Baoshijie(Car):
    pass
class Bmw(Car):
    pass
class Ix35(Car):
    pass

car_store = CarStore()
car = car_store.order("宝马")
car.move()
car.music()
car.stop()