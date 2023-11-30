from shape import Shape

class Rectangle(Shape):
    def __init__(self, name='R', width=4.0, height=2.0):
        super().__init__(name)
        self._type = 'Rectangle'
        if width <= 0 or height <= 0:
            raise ValueError("Width and height must be positive")
        self._width = width
        self._height = height
    
    @property
    def width(self):
        return self._width
    
    @width.setter
    def width(self, value):
        if value <= 0:
            raise ValueError("Width must be positive")
        self._width = value
    
    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        if value <= 0:
            raise ValueError("Height must be positive")
        self._height = value
    
    def area(self):
        return self._width * self._height
    
    def __str__(self):
        super_info = super().__str__()
        super_info += f', width: {self._width:.2f}, height: {self._height:.2f}'
        super_info += f', area: {self.area():.2f}'
        return super_info