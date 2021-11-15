"""method overriding ::  ability to chane the method implements in
 child class which is available from parent"""

print("-----method overriding-----------")


class Audi:
    def discription(self):
        print("this is the description function of class audi")


class Bmw():
    def discription(self):
        print("this is the description function of class bmw")


audi = Audi()
bmw = Bmw()
for car in (Audi, Bmw):
    car.discription(bmw)
