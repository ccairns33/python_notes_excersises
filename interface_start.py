# Python Object Oriented Programming by Joe Marini course example
# Using Abstract Base Classes to implement interfaces

from abc import ABC, abstractmethod

class JSONify(ABC):
    @abstractmethod
    def toJSON(self):
        pass


class GraphicShape(ABC):
    def __init__(self):
        super().__init__()

    @abstractmethod
    def calcArea(self):
        pass


class Circle(GraphicShape, JSONify):
    # must define its own version of the toJSON method since it is an absract method
    def __init__(self, radius):
        self.radius = radius

    def calcArea(self):
        return 3.14 * (self.radius ** 2)

    def toJSON(self):
        return f"{{\" Circle\" : {str(self.calcArea())} }}"

c = Circle(10)
print(c.calcArea())
print(c.toJSON())
