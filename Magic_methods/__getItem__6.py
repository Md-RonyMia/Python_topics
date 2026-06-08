class Data:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5]
    def __getitem__(self, index):
        #__getitem__ is used for getting the item at the specified index from the items list
        return self.items[index]

d=Data()
# finding the item at index 1 using __getitem__ method
print(d[1])
    