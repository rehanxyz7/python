class Car:
    def __init__(self,brand,model):
        Car.brand = brand
        Car.model = model

my_car = Car("Toyota","SUPREME")
print(my_car.brand)