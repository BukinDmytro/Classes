#2

class Circle:
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        print(3,14 * self.radius**2)
areaa = Circle(2)
areaa.area()