'''
class Student:
    height = 160
    def __init__(self):
        print(self.height)
        self.height+=10

Ivan = Student()
Pavel = Student()
'''
import math

'''
class Student:
    def __init__(self, name = None, height = 170):
        self.name = name
        self.height = height
    def __bool__(self):
             return self.name != None
    def __len__(self):
             return self.height
    def __del__(self):
            print("Training is over")

ivan = Student()
print(ivan.__len__())
print(ivan.__bool__())
print(len(ivan))
print(bool(ivan))
'''
'''
class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def get_info(self):
        return f"Ім'я:{self.name}, Вік:{self.age}"
student1=Student("Кіріл", 15)
print(student1.get_info())
'''
'''
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def area(self):
        return 3.14159*self.radius**2
circle1 = Circle(19)
print(circle1.area())
'''

import random
class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 100
        self.progress = 0
        self.stamina = 100
        self.alive = True
    def to_study(self):
        print("Time to study")
        self.progress += 0.12
        self.gladness -= 5
        self.stamina -=30
    def to_sleep(self):
        print("Time to study")
        self.progress -= 0
        self.gladness += 2
        self.stamina += 40
    def to_chill(self):
        print("Time to chill")
        self.progress -= 0.03
        self.gladness += 5
        self.stamina += 15
    def is_alive(self):
        if self.progress <= -0.5:
            print("You are dumb")
            self.alive = False
        elif self.gladness == 0:
            print("You was jamped intro the Window")
            self.alive = False
        elif self.stamina == 0:
            print("You was martyred")
            self.alive = False
    def end_of_day(self):
        print(f"Gladness = {self.gladness}")
        print(f"Stamina = {self.stamina}")
        print(f"Progress = {self.progress}")
    def live (self):
        day = "Day" + str(day) + "of" + self.name + "life"
        print(f"{day:=^50}")

        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
         elif live_cube == 2:
            self.to_sleep()
         elif live_cube == 3:
            self.to_chill()

pasha = Student(name = "Pasha")
for day in range(365):
    if pasha.alive == False:
        break
pasha.live(day)
