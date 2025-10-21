# Composition: Involves creating complex objects by combining objects or components

class Engine:
    def start(self):
        return "Engine starting..."
class Wheels:
    def rotate(self):
        return "Wheels rotating..."
class Chassis:
    def support(self):
        return "Chassis supporting the vehicle..."  
class Seats:
    def sit(self):
        return "Seats providing comfort..."
    

class Car:
    def __init__(self):
        self.__engine = Engine()
        self.__wheels = Wheels()
        self.__chassis = Chassis()
        self.__seats = Seats()
        
    def drive(self):
        return (f"{self.__engine.start()}\n"
                f"{self.__wheels.rotate()}\n"
                f"{self.__chassis.support()}\n"
                f"{self.__seats.sit()}\n"
                "Car is now driving!")
car = Car()
print(car.drive())