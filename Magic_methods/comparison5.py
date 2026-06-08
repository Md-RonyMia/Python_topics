class Student:
    def __init__(self, id):
        self.id = id
    def __eq__(self,other):
        return self.id == other.id
s1 = Student(1)
s2 = Student(1)
print(s1 == s2)  # Output: True

#others:
# __ne__: Defines behavior for the != operator.
# __lt__: Defines behavior for the < operator.
# __le__: Defines behavior for the <= operator.
# __gt__: Defines behavior for the > operator.
# __ge__: Defines behavior for the >= operator.

       