# Book Management System based on the given exercise and coding style

book_ids = ['1', '2', '3', '4', '5']
titles = ['Harry Potter', 'The Lord of the Rings', 'The Little Prince', 'The Da Vinci Code', 'The Alchemist']
authors = ['J.K. Rowling', 'J.R.R. Tolkien', 'Antoine de Saint-Exupéry', 'Dan Brown', 'Paulo Coelho']
statuses = [True, True, True, True, True]  # True is "available" or False is "not available"

def run():
    running = True
    while running:
        print_menu()
        option = int(input('Enter your choice (0 to quit): '))
        do_task(option)
        running = option != 0

def print_menu():
    print('Book Management System')
    print('1. Add a new book')
    print('2. Search by ID')
    print('3. Edit book details')
    print('4. Delete book')
    print('5. Show all books')
    print('6. Borrow a book')
    print('7. Return a book')
    print('8. Search by title')
    print('9. Sort by title')

    print('0. Quit')

def do_task(option):
    if option == 1:
        add_book()
    elif option == 2:
        search_book()
    elif option == 3:
        edit_book()
    elif option == 4:
        delete_book()
    elif option == 5:
        show_books()
    elif option == 6:
        borrow_book()
    elif option == 7:
        return_book()
    elif option == 8:
        search_title()
    elif option == 9:
        sort_title()
    elif option == 0:
        print('Bye')

def add_book():
    book_id = input('Enter Book ID:')
    if book_id in book_ids:
        print("This ID already exists.")
        return
    title = input('Enter book title:')
    author = input('Enter book author:')
    
    book_ids.append(book_id)
    titles.append(title)
    authors.append(author)
    statuses.append(True) # by default, a new book is available
    print('Book added successfully.')

def search_book():
    book_id = input('Enter Book ID:')
    position = search_by_id(book_id)
    if position is None:
        print('Book not found.')
        return
    print_book(position)

def search_by_id(book_id):
    for i in range(len(book_ids)):
        if book_ids[i] == book_id:
            return i
    return None

def search_title():
    title = input('Enter book title:')
    found_positions = search_by_title(title)
    if len(found_positions) == 0:
        print('No book found.')
        return
    for pos in found_positions:
        print_book(pos)

def search_by_title(title):
    found_positions = []
    for i in range(len(titles)):
        if title.strip().lower() in titles[i].strip().lower():
            found_positions.append(i)
    return found_positions

def print_book(position):
    status = 'Available' if statuses[position] else 'Not available'
    print(f'ID: {book_ids[position]}, Title: {titles[position]}, Author: {authors[position]}, Status: {status}')

def edit_book():
    book_id = input('Enter Book ID:')
    position = search_by_id(book_id)
    if position is None:
        print('Book not found.')
        return
    title = input('Enter new title:')
    author = input('Enter new author:')
    titles[position] = title
    authors[position] = author
    print('Book updated successfully.')

def delete_book():
    book_id = input('Enter Book ID:')
    position = search_by_id(book_id)
    if position is None:
        print('Book not found.')
        return
    book_ids.pop(position)
    titles.pop(position)
    authors.pop(position)
    statuses.pop(position)
    print('Book deleted successfully.')

def show_books():
    for i in range(len(book_ids)):
        print_book(i)

def borrow_book():
    book_id = input('Enter Book ID to borrow:')
    position = search_by_id(book_id)
    if position is None:
        print('Book not found.')
        return
    if statuses[position] == False:
        print('Book is already borrowed.')
        return
    statuses[position] = False
    print('Book borrowed successfully.')

def return_book():
    book_id = input('Enter Book ID to return:')
    position = search_by_id(book_id)
    if position is None:
        print('Book not found.')
        return
    if statuses[position] == True:
        print('Book is already available.')
        return
    statuses[position] = True
    print('Book returned successfully.')

def sort_title():
    for i in range(len(titles) - 1):
        j_min = i 
        for j in range(i + 1, len(titles)):
            if titles[j_min] > titles[j]:
                j_min = j
        if j_min != i:
            swap(i, j_min)

    for i in range(len(book_ids)):
        print_book(i)

def swap(i, j_min):
    book_ids[i], book_ids[j_min] = book_ids[j_min], book_ids[i]
    titles[i], titles[j_min] = titles[j_min], titles[i]
    authors[i], authors[j_min] = authors[j_min], authors[i]
    statuses[i], statuses[j_min] = statuses[j_min], statuses[i]
run()
