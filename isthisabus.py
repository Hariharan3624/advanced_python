class vehichile:
    def __init__(self,name,max_speed,mileage):
        self.name = name
        self.max_speed = max_speed
        self.mileage = mileage
class bus(vehichile):
    pass
obj = bus("volo",180,12)
print("vehichle name:", obj.name, "speed:", obj.max_speed, "mileage:",obj.mileage)