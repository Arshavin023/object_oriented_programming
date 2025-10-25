# Prototype Pattern Implementation in Python
from abc import ABC, abstractmethod

# # Bad example: Cloning without a prototype pattern.
# class Shape(ABC):
#     @abstractmethod
#     def draw(self):
#         pass

# class Circle(Shape):
#     def __init__(self):
#         self.radius = 5
#     def draw(self):
#         print(f"Drawing a circle with radius {self.radius}")

# class Rectangle(Shape):
#     def __init__(self):
#         self.height = 10
#         self.width = 5
#     def draw(self): 
#         print(f"Drawing a rectangle with side {self.height} and {self.width}")

# class ShapeActions:
#     def duplicate(self, shape: Shape):
#         if isinstance(shape, Circle):
#             new_circle = Circle()
#             new_circle.radius = shape.radius
#             new_circle.draw()
#         elif isinstance(shape, Rectangle):
#             new_rectangle = Rectangle()
#             new_rectangle.height = shape.height
#             new_rectangle.width = shape.width
#             new_rectangle.draw()
#         else:
#             raise ValueError("Unknown shape type")
        
# new_circle = Circle()
# new_circle.draw()
# new_circle.radius = 15
# new_circle.draw()
# new_rectangle = Rectangle()
# new_rectangle.draw()
# new_rectangle.height = 20
# new_rectangle.width = 10
# new_rectangle.draw()
# shape_actions = ShapeActions()
# print("Duplicating shapes without prototype pattern:")
# shape_actions.duplicate(new_circle)
# shape_actions.duplicate(new_rectangle)


# Good example: Cloning with a prototype pattern.
class Shape(ABC):
    @abstractmethod
    def draw(self):
        pass

    @abstractmethod
    def duplicate(self) -> 'Shape':
        pass
    
class Circle(Shape):
    def __init__(self, radius:float):
        self.radius = radius
    def draw(self):
        print(f"Drawing a circle with radius {self.radius}")
    def duplicate(self):
        new_circle = Circle(self.radius)
        return new_circle

class Rectangle(Shape):
    def __init__(self, width:float, height:float):
        self.height = width
        self.width = height
    def draw(self): 
        print(f"Drawing a rectangle with side {self.height} and {self.width}")
    def duplicate(self):
        new_rectangle = Rectangle(self.width, self.height)
        return new_rectangle

class Triangle(Shape):
    def __init__(self, base:float, height:float):
        self.base = base
        self.height = height
    def draw(self):
        print(f"Drawing a triangle with base {self.base} and height {self.height}")
    def duplicate(self):
        new_triangle = Triangle(self.base, self.height)
        return new_triangle

class Cylinder(Shape):
    def __init__(self, radius:float, height:float):
        self.radius = radius
        self.height = height
    def draw(self):
        print(f"Drawing a cylinder with radius {self.radius} and height {self.height}")
    def duplicate(self):
        new_cylinder = Cylinder(self.radius, self.height)
        return new_cylinder
    
class ShapeActions:
    def duplicate(self, shape: Shape):
        new_shape = shape.duplicate()
        new_shape.draw()

new_circle = Circle(15)
new_circle.draw()
new_rectangle = Rectangle(20, 10)
new_rectangle.draw()
new_triangle = Triangle(10, 5)
new_triangle.draw()
new_cylinder = Cylinder(7, 14)
new_cylinder.draw()
shape_actions = ShapeActions()
print("Duplicating shapes with prototype pattern:")
shape_actions.duplicate(new_circle)
shape_actions.duplicate(new_rectangle)
shape_actions.duplicate(new_triangle)
shape_actions.duplicate(new_cylinder)
