class Car:
    def __init__(self,brand,model):
        Car.brand = brand
        Car.model = model
    def fullname(self):
        return f"{self.brand} {self.model}"

my_car = Car("Toyota","SUPREME")
print(my_car.fullname())
print(my_car.brand)