class Data:
    def __init__(self):
        self.items = [1, 2, 3, 4, 5]
    def __setitem__(self, index,value):

        #__setitem__ is used for setting the item at the specified index in the items list
        self.items[index]=value

d=Data()
# setting the item at index 1 to 10 using __setitem__ method
d[1] = 10
print(d.items)
    