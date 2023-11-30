import math
from shape import Shape

class Circle(Shape):
    def __init__(self, name='C', radius=1.0):
        super().__init__(name)
        self._type = 'Circle'
        if radius <= 0:
            raise ValueError("Radius must be positive")
        self._radius = radius
    
    @property
    def radius(self):
        return self._radius
    
    @radius.setter
    def radius(self, value):
        if value <= 0:
            raise ValueError("Radius must be positive")
        self._radius = value
    
    def area(self):
        return math.pi * self._radius ** 2
    
    def __str__(self):
        super_str = super().__str__()
        return f'{super_str}, radius: {self._radius:.2f}, area: {self.area():.2f}'