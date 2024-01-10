class Mobile:

    brand:str
    model:str
    display:str
    price:int

    def __init__(self,brand,model,display,price):
        self.brand=brand
        self.model=model
        self.display=display
        self.price=price

    def display_phone(self):
        print(self.brand, self.model, self.price)

    #__str__ returns the string representation of the object
    def __str__(self):
        return self.brand

obj1=Mobile("Google","Pixel8", "Amoled", 70000 )

obj1.display_phone()
print(obj1) # this returns the location of the object because it has many attributes, so to print any attribute __str__ is used 