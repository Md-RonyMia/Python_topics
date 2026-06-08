# Parent Class
class Person:
    def __init__(self,name,age):
        self.name=name
        self.age=age

# Child Class
class Student(Person):
    #override parent class function
    def __init__(self,name,age,sal):
        #without using this parent class constructor will never executed,super()
        super().__init__(name,age)
        self.salary=sal
    def introduce(self):
        print(f"This is {self.name},age {self.age} and salary {self.salary} tk")
     


s=Student("Abir",25,50000)
s.introduce()

    