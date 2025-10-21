# Dependency Inversion Principle (DIP) states that high-level modules should not depend on low-level modules.
# Both should depend on abstractions (e.g., interfaces).
# Abstractions should not depend on details. Details (concrete implementations) should depend on    abstractions.

from abc import ABC, abstractmethod

# Bad Example:
class Engine:
    def start(self):
        print("Engine started")

class Car:
    def __init__(self):
        self.engine = Engine()  # High-level module depends on low-level module

    def start(self):
        self.engine.start()
        print("Car started")

# Good Example:
class Engine(ABC):
    @abstractmethod
    def start(self):
        pass 

class BasicEngine(Engine):
    def start(self):
        print("Basic Engine started")

class AdvancedEngine(Engine):
    def start(self):
        print("Advanced Engine started with turbo mode")

class Car:
    def __init__(self, engine:Engine):
        self.engine = engine # High-level module depends on low-level module

    def start(self):
        self.engine.start()
        print("Car started")


car = Car(BasicEngine())
car.start()
car2 = Car(AdvancedEngine())
car2.start()