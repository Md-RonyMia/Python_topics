# Parent Class
class Person:
    def __init__(self,name):
        self.name=name
    def introduce(self):
        print(f"this is {self.name}")

# Child Class
class Student(Person):
    pass


s=Student("Abir")
s.introduce()
    