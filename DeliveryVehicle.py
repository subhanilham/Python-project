class DeliveryVehicle():
    def __init__(self,vehicle_name,vehicle_number,available):
        self.vehicle_name = vehicle_name
        self.vehicle_number = vehicle_number       
        self.available = available
    
    def set_available_vehicle(self,available):
        self.available = available
    
    def get_available_vehicle(self):
        return self.available