class Student:
    def __init__(self, id, name, math, english):       
        self.id = id
        if name == '':
            self.name = 'John Doe'
        else:
            self.name = name
        if math < 0 or math > 100:
            self.math = 0
        else:
            self.math = math
        if english < 0 or english > 100:
            self.english = 0
        else:
            self.english = english
    
    def show(self):
        print(f'ID: {self.id}, Name: {self.name}, Math: {self.math}, English: {self.english}')
        print(f'Average grade:', self.average_grades())
    
    def edit_name(self, name):
        if name == '':
            print('Name cannot be empty')
            return
        self.name = name
    
    def edit_grades(self, math, english):
        if math < 0 or math > 100 or english < 0 or english > 100:
            print('Grades must be in range [0, 100]')
            return
        self.math = math
        self.english = english
    
    def average_grades(self):
        avg = (self.math + self.english) / 2
        return avg


#### Test class Student
john = Student(1, 'John Lennon', 80, 90)
john.show()

john.edit_name('John Yoko Lennon')
john.edit_grades(85, 70)
john.show()