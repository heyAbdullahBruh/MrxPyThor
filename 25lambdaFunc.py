# Lambda function is a single line function . 
# its define start with lambda keyword

# normal function 
def multiply(a,b):
    print(a*b)
multiply(4,5) #20

# Lambda function
# 1)-->
multiply2 = lambda a,b:a*b 
print(multiply2(4,3375843675)) #13503374700

# 2)--->
print((lambda x,y :x**y)(50,45)) #28421709430404007434844970703125000000000000000000000000000000000000000000000
