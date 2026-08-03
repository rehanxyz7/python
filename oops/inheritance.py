
class Car: #Class gives the blueprint that is available for creating object . object has its own arguments which retrieves values from the class created 
    def __init__(self,brand,model):
        Car.brand = brand
        Car.model = model


    def fullname(self):
        return f"{self.brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        super().fullname()
        self.battery_size = battery_size

my_tesla = ElectricCar("Tesla","Model S","85kwh") #we have created a object passing arguments to the class we can create 'n' number of objects out of a given class 
print(my_tesla.brand)
print(my_tesla.model)
print(my_tesla.battery_size)