class Vehicle:
    def __init__(self, max_speed, milage):
        self.max_speed = max_speed
        self.milage = milage
modleX = Vehicle(240, 18)
print("Model Max Speed: ",modleX.max_speed)
print("model milage:", modleX.milage)