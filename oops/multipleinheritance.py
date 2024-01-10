class P1():
    def m1(self):
        print("inside m1")

class P2():
    def m2(self):
        print("inside m2")


class Child(P1,P2):
    pass

ch=Child()

ch.m1()
ch.m2()

#if the methods in the parent classes are the same, the interpreter runs in the order of inheritance
#ie, if the method m is in the class P1, it runs or if it is in p2,  P2 runs