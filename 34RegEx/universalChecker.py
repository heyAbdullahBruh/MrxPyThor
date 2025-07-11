import re

def matchResult(pattern,text) :
    if re.match(pattern,text):
        print(f"{text} is a valid format")
    else : 
        print(f'{text} is not a valid format')
