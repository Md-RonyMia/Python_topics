class Person:
    def __init__(self):
        self.members=["Alice", "Bob", "Charlie"]
    def __len__(self):
        return len(self.members)
#len use for getting the length of the object and it is called when we use len() function on the object of the class
p=Person()
print(len(p))  # Output: 3