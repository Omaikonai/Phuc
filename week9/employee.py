class Employee:
    def __init__(self, name, age):
        self._name = name
        self._age = age
        self.BASIC = 1000
    
    def salary(self):
        return self.BASIC
    
    def show(self):
        print('Name:', self._name)
        print('Age:', self._age)
        print('Salary:', self.salary())

class FullTime(Employee):
    def __init__(self, name, age, rate):
        super().__init__(name, age)
        self._rate = rate
    
    def salary(self):
        return super().salary() * self._rate
    
    def show(self):
        super().show()
        print('Rate:', self._rate)

class PartTime(FullTime):
    def __init__(self, name, age, rate, days):
        super().__init__(name, age, rate)
        self.__days = days
    
    def salary(self):
        return super().salary() * self.__days / 5
    
    def show(self):
        super().show()
        print('Working days:', self.__days)

class Saler(Employee):
    def __init__(self, name, age, commission):
        super().__init__(name, age)
        self.__commission = commission
        self.__products = 0
    
    def salary(self):
        self.__products = int(input('Enter number of products: '))
        return (self.__products + self.BASIC) * self.__commission
    
    def show(self):
        super().show()
        print('Products sold:', self.__products)
        print('Commission:', self.__commission)