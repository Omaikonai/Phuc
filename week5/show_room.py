from car import Car

class ShowRoom:
    def __init__(self, name):
        self.__name = name
        self.__cars = []

    @property
    def name(self):
        return self.__name
    
    def add_car(self, car):
        self.__cars.append(car)
        print(f'Added car {car.brand} - {car.model} successfully')
    
    def remove_car(self, id):
        car = self.__find(id)
        if car is None:
            print(f'Car with id {id} not found')
            return
        
        self.__cars.remove(car)
        print(f'Removed car id {car.id} successfully')

    def __find(self, id):
        for c in self.__cars:
            if c.id == id:
                return c
        return None

    def show_all(self):
        print(f'Showing all cars in show room {self.__name}')
        for c in self.__cars:
            c.show_info()
        
    def update_price(self, id, new_price):
        car = self.__find(id)
        if car is None:
            print(f'Car with id {id} not found')
            return
        car.price = new_price
        print(f'Updated price of car id {car.id} successfully')