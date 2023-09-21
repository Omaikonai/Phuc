ids = []
names = []
ages = []

def run():
    running = True
    while running:
        print_menu()
        option = int(input('Enter your choice (0 to quit):'))
        do_task(option)
        running = option != 0

def print_menu():
    print('Student Management System')
    print('1. Add student')
    print('2. Search by ID')
    print('3. Edit student')
    print('4. Delete student')
    print('5. Show all students')

def do_task(option):
    if option == 1:
        add_student()
    elif option == 2:
        search_student()
    elif option == 3:
        edit_student()
    elif option == 4:
        delete_student()
    elif option == 5:
        show_students()
    elif option == 0:
        print('Bye')

def add_student():
    id = input('Enter ID:')
    name = input('Enter name:')
    age = input('Enter age:')

    ids.append(id)
    names.append(name)
    ages.append(age)

    print('Student added successfully.')

def search_student():
    id = input('Enter ID:')
    position = search_by_id(id)
    if position == None:
        print('Student not found.')
        return
    
    print_student(position)

def search_by_id(id):
    for i in range(len(ids)):
        if ids[i] == id:
            return i
    return None

def print_student(position):
    # TODO: print name, age at the corresponding position in names and ages
    print(f'Name: {names[position]}, age: {ages[position]}')

def edit_student():
    id = input('Enter ID:')
    position = search_by_id(id)

    if position == None:
        print('Student not found.')
        return
    
    # enter new name and age
    name = input('Enter new name:')
    age = input('Enter new age:')

    names[position] = name # update name at the corresponding position
    ages[position] = age # update age at the corresponding position

    print('Student updated successfully.')

def delete_student():
    id = input('Enter ID:')
    position = search_by_id(id)
    
    if position == None:
        print('Student not found.')
        return
    
    ids.pop(position)
    names.pop(position)
    ages.pop(position)

    print('Student deleted successfully.')

def show_students():
    for i in range(len(ids)):
        print_student(i)

### MAIN PROGRAM ###
run()