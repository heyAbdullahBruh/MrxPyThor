#Inheritance allows a class (child) to reuse code from another class (parent), enabling code reusability and extension of functionality...->


#1-->

class Worker :
    name = ''
    age=''
    sallray =0
    
    def __init__(self,name,age,sallray):
        self.name=name
        self.age=age
        self.sallray=sallray
    
    def info(self) :
        return self.name, self.age, self.sallray
        
        
class SoftwareEng(Worker) : # Inherit "Worker" class in "SoftwareEng" class
    jobTile = ''
    
    def __init__(self, name, age, sallray,jobTitle):
        super().__init__(name, age, sallray) #Methode overriding
        self.jobTile = jobTitle
    def info(self):
       return self.name, self.age, self.sallray,self.jobTile
swEngr1 = SoftwareEng('Sabedd','25',50000,'Backend Dev') 
print(swEngr1.info())#('Sabedd', '25', 50000, 'Backend Dev')

print(issubclass(SoftwareEng,Worker)) #True ; issubclass method check prarent's child class
print(issubclass(Worker,SoftwareEng)) #False


#2 --->

class Animal : 
    def __init__(self):
        print('Animal is helpful for our Environment')
        
class Doggy(Animal) :
        pass
dog1 =Doggy() #Animal is helpful for our Environment

class Catty(Animal) :
     def __init__(self):
        super().__init__()#Methode overriding
        print('Cat is helpful for our Nature')
        
cat1 =Catty() #--> 
'''
Animal is helpful for our Environment
Cat is helpful for our Nature
''' 
