class Person:
    def __init__(self,name):
        #it directly assign the name with particular instance of the class
        self.name = name
    def __str__(self):
        return f"{self.name}"

p=Person("Alice")
print(p)