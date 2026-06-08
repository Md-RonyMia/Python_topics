class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"Student(name={self.name}, age={self.age})"

s=Student("Alice", 20)
print(s)
  # This will call the __str__ method and print the string representation of
#without string it gives output as <__main__.Student object at 0x7f8b8c8c8c8c> which is not human readable
# Purpose:
# Provide a human-readable string representation of the object
