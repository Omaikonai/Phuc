from account import Account

acc01 = Account(1, 'John')
acc01.deposit(100)
acc01.withdraw(50)
acc01.show_info()

acc01.withdraw(60)
acc01.show_info()