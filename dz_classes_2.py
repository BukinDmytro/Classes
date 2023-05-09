#2

class Rectangle:
    def __init__(self, width=3, height=2):
        self.width = width
        self.height = height
        self.area = None
        self.perimeter = None
    def areaa(self):
        self.area = self.width * self.height
    def perimeterr(self):
        self.perimeter = (self.width + self.height) * 2

rectangle = Rectangle()
rectangle.areaa()
rectangle.perimeterr()
print(rectangle.area)
print(rectangle.perimeter)

