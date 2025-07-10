#Multilevel inheritance means a class inherits from a class that itself inherits from another class — like a chain.

class Animal : 
    name=''
    height= ''
    def __init__(self,name ,height):
        self.name =name
        self.height =height

'''
    |
    |
    |
'''

class Cat(Animal) :
    color = ''
    catagory= ''
    
    def __init__(self,name ,height,color,catagory):#Methode overriding
        super().__init__(name ,height)
        self.color=color
        self.catagory =catagory
    def catInfo (self):
        return self.name ,self.height,self.color,self.catagory
    
cat1 = Cat('Birall','1 meter','Pink','Bink')
print(cat1.catInfo())#('Birall', '1 meter', 'Pink', 'Bink')
'''
    |
    |
    |
'''

class ParsianCat(Cat) :
    weight =0
    def __init__(self,name ,height,color,catagory,weight):#Methode overriding
        super().__init__(name ,height,color,catagory)
        self.weight=weight
    def catInfo (self):#Methode overriding
        return self.name ,self.height,self.color,self.catagory,self.weight

parsian1 = ParsianCat('Bilai','.5 meter','Blue','Parsian',10)
print(parsian1.catInfo()) #('Bilai', '.5 meter', 'Blue', 'Parsian', 10)



