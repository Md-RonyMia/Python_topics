# Parent Class
class Person:
    def __init__(self,name):
        self.name=name
    def introduce(self):
        print(f"this is {self.name}")

# Child Class
class Student(Person):
    def self_intro(self):
        print("I am a student")
     


s=Student("Abir")
s.introduce()
s.self_intro()
    