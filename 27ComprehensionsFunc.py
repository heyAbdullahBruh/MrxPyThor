# Comprehensions funtion use instead filter and map --> 

# map --> 
# normal way-->
num= [21,34,5,6]

def square (x) :
    return x**2

numSquareResult = list(map(square,num))
print(list(numSquareResult))

# Useing Comprehensions --> rule --> [ result=> x*x  for item=> x  in list => []]
numSquareResult2= [x**2 for x in num ]
print(numSquareResult2) #[441, 1156, 25, 36]

#filter -->
# 1)
# normal way -->
sturant = ["Navid",'sabid','jhabidh']

def singleStu (n) :
    return n=='Navid'
getSingStu = list(filter(singleStu,sturant))
print(getSingStu)
# Useing Comprehensions --> rule --> [ result=> x  for item=> x  in list => [] if x["name"] =='Navid']
getSingStu2 =[ n  for  n  in sturant if  n =='Navid']
print(getSingStu2) #'Navid'


# 2)
# normal way -->
workers = [
    {
        "name":"Naved Hasan",
        "age":30,
        'sallary' :50000,
        "active":True
    },
    {
        "name":"Javed Kasan",
        "age":20,
        'sallary' :40000,
        "active":False
    },
    {
        "name":"Goved Nanas",
        "age":43,
        'sallary' :35252,
        "active":False
    },
    {
        "name":"Daged Dasab",
        "age":21,
        'sallary' :35003,
        "active":True
    }
]

def employeeDetails (n) :
    return  n["sallary"]>= 40000 and n["active"]==True 
getEmplDesc = list(filter(employeeDetails,workers))
print(getEmplDesc) #[{'name': 'Naved Hasan', 'age': 30, 'sallary': 50000, 'active': True}]

# Useing Comprehensions --> rule --> [ result=> x  for item=> x  in list => [] if x["name"] =='Navid']
getEmplDesc2 =[ wrkr  for  wrkr  in workers if  wrkr['sallary'] >30 and wrkr["active"]==True]
print(getEmplDesc2) #[{'name': 'Naved Hasan', 'age': 30, 'sallary': 50000, 'active': True}, {'name': 'Daged Dasab', 'age': 21, 'sallary': 35003, 'active': True}]