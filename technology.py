from Products.Product import Product

class technology(Product):
    def __init__(self, pro_name, price, firm, count, available, brand, type_tech):
        self.pro_name = pro_name
        self.__price = price
        self.__firm = firm
        self.available = available
        self.__count = count
        self.__brand = brand
        self.__type_tech = type_tech

    def set_brand(self, brand):
        self.__brand = brand
    def get_brand(self):
        return self.__brand

    def set_type_tech(self, type_tech):
        self.__type_tech = type_tech
    def get_type_tech(self):
        return self.__type_tech

        