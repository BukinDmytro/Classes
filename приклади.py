###

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

book1 = Book("Tom", "SOyer") #екземпляр класу


###

class Book:
    book_count = 0 #атрибут класу

    def __init__(self, title, author): #ініт і все що задається ніби функція - це метод класу
        self.title = title
        self.author = author
        Book.book_count += 1

###

class Person:
    # Атрибут класу
    species = 'human'

    def __init__(self, name, age):
        # Атрибути об'єкту
        self.name = name
        self.age = age


### приклад методу grow


class Student:
 amount_of_students = 0
 def __init__(self, height=160):
    self.height = height
    Student.amount_of_students+=1
 def grow(self, height=1):
    self.height+=height
nick = Student()
kate = Student(height=170)
nick.grow(height=15)
print(kate.height)
print(nick.height)


### метод  __str__(),

class Student:
    def __init__(self, name=None):
        self.name = name

    def __str__(self):
        return f"I am a student.My name is {self.name}"


nick = Student(name="Nick")
print(nick)


### метод __del__()


class Student:
    def __init__(self, name=None):
        self.name = name
    def __del__(self):
        print("Training is over.I am now an expert!")
nick = Student()


###
'''Конструктор класу - це метод з іменем __init__, який викликається автоматично при створенні нового екземпляру класу.'''
###



### симуляція життя студента

import random
class Student:

    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
    def to_sleep(self):
        print("I will sleep")
        self.gladness += 3
    def to_chill(self):
        print("Rest time")
        self.gladness += 5
        self.progress -= 0.1
    def is_alive(self):
        if self.progress < -0.5:
            print("Cast out…")
            self.alive = False
        elif self.gladness <= 0:
            print("Depression…")
            self.alive = False
        elif self.progress > 5:
            print("Passed externally…")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Progress = {round(self.progress, 2)}")
    def live(self, day):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()
        self.end_of_day()
        self.is_alive()

nick = Student(name="Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)