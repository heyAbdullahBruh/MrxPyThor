# Type casting is convertion way in Python . Like a user give a number on input but input always giving  string . If this number of string convert in actual number then use type casting way . 
# convert intiger -- int
# convert floating number -- float

num1 = input("Enter first number :")
num2 = input("Enter second number :")

result = num1 +num2
print("Result is "+ result) # If any user give value on num1 is 1 and num2 is 2 then the will show 12 . Bcz, 1 and 2 are string . 

num1Int = int(num1) 
num2Int = int(num2) 
result = num1Int + num2Int
print("Result is ", result) # Now, If any user give value on num1 is 1 and num2 is 2 then the will show 3


num3 = int(input("Enter Third number :"))
num4 = int(input("Enter fourth number :"))
result2 = num3 + num4
print("Result2 is ", result2)