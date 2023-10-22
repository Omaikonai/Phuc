from car import Car

cx5 = Car('Honda', 'CX5', 10000)

print(cx5.brand) # print(cx5.get_brand())
print(cx5.model)

cx5.price = 20000

cx5.show_info()

cx5.price = -100 # cx5.set_price(-100)
cx5.show_info()