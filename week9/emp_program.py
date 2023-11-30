from employee import Employee, FullTime, PartTime, Saler

john = Employee('John', 20)
john.show()

paul = FullTime('Paul', 20, 1.4)
paul.show()

mike = PartTime('Mike', 22, 1.2, 3)
mike.show()

anna = Saler('Anna', 33, 0.1)
anna.show()