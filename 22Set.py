# Set is unorderd collection of items,where there will no be any order(Don't access with any index number) . It's another data structure in Python .
# In Set can't store duplicate value . If do it then it's not returen . 
# 2 ways to define Set -> 1) curly brackes 2) Set Function. 
#  If set items are number then it's return a sorting number of SET, if that will define random way.

num1 ={3,8,2,1,4,6,7} #Define curly brackes
num2 =set([9,2,8,4,5,7,6,4]) # Define Set Function. 
'''
print(num1) #{1, 2, 3, 4, 6, 7}
print(num2) # {2, 4, 5, 6, 7, 8, 9} ; Cut duplicate

num1.remove(3) #remove 
num1.add(4)# add ; Note : If is it already have in set then it won't add in set.
num1.update([3])# it's similar of update
num2.discard(9) #it's similar of remove

print(3 in num2) #False
print(3 not in num2) #True
print(4 in num2) #True
'''


#Set oparations --->
#1) Union set --> Unionwork with combine multiple sets and checks which value are similer in those sets, then cut these similar value and store one value . and finaly it's return combine set. It define with | between sets
num3 ={11,8,2,22,44,45,7,6}

print(num1 | num2 |num3) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 11, 44, 45, 22}

#2) Intersaction Set -> it's return common value from multiple sets. It define with & between sets
print(num1 & num2 & num3) #{8, 2, 6, 7}

# 3) Defference set --> it's cut common value from 1st sets when 1st set compare with 2nd sets. It works , which set is define in print or result . Then It check 1st set with 2nd set and compare which value are similar 1st with 2nd then cut these value and return remaining value from 1st set.  It define with - between sets
print(num1 - num2 ) #{1, 3}
print(num2 - num1 ) #{9, 5}
