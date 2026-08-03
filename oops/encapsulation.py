class Car:
    def __init__(self,brand,model):
        Car.__brand = brand #making private and inaccessible directly to the users 
        Car.model = model

    def get__brand(self):
        return self.__brand 
    def fullname(self):
        return f"{self.__brand} {self.model}"

my_car = Car("Toyota","SUPREME")
print(my_car.fullname())
print(my_car.get__brand())