#Abstraction in Python means hiding unnecessary details from the user and showing only the essential features — just like how you drive a car without knowing the engine's internal design.
# In Python, abstraction is commonly done using abstract classes and abstract methods, provided by the 'abc' module.
# abc = abstract base class

# When a class creates an abstract method, if a child class uses this class(parent) then in child class must use the method(abstract) of the parent class.
# Can't instantiate abstract class without an implementation for abstract method 


from abc import ABC , abstractmethod

class Animal(ABC) : # ABC
    name=''
    height= ''
    def __init__(self,name ,height):
        self.name =name
        self.height =height
    @abstractmethod
    def info(self): # method(abstract)
        pass

class Cat(Animal) :
    color = ''
    catagory= ''
    
    def __init__(self,name ,height,color,catagory):
        super().__init__(name ,height)
        self.color=color
        self.catagory =catagory
    def info (self):
        return self.name ,self.height,self.color,self.catagory

#  a = Animal()  ❌ Error: Can't instantiate abstract class

cat1 = Cat('Birall','1 meter','Pink','Bink')
print(cat1.info())#('Birall', '1 meter', 'Pink', 'Bink')
