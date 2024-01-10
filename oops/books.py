class Book:

    name:str
    author:str
    pages:int
    price:int

    def __init__(self,name,author,pages,price):
        #__init__ initializes the instance variables(variables starting with self)
        self.name=name
        self.author=author
        self.pages=pages
        self.price=price
    
    def display_book(self):
        print(self.name,self.author)

    def __str__(self):
        return self.name

obj=Book("Mein Kamf", "Adolf hitler", 347, 1500)
# constructor is invoked while object creation
print(obj)
obj.display_book()