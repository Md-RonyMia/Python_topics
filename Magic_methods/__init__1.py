class Student:
    # By assigning a object into Student it directly calls the __init__ method and assigns the value to the name variable
    #It is basically a constructor which is used to initialize the object of the class
    def __init__(self,name):
        self.name = name

    def intro(self):
        print(f"This is {self.name}")

s=Student("John")
s.intro()

# Purpose:

# Initialize object attributes
# Runs when object is created