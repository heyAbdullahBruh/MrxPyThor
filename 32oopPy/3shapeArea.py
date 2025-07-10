# Make a shape area calculator with class --->

class Triangle : 
    base = 0
    height = 0
    
    def __init__(self,base,height):
        self.base=base
        self.height=height
    def calc (self): 
        baseNum= float(self.base)
        heightNum= float(self.height)
        result = .5 * baseNum * heightNum
        
        print(f"The triengle shape's area is = {result} meter^2 ")
        

triangle1= Triangle(30,40)
triangle1.calc() # The triengle shape's area is = 600.0 meter^2 

triangle2= Triangle(.2123,.32930)
triangle2.calc() # The triengle shape's area is = 0.034955194999999994 meter^2 

