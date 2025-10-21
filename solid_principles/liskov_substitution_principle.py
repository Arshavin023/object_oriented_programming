# Liskov Substitution Principle (LSP) states that objects of a superclass should be replaceable
# with objects of its subclasses without affecting the correctness of the program.
# This means that subclasses should extend the behavior of the superclass without changing its original functionality. 

from abc import ABC, abstractmethod

# Bad Example:
class Shape(ABC):
    @abstractmethod
    def area(self) -> float:
        pass

# class Rectangle(Shape):
#     def __init__(self, width: float=0.0, height: float=0.0):
#         self.__width = width
#         self.__height = height

#     @property 
#     def width(self) -> float:
#         return self.__width
    
#     @width.setter
#     def width(self, value: float):
#         self.__width = value 

#     @property
#     def height(self) -> float:
#         return self.__height
    
#     @height.setter
#     def height(self, value: float):
#         self.__height = value

#     def area(self) -> float:
#         return self.__width * self.__height

# class Square(Rectangle):
#     def __init__(self, side: float=0.0):
#         super().__init__(side, side)

#     @Rectangle.width.setter
#     def width(self, value: float):
#         self._Rectangle__width = value
#         self._Rectangle__height = value

#     @Rectangle.height.setter
#     def height(self, value: float):
#         self._Rectangle__height = value
#         self._Rectangle__width = value


# Good Example:
class Rectangle(Shape):
    def __init__(self, width: float=0.0, height: float=0.0):
        self.width = width
        self.height = height
    def area(self) -> float:
        return self.width * self.height

class Square(Shape):
    def __init__(self, side: float=0.0):
        self.side = side
    def area(self) -> float:
        return self.side**2

class Triange(Shape):
    def __init__(self, base: float=0.0, height: float=0.0):
        self.base = base
        self.height = height
    def area(self) -> float:
        return 0.5*(self.base*self.height)
    
# rectangle = Rectangle()
# rectangle.width = 5
# rectangle.height = 10
# print(f"Rectangle area expected 10*5=50: {rectangle.area()}")  # Output: Rectangle area: 50

# square = Square()
# square.side = 5
# print(f"Square area expected 5*5=25: {square.area()}")

# In the good example, both Rectangle and Square inherit from Shape and implement the area method.
# They can be used interchangeably without affecting the correctness of the program, thus adhering to the
# Liskov Substitution Principle.
square = Square()
square.side = 7
rectangle = Rectangle()
rectangle.width,rectangle.height=10,5
triange = Triange()
triange.base,triange.height=8,4

def return_area(shape:Shape) -> float:
    return shape.area() 

print(f"Rectangle area expected 10*5=50: {return_area(rectangle)}")  # LSP: Rectangle can be used wherever Shape is expected
print(f"Square area expected 7*7=49: {return_area(square)}")  # LSP: Square can be used wherever Shape is expected
print(f"Triangle area expected 0.5*8*4=16: {return_area(triange)}")
  # LSP: Square can be used wherever Rectangle is expected

