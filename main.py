
from Services.Courier import Courier
from Services.DeliveryCenters import DeliveryCenters
from Services.DeliveryService import DeliveryService
from Services.DeliveryVehicle import DeliveryVehicle
from User.User import User
from User.Consumer import Consumer
from User.Purchaser import Purchaser
from Products.Product import Product
from Products.food import food
from Products.clothes import clothes
from Products.accessory import accessory
from Products.technology import technology
from Products.hobby import hobby
from Products.Products import Products
from User.PurchaserAddress import PurchaserAddress
from Services.Garage import Garage

#create user
subhan = User()
#register
subhan.get_register("subhan","subhanshirinzade@gmail.com","1234","1234")
#login
subhan.login("subhan","subhanshirinzade@gmail.com","1234")
#being consumer or purchaser
subhan = Consumer()






#available produts
xiaomi_mi_band_5 = technology("Xiaomi MI band 5","50$","Xiaomi","5000",True,"Xiaomi mi","Smart Watch")
Iphone_pro_max = technology("Iphone Pro Max 12","3500$","Apple","350",True,"Iphone","Mobile Phone")

lays = food("Lays Classic","2$","Lays","12000",True,False,"01.01.2023")
noodle = food("Instant Noodle","0.50$","Kent","1200000",True,False,"02.05.2023")

Air_Jordan_tshirt = clothes("Air Jordan Logo T-shirt","20$",True,"Air Jordan","500","M","black")
Dress = clothes("V-necked Red Woman Dress","200$","DeFacto","200",True,"L","red")

Neck_jewelry = accessory("Daisy necklace","25$","Papatya silver","500",True,"necklace","gold")
Bag = accessory("Unisex Hugbag","60$","Aqua Di Polo","500",True,"hugbag","fabric")

Piano = hobby("Bechstein D 282","119000$","Bechstein","10",True,"Music")
Basketball = hobby("Spalding NBA Zi/O","35$","Spalding","500",True,"Sport")

#where the products are (warehouse)
sala = Products("baka",[xiaomi_mi_band_5,Iphone_pro_max,lays,noodle,Air_Jordan_tshirt,Dress,Neck_jewelry,Bag,Piano,Basketball])

#couriers
farid = Courier("farid","002",True)
derya = Courier("derya","003",True)
nicat = Courier("nicat","004",False)
#derlivey centers
Badamdar = DeliveryCenters("yasamal")
Yasamal = DeliveryCenters("badamdar")

#delivery vehicles
motorcyle = DeliveryVehicle("Honda Alpha","99-bb-168",True)
car = DeliveryVehicle("Toyota Prius","10-nd-151",True)

#garages
Anything = Garage("add",[motorcyle,car])

#delivery service
Volt = DeliveryService("volt",[farid, derya, nicat],[Yasamal, Badamdar])

x = input()
while True:
    if x == "Yes":
        subhan.be_consumer()
        print()
        print("--------------------------------Information-------------------------------")
        print()
        print("Please give info about your address and card info")
        subhan.enter_info("subhan","baku","0001","1234","050-585-55-54")
        print()
        print("----------------------------Searching Product-----------------------------")
        print()
        Chosen_product = subhan.search_product(sala)
        print(Chosen_product)
        random_available_courier = subhan.searh_for_couriers(Volt)
        print(random_available_courier)
        if random_available_courier == "derya":
            random_available_vehicle = derya.choosing_vehicle(Anything)
            print(random_available_vehicle)
        else:
            random_available_vehicle = farid.choosing_vehicle(Anything)
            print(random_available_vehicle)
    elif x == "No":
        break
    else:
        print("You must be write Yes or No")
        break
    
        








Ali = Purchaser()

z = input()
while True:
    if z == "Yes":
        break
        Ali.be_purchaser()
        print()
        print("--------------------------------Information-------------------------------")
        print()
        print("Please give info about your contact number and mail for backups")
        Ali.enter_info("050-865-65-65","sajgs@mail.com")
        baku = PurchaserAddress("azerbaijan","baku","badamdar 7","0022","Bak; yasamal")
    elif z == "No":
        break
    
Ali.run()    




