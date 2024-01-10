from abc import ABC,abstractmethod

class Editor(ABC):

    @abstractmethod
    def edit(self):
        pass

    @abstractmethod
    def debug(self):
        pass

    @abstractmethod
    def execute(self):
        pass


class VsCode(Editor):

    def edit(self):
        print("VsCode can edit")

    def debug(self):
        print("VsCode can debug")

    def execute(self):
        print("VsCode can execute")


obj=VsCode()
obj.edit()
