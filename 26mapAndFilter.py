# Map and filer always work with list . those function always accept 2 value of peramete -> 1) function ,2) list(Arr).And its always returen list

# map -->

num= [21,34,5,6]

def square (x) :
    return x**2

numSquareResult = list(map(square,num))
print(list(numSquareResult))



#filter -->
# 1)
sturant = ["Navid",'sabid','jhabidh']

def singleStu (n) :
    return n=='Navid'
getSingStu = list(filter(singleStu,sturant))
print(getSingStu)

# 2)
employee = [
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
getEmplDesc = list(filter(employeeDetails,employee))
print(getEmplDesc)


