
from Products.Product import Product
from Products.food import food
from Products.clothes import clothes
from Products.accessory import accessory
from Products.technology import technology
from Services.DeliveryService import DeliveryService
from User import User
from Products.Products import Products

import random
class Consumer():
    def __init__(self):
        pass
        print("---------------------------------Consumer---------------------------------")
        print("")
        print("Fist of all you must be consumer")
        print("")
        print("Do you want to consumer?")

    def be_consumer(self):
        pass

    def enter_info(self,name,address,cardnumber,card_pass,phone_num):
        self.name = name
        self.address = address
        self.cardnumber = cardnumber
        self.card_pass = card_pass
        self.phone_num = phone_num
        print("")
        print("You are a Consumer now")
        print("")
        print("Your info will be safe :)")
        print("")

    
    def search_product(self, xx):
        print(self.name, "searhcing products")
        print()
        
        print("Do you want to order any product?")
        w = input()
        if w == "Yes":
            print("There are available products:")
            a_products = xx.check_available_products()
            print(a_products)
            print()
            print("---------------------------------Ordering---------------------------------")
            print("Please write product what you want")
            a = input()
            x = len(a_products)
            for i in range(x):
                
                if a == a_products[i]:
                    print()
                    print("You ordered", a)
                    print()
                
                else:
                    pass
                    
                i = i + 1
                
        
        elif w == "No":
            return
    
        else:
            print("You must be write Yes or No")

        return "--------------------------------------------------------------------------"

    def searh_for_couriers(self, DeliveryService):
        print()
        print("---------------------------------Delivery---------------------------------")
        print()
        print(self.name,"is searching for available couriers")
        print()
        available_couriers = DeliveryService.check_available_couriers()
        courier_choice = random.choice(available_couriers)
        print()
        print(self.name, "chose the following courier", courier_choice.courier_name)
        print()
        return "--------------------------------------------------------------------------"

    

       
    
    

        
    

        



