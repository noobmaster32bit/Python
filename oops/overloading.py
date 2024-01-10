class Calculator:
    def add(self,n1,n2):
        return n1+n2
    


    def add(self,n1,n2,n3):
        return n1+n2+n3
    


    def add(self,n1,n2,n3,n4):
        return n1+n2+n3+n4
    
op=Calculator()
print(op.add(15,64,30,82))

# print(op.add(10,20))  will not work 
# the most recent method will work because of method overloading
#one method and multiple arguments  
#use *args or **kwargs to support method overloading

