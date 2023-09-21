ids = []
names = []
prices = []
quantities = []

def run():
    running = True
    while running:
        print_menu()
        option = int(input('Enter your choice (0 to quit): '))
        do_task(option)
        running = option != 0

def print_menu():
    print('Product Management System')
    print('1. Add product')
    print('2. Edit product')
    print('3. Sell product')
    print('4. Show all products')

def do_task(option):
    if option == 1:
        add_product()
    elif option == 2:
        edit_product()
    elif option == 3:
        sell_product()
    elif option == 4:
        show_products()
    elif option == 0:
        print('Bye')

def add_product():
    id = input('Enter ID: ')
    name = input('Enter name: ')
    price = input('Enter price: ')
    quantity = input('Enter quantity: ')

    ids.append(id)
    names.append(name)
    prices.append(price)
    quantities.append(quantity)

    print('Product added successfully.')

def edit_product():
    id = input('Enter ID: ')
    position = search_by_id(id)
    if position == None:
        print('Product not found.')
        return
    
    print_product(position)

    name = input('Enter name: ')
    price = input('Enter price: ')
    quantity = int(input('Enter quantity: '))

    names[position] = name
    prices[position] = price
    quantities[position] = quantity

    print('Product updated successfully.')

def search_by_id(id):
    for i in range(len(ids)):
        if ids[i] == id:
            return i
    return None

def print_product(position):
    print(f'Name: {names[position]}, price: {prices[position]}, quantity: {quantities[position]}')

def sell_product():
    id = input('Enter ID: ')
    position = search_by_id(id)
    if position == None:
        print('Product not found.')
        return
    
    print_product(position)
    quantity = int(input('Enter quantity to sell: '))
    if quantity > int(quantities[position]):
        print('Not enough products.')
        return
    
    quantities[position] -= quantity
    print('Product sold successfully. Current quantity: ', quantities[position])

def show_products():
    print('Product list')
    for i in range(len(ids)):
        print_product(i)