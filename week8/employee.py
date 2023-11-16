class Employee:
    def __init__(self, name, salary, age):
        try:
            salary = int(salary)
        except ValueError:
            raise ValueError('Salary must be an integer number')
        try:
            age = int(age)
        except ValueError:
            raise ValueError('Age must be an integer number')
        
        if name == '':
            raise ValueError('Name cannot be empty')
        if salary <= 0:
            raise ValueError('Salary must be positive')
        if age < 18 or age > 65:
            raise ValueError('Age must be in range [18, 65]')
        
        
        
        self.__name = name
        self.__salary = salary
        self.__age = age
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self, value):
        if value == '':
            raise ValueError('Name cannot be empty')
        self.__name = value

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, value):
        if value <= 0:
            raise ValueError('Salary must be positive')
        try:
            value = int(value)
        except ValueError:
            raise ValueError('Salary must be an integer number')
        
        self.__salary = value
    
    @property
    def age(self):
        return self.__age
    
    @age.setter
    def age(self, value):
        if value < 18 or value > 65:
            raise ValueError('Age must be in range [18, 65]')
        try:
            value = int(value)
        except ValueError:
            raise ValueError('Age must be an integer number')
        self.__age = value