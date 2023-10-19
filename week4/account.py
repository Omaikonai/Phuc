class Account():
    def __init__(self, id, name):
        self.__id = id
        self.__name = name # should validate name is not empty
        self.__balance = 0 # should validate balance is not negative
    
    def get_id(self):
        return self.__id
    
    def get_name(self):
        return self.__name
    
    def set_name(self, name):
        self.__name = name
    
    def get_balance(self):
        return self.__balance
    
    def withdraw(self, amount):
        if amount <= 0:
            print("Amount must be positive")
            return
        
        if amount > self.__balance:
            print("Insufficient balance")
            return
        
        self.__balance -= amount
        print(f'Withdraw {amount} successfully. Current balance: {self.__balance}')
    
    def deposit(self, amount):
        if amount <= 0:
            print("Amount must be positive")
            return
        
        self.__balance += amount
        print(f'Deposit {amount} successfully. Current balance: {self.__balance}')
    
    def show_info(self):
        print(f'Account: {self.__id}, Name: {self.__name}, Balance: {self.__balance}')