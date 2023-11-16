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