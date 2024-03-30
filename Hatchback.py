from Vehicle import Vehicles
class Hatchback(Vehicles):
    def speed(self):
        print(f"The {self.car_type} speeds at 100km/hr in 4.1 sec.")
        
class Modern_Hatchback(Vehicles):
    def speed(self):
        print(f"The {self.car_type} speeds at 150km/hr in 4.1 sec.")
        
year = 1961