#  Count sentence element--->

sentence = input("Enter your sentence : ")

wordsNum =1
letterNumb =0
digitNumb =0

for x in sentence :
    capX = x.lower()
    if "a"<= x <="z" :
        letterNumb = letterNumb +1
    elif "0"<= x <="9" :
        digitNumb = digitNumb +1
    elif  x ==" " :
        wordsNum = wordsNum +1
print(f"LetterNumber = {letterNumb}\n Digit Number = {digitNumb} \n Word Number : {wordsNum}")

# Hello I'm abdullah. I 17 years old gay. Result : ---> 
# LetterNumber = 24
# Digit Number = 2
# Word Number : 8