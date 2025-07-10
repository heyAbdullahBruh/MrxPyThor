#🔮 Magic Methods in Python (also called dunder methods) are special methods that start and end with double underscores like __init__, __str__, __len__, etc.
# They let you define how your objects behave with built-in functions and operators.



'''
| Magic Method             | Purpose                           | Example Use       |
| -------------------------| --------------------------------- | ----------------- |
| `__init__(self,other)`   | Constructor                       | `obj = MyClass()` |
| `__str__(self,other)`    | String representation (for print) | `print(obj)`      |
| `__repr__(self,other)`   | Official string (for debugging)   | `repr(obj)`       |
| `__len__(self,other)`    | Length of object                  | `len(obj)`        |
| `__add__(self,other)`    | Addition operator (`+`)           | `obj1 + obj2`     |
| `__sub__(self,other)`    | Substraction operator (`-`)       | `obj1 - obj2`     |
| `__mul__(self,other)`    | Multiply operator (`*`)           | `obj1 * obj2`     |
| `__div__(self,other)`    | Division operator (`/`)           | `obj1 / obj2`     |
| `__eq__(self,other)`     | Equality (`==`)                   | `obj1 == obj2`    |
| `__ne__(self,other)`     | not equal (`!=`)                  | `obj1 != obj2`    |
| `__lt__(self,other)`     | Less than (`<`)                   | `obj1 < obj2`     |
| `__le__(self,other)`     | Less than equal (`<=`)            | `obj1 < obj2`     |
| `__gt__(self,other)`     | grater than (`>`)                 | `obj1 > obj2`     |
| `__ge__(self,other)`     | grater than equal (`>=`)          | `obj1 > obj2`     |

'''

class Country : 
    name =''
    age =0
    population =0
    gdp =0
    area =0
    currancy =''
    
    def __init__(self,name,age,population,gdp,area,currancy): #__init__ Magic Method
        self.name=name
        self.age=age
        self.population=population
        self.gdp=gdp
        self.area=area
        self.currancy=currancy
    def __str__(self):
        return f"The Country name is {self.name}. {self.name}'s population is {self.population} Million and GDP is {self.gdp}trillion . {self.name}'s use {self.currancy} currancy" 
    def __eq__(self, other):
        if self.currancy == other.currancy : 
            return f"{self.name} and {other.name} currancy are similar"
        else : 
            return f"{self.name} and {other.name} currancy aren't similar"
    def __add__(self,other) :
        sum = self.population +other.population
        return f"{self.name} and {other.name} total population is {sum}Million "
    def __gt__(self,other):
        if self.gdp > other.gdp :
            return f"{self.name}'s have more than GDP  from {other.name}"
        else :
            return f"{other.name}'s have more than GDP  from {self.name}"

country1 =Country('USA',200,150,110,55.5,"USD")
country2 =Country('MEXICO',100,50,10,35.5,"USD")

print(country1) #The Country name is USA. USA's population is 110 Million and GDP is 150trillion . USA's use USD currancy

print(country1==country2) #USA and MEXICO currancy are similar
print(country1+country2)  #USA and MEXICO total population is 120Million
print(country1<country2)





