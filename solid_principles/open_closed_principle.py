# Open/Closed Principle (OCP) states that software entities (classes, modules, functions, etc.) 
# should be open for extension but closed for modification.
# This means that you should be able to add new functionality without changing existing code.   

# from enum import Enum
import math
from abc import ABC, abstractmethod

# Bad Example:
# class ShapeType(Enum):
#     CIRCLE = 'circle'
#     RECTANGLE = 'rectangle'

# class Shape:
#     def __init__(self, shape_type:ShapeType, radius: float = 0, 
#                  height: float = 0, width: float = 0):
#         self.type = shape_type
#         self.height = height
#         self.width = width
#         self.radius = radius

#     def calculate_area(self) -> float:
#         if self.type == ShapeType.CIRCLE:
#             return round(math.pi * (self.radius ** 2),4)
#         elif self.type == ShapeType.RECTANGLE:
#             return self.height * self.width
#         else:
#             raise ValueError("Unknown shape type")
# circle = Shape(ShapeType.CIRCLE, radius=5)
# rectangle = Shape(ShapeType.RECTANGLE, height=4, width=6)

# print(f"Calculate area: {circle.calculate_area()}") 
# print(f"Calculate area: {rectangle.calculate_area()}") 

# Good Example:
class Shape(ABC):
    @abstractmethod
    def calculate_area(self) -> float:
        pass

class Circle(Shape):
    def __init__(self, radius: float):
        self.radius = radius
    def calculate_area(self) -> float:
        return round(math.pi * (self.radius ** 2),4)

class Rectangle(Shape):
    def __init__(self, height: float, width: float):
        self.height = height
        self.width = width  
    def calculate_area(self) -> float:
        return self.height * self.width

class Triangle(Shape):
    def __init__(self, base: float, height: float):
        self.base = base
        self.height = height  
    def calculate_area(self) -> float:
        return 0.5 * self.base * self.height
# Now we can add new shapes without modifying existing code

circle = Circle(radius=5)
rectangle = Rectangle(height=4, width=6)
triangle = Triangle(base=4, height=5)

print(f"Calculate area of Circle: {circle.calculate_area()}") 
print(f"Calculate area of Rectangle: {rectangle.calculate_area()}") 
print(f"Calculate area of Triangle: {triangle.calculate_area()}")