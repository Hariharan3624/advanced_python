class dog:
    def __init__(self,breed,color):
        self.breed = breed
        self.color = color
square = dog("pitbull","brown")
circle = dog("husky","black")
print(square.breed)
print(square.color)
print(circle.breed)
print(circle.color)