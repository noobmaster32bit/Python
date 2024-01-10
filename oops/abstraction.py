from abc import ABC,abstractmethod

class Car(ABC):

    @abstractmethod
    def __init__(self,name,brand,model):
        pass

    @abstractmethod
    def start(self):
        pass

    @abstractmethod    
    def accelerate(self):
        pass

    @abstractmethod
    def stop(self):
        pass

class Audi(Car):

    def __init__(self, name, brand, model):
        self.name=name
        self.brand=brand
        self.model=model

    def start(self):
        print("audi starts")

    def accelerate(self):
        print("Audi accelerates")

    def stop(self):
        print("audi stops")

obj=Audi("audiQ3","Audi",2023)
obj.start()
obj.accelerate()
obj.stop()
