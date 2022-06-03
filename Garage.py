class Garage:
    def __init__(self,garage_name,vehicles):
        self.garage_name = garage_name
        self.vehicles = vehicles

    def check_available_vehicles(self):
        available_vehicles = []
        for vehicle in self.vehicles:
            if vehicle.get_available_vehicle:
                available_vehicles.append(vehicle)
                print(vehicle.vehicle_name, end=" ")
        print()
        return available_vehicles