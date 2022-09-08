class Product:
    def __init__(self, price):
        self.price = price
        
    # get the price
    @property
    def price(self):
        return self.__price
    
    # set the price
    @price.setter
    def price(self, value):
        if value < 0:
            return None
        self.__price = value
        
pro = Product(10)
pro.price = -45
print(pro.price)
