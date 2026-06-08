#When mulitpl inheritance exists then it follow mro
#Method Resolution Order(MRO)
class A:
    def intro(self):
        print("A")

class B(A):
    def intro(self):
        print("B") 

class C(A):
    def intro(self):
        print("C")

class D(B,C):
    pass

d=D()

#it follows B->C->A
d.intro()
