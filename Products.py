class Products:
    def __init__(self,p_name,available_products):
        self.p_name = p_name
        self.available_products = available_products

    def check_available_products(self):
        b_products = []
        for producct in self.available_products:
            if producct.get_available_product:
                b_products.append(producct.pro_name)
               
        print()
        return b_products

    