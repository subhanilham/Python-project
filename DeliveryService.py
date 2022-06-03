class DeliveryService():
    def __init__(self,name,couriers,center):
        self.name = name
        self.couriers = couriers
        self.center = center
   
    def check_available_couriers(self):
        print("Service", self.name, "searching for available courier")
        print()
        available_couriers = []
        print("There are available courier:")
        print()
        for courier in self.couriers:
            if courier.get_available():
                available_couriers.append(courier)
                print(courier.courier_name, end=", ")
            else:
                break
        print()
        return available_couriers
        

        
       


        