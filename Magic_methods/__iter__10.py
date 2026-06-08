class Counter:
    def __init__(self,max_num):
        #first we will initialize the max_num and current number to 1
        self.max_num=max_num
        self.current=1

    def __iter__(self):
        #__iter__ is used for returning the iterator object itself and it is called when we use iter() function on the object of the class
        return self
    def __next__(self):
        #__next__ is used for getting the next item from the iterator and it is called when we use next() function on the object of the class
        if self.current>self.max_num:
            raise StopIteration
        num=self.current
        self.current+=1
        #returning the current number and then incrementing it by 1 for the next iteration
        return num

for i in Counter(5):
    print(i)
           
        