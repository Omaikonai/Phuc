from student import Student

students = [] # empty list of Student objects

def main():
    running = True
    while running:
        print_menu()
        choice = int(input('Enter your choice: '))
        do_task(choice)
        running = choice != 0

def print_menu():
    print('Student Management System')
    print('1. Add student')
    print('2. Search by ID')
    print('3. Edit student')
    print('4. Show all students')

def do_task(choice):
    if choice == 1:
        add_student()
    elif choice == 2:
        search_by_id()
    elif choice == 3:
        edit_student()
    elif choice == 4:
        show_students()
    elif choice == 0:
        print('Bye')

def add_student():
    id = input('Enter student ID: ')
    name = input('Enter student name: ')
    grade = float(input('Enter student grade: '))
    # create student object
    st = Student(id, name, grade)
    # add student object to list
    students.append(st)

def search_by_id():
    id = input('Enter student ID to search: ')
    for st in students:
        if st.id == id:
            print('Student found.')
            st.show_info()
            return
    print(f'Not found any student with ID {id}.')

def edit_student():
    id = input('Enter student ID to search: ')
    for st in students:
        if st.id == id:
            new_name = input('Enter new name: ')
            new_grade = float(input('Enter new grade: '))
            st.name = new_name
            st.grade = new_grade
            print('Student updated.')
            return
    print(f'Not found any student with ID {id}.')

def show_students():
    print('All student information:')
    for st in students:
        st.show_info()

#### MAIN PROGRAM ####
main()