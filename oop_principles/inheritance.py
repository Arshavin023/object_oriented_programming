# Inheritance: It's a fundamental concept in OOP where a new class (child class) 
# can inherit attributes and methods from an existing class (parent class). 
# This promotes code reusability and establishes a hierarchical relationship between classes.  

class Vehicle:
    def __init__(self, make:str, model:str, year:int):
        self.make = make
        self.model = model
        self.year = year

    def start(self):
        return f"The engine of the {self.make} {self.model} is starting."

    def stop(self):
        return f"The engine of the {self.make} {self.model} is stopping."

class Car(Vehicle):
    def __init__(self, make:str, model:str, year:int, 
                 num_of_doors:int, num_of_wheels:int=4):
        super().__init__(make, model, year)
        self.num_of_doors = num_of_doors

    def open_trunk(self):
        return f"The trunk of the {self.make} {self.model} is now open."

class Motorcycle(Vehicle):
    def __init__(self, make:str, model:str, year:int, num_of_wheels:int,
                 has_sidecar:bool=False):
        super().__init__(make, model, year)
        self.has_sidecar = has_sidecar
        self.num_of_wheels = num_of_wheels

    def pop_wheelie(self):
        return f"The {self.make} {self.model} is popping a wheelie!"
    
# Example usage:    
my_car = Car("Toyota", "Camry", 2007, 4)
print(my_car.__dict__)
print(my_car.start())
print(my_car.open_trunk())
print(my_car.stop())

my_bike = Motorcycle("Jinjeng", "Toyota", 2019, 2)
print(my_bike.__dict__) 
print(my_bike.start())
print(my_bike.pop_wheelie())
print(my_bike.stop())