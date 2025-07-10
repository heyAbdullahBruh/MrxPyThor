# Python class constructor __init__() method automatically runs when a new object is created, used to initialize the object’s properties.

#A method is a function defined inside a class that automatically takes the instance (self) as its first argument and is used to work with instance data.

class Student :
    name=''
    age=''
    stuId=''
    
    def __init__(self,name,age,stuId): #constractor
        self.age =age
        self.name=name
        self.stuId=stuId
        
    def info (self) :
        print(f"Student Name  : {self.name}\nStudent age  : {self.age}\nStudent Id  : {self.stuId} ")

stu1= Student("Rafeed",18,"34234sd")
stu1.info() #--->
"""
Student Name  : Rafeed
Student age  : 18     
Student Id  : 34234sd 
"""

stu2= Student("Naved",98,"sdhfh3223")
stu2.info() #--->
"""
Student Name  : Naved
Student age  : 98
Student Id  : sdhfh3223 
"""