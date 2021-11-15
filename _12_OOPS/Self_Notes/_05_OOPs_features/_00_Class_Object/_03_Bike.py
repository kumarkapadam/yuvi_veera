class Bike:
    def __init__(self, bike_name, mileage, color):
        self.bike = bike_name
        self.mil = mileage
        self.color = color

    def bike_det(self):
        print(
            f'bike name {self.bike} mileage is {self.mil} color is {self.color}')


bike_name = input("enter bike name:")
mileage = input("enter mileage:")
color = input("enter color:")

b1 = Bike(bike_name, mileage, color)
b1.bike_det()
