class Parent1:
    def m1(self):
        print("inside parent1 m1 method")


class Parent2(Parent1):
    def m2(self):
        print("inside parent2 m2 method")


class Child(Parent2):
    def c(self):
        print("inside child c method")


obj1=Child()
obj1.c()
obj1.m2()
obj1.m1()

#child inherits from parent2 and parent 2 inherits from parent1
# this is multi level inheritance