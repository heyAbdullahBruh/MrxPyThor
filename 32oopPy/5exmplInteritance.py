# example of class inheritence

#Area calc-2--->

class Shape :
    base = 0
    height = 0
    def __init__(self,base,height):
        self.base=base
        self.height =height
    def calc() :
        print(f"Calculate your shape ")
        
        
class Tringle(Shape) :
    
    def calc(self) : #Method overriding
        result =.5 * self.base * self.height
        print(f"The Tringle shape's area is = {result} ")

tringle1 =Tringle(20,40)
tringle1.calc() #The Tringle shape's area is = 400.0 

class Rectangle(Shape) :
    
    def calc(self) :#Method overriding
        result = self.base * self.height
        print(f"The Rectangle shape's area is = {result} ")
        
rec1 =Rectangle(30,50) 
rec1.calc() #The Rectangle shape's area is = 1500 
        
        