# Observer Pattern Implementation in Python: A simple example demonstrating the Observer design pattern.
from abc import ABC, abstractmethod

# Bad Example: Tight coupling between subject and observers.
# class Sheet2:
#     def __init__(self):
#         self.total = 0

#     def calculate(self, values:list[float]):
#         sum = 0 
#         for value in values:
#             sum += value
#         self.total = sum
#         print(f"New Total: {self.total}")
#         return self.total

# class BarChart:
#     def render(self, values:list[float] ):
#         print(f"BarChart rendering with new values")

# class DataSource:
#     def __init__(self):
#         self.__values:list[float] = []
#         self.dependents:list[object] = []
    
#     @property 
#     def values(self) -> list[float]:
#         return self.__values
    
#     @values.setter
#     def values(self, new_values:list[float]):
#         self.__values = new_values
#         # update all dependents
#         for dependent in self.dependents:
#             if isinstance(dependent, Sheet2):
#                 dependent.calculate(self.__values)
#             elif isinstance(dependent, BarChart):
#                 dependent.render(self.__values)

#     def add_dependent(self, dependent:object):
#         self.dependents.append(dependent)
    
#     def remove_dependent(self, dependent:object):
#         self.dependents.remove(dependent)


# Good Example: Loose coupling using Observer pattern.
class Observer(ABC):
    @abstractmethod
    def update(self) -> None:
        pass

class Subject:
    def __init__(self):
        self.observers: list[Observer] = []
    
    def add_observer(self, observer:Observer):
        self.observers.append(observer)
    
    def remove_observer(self, observer:Observer):
        self.observers.remove(observer)
    
    def notify_observers(self):
        for observer in self.observers:
            observer.update()

class DataSource(Subject):
    def __init__(self):
        super().__init__()
        self.__values:list[float] = []
    
    @property 
    def values(self) -> list[float]:
        return self.__values
    
    @values.setter
    def values(self, new_values:list[float]):
        self.__values = new_values
        super().notify_observers()

class Sheet2(Observer):
    def __init__(self, data_source:DataSource):
        self.total = 0
        self.data_source = data_source

    def update(self) -> None:
        self.total = self.calculate(self.data_source.values)

    def calculate(self, values:list[float]):
        sum = 0 
        for value in values:
            sum += value
        self.total = sum
        print(f"New Total: {self.total}")
        return self.total

class BarChart(Observer):
    def __init__(self, data_source:DataSource):
        self.data_source = data_source

    def update(self):
        print(f"BarChart rendering with new values")

data_source = DataSource()
sheet2 = Sheet2(data_source)
bar_chart = BarChart(data_source)

data_source.add_observer(sheet2)
data_source.add_observer(bar_chart)

print(data_source.values)

data_source.values = [1,2,3,4,4.5]
