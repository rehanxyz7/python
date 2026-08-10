class Car:
    def __init__(self,brand,model):
        Car.__brand = brand #making private and inaccessible directly to the users 
        Car.model = model

    def get__brand(self): #creating a get method to make private info accessible to user only if it is needed by them 
        return self.__brand 
    def fullname(self):
        return f"{self.__brand} {self.model}"

my_car = Car("Toyota","SUPREME")
print(my_car.fullname())
print(my_car.get__brand()) #to know the brand we need to actually call the get method to get the value