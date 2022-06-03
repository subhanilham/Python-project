
from Products.Product import Product

class clothes(Product):
    def __init__(self, pro_name, price, firm, count, available, size, color):
        self.pro_name = pro_name
        self.__price = price
        self.__firm = firm
        self.__count = count
        self.available = available
        self.__size = size
        self.__color = color
    
    def set_size(self, size):
        self.__size = size
    def get_size(self):
        return self.__size

    def set_color(self, color):
        self.__color = color
    def get_color(self):
        return self.__color