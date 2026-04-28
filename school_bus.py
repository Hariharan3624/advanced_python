class vehichle:
    def __init__(self,name,capacity):
        self.name = name
        self.capacity = capacity
    def fare(self):
        return self.capacity * 100
class bus(vehichle):
    def fare(self):
        base = super().fare()
        total = base + (0.10 * base)
        return total
school_bus = bus("school volvo",50)
print(f"total bus fare is: INR: {school_bus.fare()}")