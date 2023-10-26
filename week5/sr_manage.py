from car import Car
from show_room import ShowRoom

class ShowRoomManagement:
    def __init__(self):
        name = input('Enter show room name: ')
        self.__showrooms = ShowRoom(name) # create an emtpy ShowRoom object

    def run(self):
        running = True
        while running:
            self.__print_menu()
            choice = int(input('Enter your choice: '))
            self.__do_task(choice)
            running = choice != 0

    def __print_menu(self):
        print(f'Show room management for {self.__showrooms.name}')
        print('1. Add car')
        print('2. Remove car')
        print('3. Show all cars')
        print('4. Update price')
        print('0. Exit')

    def __do_task(self, choice):
        if choice == 1:
            self.__add_car()
        elif choice == 2:
            self.__remove_car()
        elif choice == 3:
            self.__show_all()
        elif choice == 4:
            self.__update_price()
        elif choice == 0:
            print('Exiting...')
        else:
            print('Invalid choice')
    
    def __add_car(self):
        id = int(input('Enter car id: '))
        brand = input('Enter brand: ')
        model = input('Enter model: ')
        price = int(input('Enter price: '))

        car = Car(id, brand, model, price)
        self.__showrooms.add_car(car)

    def __remove_car(self):
        id = int(input('Enter car id: '))
        self.__showrooms.remove_car(id)
    
    def __show_all(self):
        self.__showrooms.show_all()
    
    def __update_price(self):
        id = int(input('Enter car id: '))
        new_price = int(input('Enter new price: '))
        self.__showrooms.update_price(id, new_price)

## End of ShowRoomManagement class

if __name__ == '__main__':
    app = ShowRoomManagement()
    app.run()