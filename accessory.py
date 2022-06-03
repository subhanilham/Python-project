from Products.Product import Product

class accessory(Product):
    def __init__(self,pro_name,price,firm,count,available,type_acc,material):
        self.pro_name = pro_name
        self.__price = price
        self.__firm = firm
        self.__count = count
        self.available = available
        self.__type_acc = type_acc
        self.__material = material

    def set_type_acc(self, type_acc):
        self.__type_acc = type_acc
    def get_type_acc(self):
        return self.__type_acc
    
    def set_material(self, material):
        self.__material = material
    def get_material(self):
        return self.__material