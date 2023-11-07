class Student:
    def __init__(self, id, name, grade):
        self.__id = id
        self.__name = name
        self.__grade = grade

    @property
    def id(self):
        return self.__id
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def grade(self):
        return self.__grade
    
    @grade.setter
    def grade(self, value):
        self.__grade = value