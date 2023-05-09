#1

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def is_adult(self):
        if self.age >= 18:
            print("True")
        elif self.age < 18:
            print("False")
dima = Person("Dima" , 16)
print(dima.age)
