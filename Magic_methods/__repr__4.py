class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __repr__(self):
        return f"Student('{self.name}', {self.age})"
s = Student("Alice", 20)
#difference between __str__ and __repr__ is that __str__ is used for creating a human-readable string representation of the object, while __repr__ is used for creating an unambiguous string representation of the object that can be used to recreate the object.
print(repr(s))