# Python Function Have 2 args --> 1) xargs(*args) 2)xxargs

# xargs-->
# xargs help multiple items can be passed thorw a single argument perameter to function 
#xargs returen a tuple.
# xargs define -> * before perameter


# before  xargs---->
def classOneStu(name,age,classN,sallary): # multiple perameter
    print(name,age,classN,sallary)
classOneStu("Habulla",24,"Two",30000)

# after  xargs---->
def classTwoStu(*details): # single perameter
    print(details) #('Jambura', 54, 'Seven', 40000)
    print(details[0]) #Jambura
classTwoStu("Jambura",54,"Seven",40000) #multiple items


#xxargs(**agrs)--->
# xxargs help multiple items can be passed thorw a single argument perameter to function .And it also help show key with value when result return 
#xargs returen a dictionary(object).
# xargs define -> ** before perameter

def classThreeStu(**details): # single perameter
    print(details) 
    print(details['name']) #Jambura
classThreeStu(name="Jambura",age=54,classN="Seven",sallray=40000) #return --> {'name': 'Jambura', 'age': 54, 'classN': 'Seven', 'sallray': 40000}



