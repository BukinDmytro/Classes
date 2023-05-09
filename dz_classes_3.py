#3

class Car:
    def __init__(self,brand = "Audi",model = "RS6",year = "2022"):
        self.brand = brand
        self.model = model
        self.year = year
    def info(self):
        print("Brand - ", self.brand ,"Model - ", self.model ,"Year - ",  self.year)
mashina = Car()
mashina.info()
