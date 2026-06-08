#When mulitpl inheritance exists then it follow mro
#Method Resolution Order(MRO)
class A:
    def intro(self):
        print("A")

class B(A):
    def intro(self):
        print("B")
        super().intro() 

class C(A):
    def intro(self):
        print("C")
        super().intro()

class D(B,C):
    def intro(self):
        print("D")
        super().intro()

d=D()

#it follows D->B->C->A
d.intro()
