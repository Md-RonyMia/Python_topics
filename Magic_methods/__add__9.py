class Money:
    def __init__(self,amount):
        self.amount=amount
    def __add__(self,other):
        #return into main class with addition of previous amount and new amount
        return Money(self.amount+other.amount)
    def __str__(self):
        return f"Total amount {self.amount} tk"
    
m1=Money(15000)
m2=Money(15000)
m3=Money(100)
print(m1+m2+m3)


# similar has sub