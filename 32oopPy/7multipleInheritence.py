#Multiple inheritance means a class inherits from two or more parent classes.

class People :
    name =''
    phone =''
    
    def __init__(self,name,phone):
        self.name =name
        self.phone =phone
    def info (self) :
        return self.name, self.phone
    
class Worker :
    work =""
    sallary =""
    def __init__(self,work,sallary):
        self.work =work 
        self.sallary =sallary
    def info (self) :
        return self.work,self.sallary,
    
class Student(People,Worker) :
    classN = ''
    age =''
    def __init__(self, name, phone,work,sallary,age,classN):
        People.__init__(self,name, phone) # Call People constructor
        Worker.__init__(self,work,sallary) # Call Worker constructor
        self.classN =classN
        self.age =age
    def info (self) :
        return self.name, self.phone,self.work,self.sallary,self.age,self.classN
    
student1= Student('Abed',"01823723744",'Journalist','20000',25,'Honors')

print(student1.info()) # ('Abed', '01823723744', 'Journalist', '20000', 25, 'Honors')
