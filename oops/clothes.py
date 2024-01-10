class Cloth:
    name:str

    def __init__(self,name):
        self.name=name

    def __str__(self):
        return self.name
    
class Variant(Cloth):

    brand_name:str
    size:str
    color:str

    def __init__(self,name,brand_name,size,color):
        super(). __init__(name)
        self.brand_name=brand_name
        self.size=size
        self.color=color

var_obj=Variant("Casual Shirt","Allen Solly","medium","navyBlue")
print(var_obj)



