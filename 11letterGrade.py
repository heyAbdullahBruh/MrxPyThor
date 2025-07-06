# The Program make with conditional statement (if , else, elif)
from math import *

mathMarks = float(input("Enter Your Math Mark : "))
bioMarks = float(input("Enter Your Math Mark : "))
chemiMarks = float(input("Enter Your Math Mark : "))
physicsMarks = float(input("Enter Your Math Mark : "))

totalMarks =mathMarks + bioMarks + chemiMarks + physicsMarks

if 90<= mathMarks <=100 and 90<= bioMarks <=100 and 90<= chemiMarks <=100 and 90<= physicsMarks <=100 or 360<= totalMarks <=400 :
    print(f"You Got A+ and your Total Marks = {totalMarks}")
elif 70<= mathMarks <90 and 70<= bioMarks <90 and 70<= chemiMarks <90 and 70<= physicsMarks <90 or 280<= totalMarks <360 :
     print(f"You Got A and your Total Marks = {totalMarks}")
elif 50<= mathMarks <70 and 50<= bioMarks <70 and 50<= chemiMarks <70 and 50<= physicsMarks <70 or 200<= totalMarks <280 :
     print(f"You Got B and your Total Marks = {totalMarks}")
else : 
    print(f"You were failed and your Total Marks = {totalMarks}")
    
print("Math \tBio \tChemi \tPhysics")
print(f"{mathMarks} \t {bioMarks} \t {chemiMarks} \t {physicsMarks}")