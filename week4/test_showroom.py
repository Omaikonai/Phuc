from show_room import ShowRoom
from car import Car

cx5 = Car(1, 'Honda', 'CX5', 10000)
kona = Car(2, 'Hyundai', 'Kona', 20000)
tucson = Car(3, 'Hyundai', 'Tucson', 30000)

best_cars = ShowRoom('Hanoi Best Cars')
best_cars.add_car(cx5)
best_cars.add_car(kona)
best_cars.add_car(tucson)

best_cars.show_all()

best_cars.remove_car(2)
best_cars.show_all()

best_cars.remove_car(10)
