from shape import Shape
from circle import Circle
from rectangle import Rectangle

class ShapeManagement:
    def __init__(self):
        self.__shapes = []
    
    def run(self):
        running = True
        while running:
            self.__print_menu()
            choice = int(input('Enter your choice: '))
            self.__do_task(choice)
            running = choice != 0
    
    def __print_menu(self):
        print('1. Add circle')
        print('2. Add rectangle')
        print('3. Show all shapes')
        print('4. Quit')
    
    def __do_task(self, choice):
        if choice == 1:
            self.add_circle()
        elif choice == 2:
            self.add_rectangle()
        elif choice == 3:
            self.show_all()
        elif choice == 4:
            print('Exiting...')
        else:
            print('Invalid choice')
    
    def add_circle(self):
        name = input('Enter circle name: ')
        radius = float(input('Enter circle radius: '))
        c = Circle(name, radius)
        self.__shapes.append(c)
        print(f'Added {c}')
    
    def add_rectangle(self):
        name = input('Enter rectangle name: ')
        width = float(input('Enter rectangle width: '))
        height = float(input('Enter rectangle height: '))
        r = Rectangle(name, width, height)
        self.__shapes.append(r)
        print(f'Added {r}')
    
    def show_all(self):
        for shape in self.__shapes:
            print(shape)

## MAIN ##

program = ShapeManagement()
program.run()