class Parent:
    def mobile(self):
        print("IQOO Z3")

    def vehicle(self):
        print("Glamour")

class Child(Parent):
    # pass
    def mobile(self):
        print("Samsung S23")

obj=Child()
obj.mobile()
obj.vehicle()

# child has a method and it overrides the method of parent 
# same methodname and same signature 