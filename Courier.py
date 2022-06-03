from Services.Garage import Garage
from Services.DeliveryVehicle import DeliveryVehicle
import random
class Courier():
    def __init__(self,courier_name,c_contact_num,available):
        self.courier_name = courier_name
        self.c_contact_num = c_contact_num
        self.available = available
    
    def get_available(self):
        return self.available

    def set_available(self, available):
        self.available = available

    def choosing_vehicle(self,vehicle):
        print("Your courier choosing vehicle")
        print()
        print("Available vehicles:")
        available_vehicles = vehicle.check_available_vehicles()
        print()
        vehicle_choice = random.choice(available_vehicles)
        print("Your courier's vehicle is",vehicle_choice.vehicle_name)
        print()
        print("Your order is on its way")
        print()
        return "---------------------------------------------------------------------------"