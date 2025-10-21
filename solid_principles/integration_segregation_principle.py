# Interface Segregation Principle (ISP) Example
# states that no client should be forced to depend on methods it does not use.
# This means that larger interfaces should be split into smaller, more specific ones
# so that clients only need to know about the methods that are of interest to them. 

from abc import ABC, abstractmethod
import math

# # Bad Example:
# class Shape(ABC):
#     @abstractmethod
#     def area(self) -> float:
#         pass

#     @abstractmethod
#     def volume(self) -> float:
#         pass

# class Circle(Shape):
#     def __init__(self, radius: float):
#         self.radius = radius

#     def area(self) -> float:
#         return round(math.pi * (self.radius ** 2),4)

#     def volume(self) -> float:
#         raise NotImplementedError("Circle does not have volume")

# class Sphere(Shape):
#     def __init__(self, radius: float):
#         self.radius = radius

#     def area(self) -> float:
#         return round(4 * math.pi * (self.radius ** 2),4)

#     def volume(self) -> float:
#         return round((4/3) * math.pi * (self.radius ** 3),4)
    
# circle=Circle(radius=5)
# print(f"Circle area: {circle.area()}")
# print(f"Circle volume: {circle.volume()}")  # This will raise an error  

# sphere = Sphere(radius=5)
# print(f"Sphere area: {sphere.area()}")
# print(f"Sphere volume: {sphere.volume()}")


# Good Example:
class Shape3D(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

    @abstractmethod
    def volume(self) -> float:
        pass

class Shape2D(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

class Circle(Shape2D):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return round(math.pi * (self.radius ** 2),4)

class Sphere(Shape3D):
    def __init__(self, radius: float):
        self.radius = radius

    def area(self) -> float:
        return round(4 * math.pi * (self.radius ** 2),4)

    def volume(self) -> float:
        return round((4/3) * math.pi * (self.radius ** 3),4)
    
circle=Circle(radius=5)
print(f"Circle area: {circle.area()}")

sphere = Sphere(radius=5)
print(f"Sphere area: {sphere.area()}")
print(f"Sphere volume: {sphere.volume()}")