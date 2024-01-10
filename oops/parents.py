class Parent:
    def properties(self):
        self.vehicles=["swift","phantom"]
        return self.vehicles
    
    
class Child(Parent):
    def properties(self):
        self.context=super().properties()
        self.context.append("bentley")
        return self.context


ch=Child()
print(ch.properties())

par=Parent()
print(par.properties())
