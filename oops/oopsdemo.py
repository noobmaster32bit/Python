
class Employee:
    name:str
    id:int
    department:str
    salary:int

    def set_emp(self,name,id,dep,sal):
        self.name=name
        self.id=id
        self.department=dep
        self.salary=sal

    def display_emp(self):
        print(self.name,self.id,self.department,self.salary)

emp1=Employee()

emp1.set_emp("manoj",147,"UEX",32000)
emp1.display_emp()

emp2=Employee()
emp2.set_emp("alan",786,"SDE",33000)
emp2.display_emp()