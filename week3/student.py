class Student:
    def __init__(self, id, name, grade):
        self.id = id
        self.name = name
        self.grade = grade

    def show_info(self):
        print(f'ID: {self.id}, Name: {self.name}, Grade: {self.grade}')