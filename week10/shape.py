from abc import ABC, abstractmethod

# To make Shape an abstract class, we inherit it from ABC
class Shape(ABC):
    def __init__(self, name):
        if name == "":
            raise ValueError("Name cannot be empty")
        self._name = name
        self._type = 'Shape'

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        if value == "":
            raise ValueError("Name cannot be empty")
        self._name = value
    
    @property
    def type(self):
        return self._type
    
    # To make area an abstract method, we use the decorator @abstractmethod
    @abstractmethod
    def area(self):
        pass

    def __str__(self):
        return f'{self._type}: {self._name}'