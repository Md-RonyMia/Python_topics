class Person:
    #Every instance of the class will have the same value for this attribute
    School="ABC School"

    def __init__(self,name):
        #it directly assign the name with particular instance of the class
        self.name = name
    def __str__(self):
        return f"{self.name} from {self.School}"
p1=Person("Alice")
p2=Person("Bob")
print(p1)
print(p2)