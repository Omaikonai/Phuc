class Student:
    def __init__(self, id, name, grade):
        self.__id = id
        if name == '':
            name = 'John Doe'
        
        self.__name = name

        if grade < 0:
            grade = 0
        elif grade > 10:
            grade = 10

        self.__grade = grade

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            value = 'John Doe'

        self.__name = value

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        if value < 0:
            value = 0
        elif value > 10:
            value = 10
            
        self.__grade = value