from Products.Product import Product

class food(Product):
    def __init__(self, pro_name, price, firm, count, available, promotion, expiration_date):
        self.pro_name = pro_name
        self.__price = price
        self.__firm = firm
        self.__count = count
        self.available = available
        self.__promotion = promotion
        self.__expiration_date = expiration_date

    def set_promotion(self, promotion):
        self.__promotion = promotion
    def get_promotion(self):
        return self.__promotion

    def set_expiration_date(self, expiration_date):
        self.__expiration_date = expiration_date
    def get_expiration_date(self):
        return self.__expiration_date