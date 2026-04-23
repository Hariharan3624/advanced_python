import math as m
class circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return m.pi * (self.radius ** 2)
    def perimeter(self):
        return 2 *m.pi * self.radius 
user = float(input("enter radius of the circle: "))
my = circle(user)
print(f"area: {my.area():2f}")
print(f"permeter: {my.perimeter():.2f}")