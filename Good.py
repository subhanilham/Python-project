class Good():
    def __init__(self, id, name, count, price, unit, type):
        # Unit price unit price unit type type: type
        self.id = id
        self.name = name
        self.count = 0
        self.price = 0
        self.unit = unit
        self.type = type
        self.set_count(count)
        self.set_price(price)
	
    #Limit of quantity. If the input is less than 0, return 0
    def set_count(self, count):
        if count > 0:
            self.count = count
        else:
            self.count = 0

    def get_count(self):
        return self.count

    ##Unit price limit. If the value is less than 0, return 0
    def set_price(self, price):
        if price > 0:
            self.price = price
        else:
            self.price = 0

    def get_price(self):
        return self.price

    def __str__(self):
        return f"{self.id},{self.name},{self.price},{self.count},{self.unit},{self.type}"



        