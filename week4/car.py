class Car:
    def __init__(self, brand, model, price):
        self.__brand = brand
        self.__model = model
        self.__price = price
        self.__mileage = 0
    
    def get_brand(self):
        return self.__brand
    
    def get_model(self):
        return self.__model
    
    def get_price(self):
        return self.__price
    
    def get_mileage(self):
        return self.__mileage
    
    def set_price(self, price):
        if price <= 0:
            print('Price must be positive.')
            return
        self.__price = price

    def update_mileage(self, mile):
        if mile <= 0:
            print('Mileage must be positive.')
            return
        self.__mileage += mile
        print(f'Current mileage: {self.__mileage}')
    
    def show_info(self):
        print(f'Brand: {self.__brand}, Model: {self.__model}, Price: {self.__price}, Mileage: {self.__mileage}')