from Products.Good import Good
class Purchaser:
    def __init__(self):
        self.good_data = []
        print("---------------------------------Purchaser--------------------------------")
        print("")
        print("Fist of all you must be purchaser")
        print()
        print("Do you want to purchaser?")
        
    def be_purchaser(self):
        pass
        
    def enter_info(self,cont_num,backup_mail):
        self.cont_num =cont_num
        self.backup_mail = backup_mail
        print()
        print("You are a purchaser now")
        print()
        print("--------------------------------------------------------------------------")
        
    def sendout(self):
        print("")
        print("------------------------------Adding Product------------------------------")
        print("------------------------1.Add Product-------------------------------------")
        print("------------------------2.Show added product(s)---------------------------")
        print("------------------------3.Exit--------------------------------------------")
    
    # aaa,bbb,ccc completed the entry of goods [bbb,ccc is the judgment condition of aaa]
    def a_good(self):
        good_id = input("Please enter the item Id:")
        good_name = input("Please enter product's name:")
        good_pirce = input("Please enter the unit price:")
        good_count = input("Please enter the quantity of goods:")
        good_unit = input("Please enter the unit of firm of goods:")
        good_type = input("Please enter the type of product:")
        good = Good(good_id, good_name, float(good_pirce), int(good_count), good_unit, good_type)
        self.good_data.append(good)
        print("Goods added successfully!")

    def b_good(self):
        print("------------------------------Added Products------------------------------")
        for item in self.good_data:
            print(f"ID {item.id}  Name {item.name}    Count {item.count}    Price {item.price}    Firm {item.unit}    Type {item.type}")
        print("--------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------")
        print("--------------------------------------------------------------------------")    
        
    # Main loop
    def run(self):
        while True:
            self.sendout()
            index = input("Please select the operation: ")
            if index == "1":
                self.a_good()
            elif index == "2":
                self.b_good()
            elif index == "3":
                print("Good bye, you are welcome")
                return
            else:
                print("What the hell did you lose? Do it again")
        

    
        


  