class Student:
    name:str
    id:int
    department:str
    yoj:int

    def set_stu(self,name,id,dept,yoj):
        self.name=name
        self.id=id
        self.department=dept
        self.yoj=yoj

    def display_stu(self):
        print(self.name,self.id,self.department,self.yoj)

std1=Student()
std1.set_stu("Akshay", 123, "Cse", 2019)
std1.display_stu()

std2=Student()
std2.set_stu("Avinash", 963, "IT", 2020)
std2.display_stu()




