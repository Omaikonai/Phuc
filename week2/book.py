# Class book
# Atributes: id, title, author, status
# Behaviors: print, edit_title, edit_author, update_status

class Book:
    # constructor: create an object with attributes set to values of parameters
    def __init__(self, id, title, author, status):
        self.id = id
        self.title = title
        self.author = author
        self.status = status
    
    def print(self):
        status = 'Available' if self.status else 'Not available'
        print(f'ID: {self.id}, Title: {self.title}, Author: {self.author}, Status: {status}')

    def edit_title(self, title):
        self.title = title

    def edit_author(self, author):
        self.author = author

    def update_status(self):
        self.status = not self.status

# Testing object
# create object by calling the constructor
book1 = Book(1, 'The Alchemist', 'Paulo Coelho', True)
# tell object to print (call method print)
book1.print()
book1.update_status()
book1.print()

book2 = Book(2, 'Harry Potter', 'J.K. Rowling', False)
book2.print()
book2.edit_author('Joanne Rowling')
book2.print()