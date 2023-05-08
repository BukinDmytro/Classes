#1

class Student():
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def print_info(self):
        print(f"Ім'я: {self.name} , Вік: {self.age}")
student = Student("Діма" , 16)
student.print_info()