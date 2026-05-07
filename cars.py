class bmw:
    def fuel(self):
        print("BMW: uses disel or electric")
    def max_speed(self):
        print("BMW max speed is 250 km/h")
class ferrari:
    def fuel(self):
        print("ferrari: uses high-octone petrol")
    def max_speed(self):
        print("ferrari: max speed is 350 km/h")
car1 = bmw()
car2 = ferrari()
for car in (car1,car2):
    car.fuel()
    car.max_speed()
