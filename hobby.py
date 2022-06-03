from Products.Product import Product

class hobby(Product):
    def __init__(self, pro_name, price, firm, count, available, type_of_hobby, ):
        self.pro_name = pro_name
        self.__price = price
        self.__firm = firm
        self.__count = count
        self.__available = available
        self.__type_of_hobby = type_of_hobby
        
    def set_type_of_hobby(self, type_of_hobby):
        self.__type_of_hobby = type_of_hobby
    def get_type_of_hobby(self):
        return self.__type_of_hobby
