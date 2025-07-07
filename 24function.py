# fucntion make re-useable code ;
# python have 2types function --> 1) User define function , 2) library function

a=2
b=3
print(a+b) #5

a=5
b=8
print(a+b) #13

a=6
b=7
print(a+b) #13

a=9
b=8
print(a+b)#17


# Define A function --->
def sum(a,b):
    print(a+b)
sum(33,44) # 77
sum(32,79)# 111
sum(76,89)# 165
sum(54,34)# 88

# Retrun a result from a function --> 
def toThePowerSum(x,y):
    return x**y
threePower5 =toThePowerSum(3,5)
print(threePower5) #243



