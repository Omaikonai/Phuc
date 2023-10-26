class Car:
    def __init__(self, id, brand, model, price):
        self.__id = id
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__mileage = 0
    
    @property
    def id(self):
        return self.__id
    
    @property
    def brand(self):
        return self.__brand
    
    @property
    def model(self):
        return self.__model
    
    @property
    def price(self):
        return self.__price
    
    @price.setter
    def price(self, value):
        if value <= 0:
            print('Price must greater than 0')
            return
        self.__price = value

    def update_mileage(self, mile):
        if mile <= 0:
            print('Mileage must be positive.')
            return
        self.__mileage += mile
        print(f'Current mileage: {self.__mileage}')
    
    def show_info(self):
        print(f'Brand: {self.__brand}, Model: {self.__model}, Price: {self.__price}, Mileage: {self.__mileage}')