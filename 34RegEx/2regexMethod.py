# Import regex from re --->
import re 

# Method1 : match 
# Checks if the pattern matches from the start of the string. Useful for validation where pattern must be at beginning.-->
'''
pattern =r"Hellow"
if re.match(pattern,"Hellow I am a programmer , Hellow who are you ?") :
    print('Matched') 
else :
    print('not matched')
    '''

# Method2 -> search ;
# Searches for the first occurrence of the pattern anywhere in the string.
'''
pattern =r"Kutta"
if re.search(pattern,"Dog is a Kutta ,Kutta is best for our Env?") :
    print('Matched') 
else :
    print('not matched')
    '''
    
# Method2.5 -> search methode have 3methods of object ;1) .start() ,2).end(), 3) .span()
'''
pattern = "Flower"
matchP = re.search(pattern,"Rose is a most valuable Flower")
if matchP :
    print(matchP.start())# It's return Start index of matched pattern
    print(matchP.end())# It's return End index of matched pattern
    print(matchP.span())# It's return satrt and end index of matched pattern
else :
    print('not matched')
    '''

# Method3 -: findall
#Returns all non-overlapping matches as a list – great for extracting multiple matches.
'''
pattern =r"Kutta"
print(re.findall(pattern,r"Kutta is a most valo prani in our ENV! Kuttay eat every murgi")) #['Kutta', 'Kutta']
'''

# Method4 ->sub ;
# Replaces all matches of the pattern with another string – ideal for cleaning or formatting text.
# sub method accept three value , 1) pattern , 2) replace item 3) text

'''
pattern =r"Kutta"
text="Kutta is a most valo prani in our ENV! Kuttay eat every murgi"
replaceItem="Fox"
changeText = re.sub(pattern,replaceItem,text)
print(changeText) #Fox is a most valo prani in our ENV! Foxy eat every murgi
'''






