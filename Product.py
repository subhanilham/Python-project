
class Product:
    def __init__(self,pro_name,price,firm,count,available):
        self.__available = available
        self.__pro_name = pro_name
        self.__price = price
        self.__firm = firm
        self.__count = count

    def get_available_product(self):
        return self.available
    def set_available_product(self,available):
        self.available = available

    def set_pro_name(self,pro_name):
        self.pro_name = pro_name
    def get_pro_name(self):
        return self.pro_name

    def set_price(self,price):
        self.__price = price
    def get_price(self):
        return self.__price

    def set_firm(self,firm):
        self.__firm = firm
    def get_firm(self):
        return self.__firm
    
    def set_count(self,count):
        self.__count = count
    def get_count(self):
        return self.__count

   


       
   