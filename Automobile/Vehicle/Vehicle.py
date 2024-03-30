class Vehicles:
    def __init__(self, car_type, car_price, car_tyres, car_doors):
        self.car_type = car_type
        self.car_price = car_price
        self.car_tyres = car_tyres
        self.car_doors = car_doors
        
    def speed(self):
        print(f'this {self.car_type}')
        
    def attributes(self):
        print(f"Car Type: {self.car_type}")
        print(f"Car Price: {self.car_price}")
        print(f"Car Tyres: {self.car_tyres}")
        print(f"Car Doors: {self.car_doors}")