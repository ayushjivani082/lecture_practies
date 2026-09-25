from abc import ABC , abstractmethod

import math
# Abstract Class Shape

class Shape(ABC):

    @abstractmethod
    def area(self):
        pass

class Rectangle(Shape):
    def __init__(self , length , width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Circle(Shape):

    def __init__(self , radius):
        self.radius = radius

    def area(self):
        return self.radius * self.radius * math.pi

    def display(self):
        return f"{self.radius}"



class Triangle(Shape):

    def __init__(self , base , height):
        self.height = height
        self.base = base


    def area(self):
        return 1/2 * self.base * self.height


r = Rectangle(10 , 20)

print(r.area())

c = Circle(10)

print(round(c.area() , 2))

print(c.display())

t = Triangle(10 , 200)

print(t.area())