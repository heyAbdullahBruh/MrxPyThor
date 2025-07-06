# Python have 2 types control statement 
# 1) Conditional control statement --> if,elif, else
# 2) loop control statement --> while , for 

# 1) Conditional control statement(CCS) ------->

# i)Normal CCS (if,else)-->
'''
if 60>40 :
    print('Correct')
else:
    print('Worng') 
'''   

# ii)CreateAMarkSheet and using elif-->

'''
marks = 30
if marks >= 80:
    print('A+') 
elif marks >= 70:
    print('A')
elif marks >= 60:
    print("A-")
elif marks >= 50:
    print('B+')
elif marks >= 40:
    print('C+')
elif marks >= 33:
    print('A+')
else:
    print('Failed')
'''
    
# iii) Inner if statement(nested conditional statement)-->

'''
userAge = 20
userClass =11

if userAge >19 :
    if userClass > 10:
        print("Praptoboyoska User")
    else :
        print("Boyos Beshi But choto class e pore")
else : 
    print("Choto Polapan")
'''

# iv) Ternary Operator ( short conditional statement)-->
'''
userAge = 12
userClass =11

result = "Praptoboyoska User" if userAge >18 else  "Choto Polapan"

print(result)
'''

# v) logical operator of conditional statement--> (and , or ,not)

'''
price =int(input("Enter Mal er price"))
rating =float(input("Enter Mal er Rating"))
delivary= int(input("Enter Delivary charge"))

if price <=50 and delivary ==0 and 4<= rating <=5:
    print('I will buy this Mal.')
else:
    print("I can't buy this Mal.")
'''
    
letter = input('Enter a letter')

if letter =='a' or letter =='e' or letter =='i' or letter =='o' or letter =='u' :
    print(f"The Letter {letter} is vowel.")
else :
    print(f"The Letter {letter} is consonant.")

