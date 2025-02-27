
class Product:

    def __init__(self, price):
        self.set_price(price)

    def get_price(self):
        print("Getter Called.....")
        return self.__price

    def set_price(self, val):
        print("Setter Called.....")
        self.__price = val

    def del_price(self):
        print("deleter called......")
        self.__price = 0

    price = property(get_price, set_price, del_price)


coke = Product(110)
print(coke.price)

coke.price = 75
print(coke.price)

del coke.price
print(coke.price)

coke.price = 120
print(coke.price)
