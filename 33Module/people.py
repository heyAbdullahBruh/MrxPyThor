# Create Module ---> 

class Student : 
    name = ''
    age=''
    classN=''
    stuId=''
    
    def __init__(self,name,age,classN,stuId):
        self.name=name
        self.age=age
        self.classN=classN
        self.stuId=stuId
    def info(self):
        print(f"name : {self.name},\nage : {self.age},\nclass : {self.classN},\nstudentId : {self.stuId}") 
    
class Worker : 
    name = ''
    age=''
    sallary=''
    employeeId=''
    
    def __init__(self,name,age,sallary,employeeId):
        self.name=name
        self.age=age
        self.sallary=sallary
        self.employeeId=employeeId
        
    def info(self):
        print(f"name : {self.name},\nage : {self.age},\n sallary : {self.sallary},\nemployeeId : {self.employeeId}") 
        
    