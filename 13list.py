# Python list are similar of Array.---> ['print','hellow','eere',3,4]

student =["Salam","Balam","Kalam","Jalam",'Samal','Kamal','Jamal',"Bamal"]

'''
# 1)--->
print(student) # ['Salam', 'balam', 'Kalam', 'Jalam', 'Samal', 'Kamal', 'Jamal', 'Bamal']

# 2)--->
print(student[1]) # Balam

# 3)--->
# print(student[2:]) # ['Kalam', 'Jalam', 'Samal', 'Kamal', 'Jamal', 'Bamal']

# 4)--->
print(student[-1]) # Bamal ; Return Last of idx value

# 5)--->
print("Tamal" in student) # False ; Bcz, Tamal Haven't in student list

# 6)--->
print("Jalam" in student) # True ; Bcz, Tamal Have in student list

# 7)--->
print("Tamal" not in student) # True ; Bcz, Tamal Haven't in student list

# 8)--->
print(student + ["Tamal", "Gamal"]) # add items with list

# 9)--->
print(student * 3) # return every items 3 times . Like --> ['Salam', 'Balam', 'Kalam', 'Jalam', 'Samal', 'Kamal', 'Jamal', 'Bamal', 'Salam', 'Balam', 'Kalam', 'Jalam', 'Samal', 'Kamal', 'Jamal', 'Bamal', 'Salam', 'Balam', 'Kalam', 'Jalam', 'Samal', 'Kamal', 'Jamal', 'Bamal']

# 10)--->
print(len(student)) #8 ; It's Return length of List.

# 11)--->
student.append("Namal") #add one items on last value in list 
print(student) # ['Salam', 'Balam', 'Kalam', 'Jalam', 'Samal', 'Kamal', 'Jamal', 'Bamal', 'Namal']
# 12)--->
student.insert(3,"Pamal") # insert a item in specific index in list 
print(student) #['Salam', 'Balam', 'Kalam', 'Pamal', 'Jalam', 'Samal', 'Kamal', 'Jamal', 'Bamal', 'Namal']


'''

# 13)--->
student.sort() # sort list
print(student) #['Balam', 'Bamal', 'Jalam', 'Jamal', 'Kalam', 'Kamal', 'Salam', 'Samal']

# 13)--->
student.remove("Bamal") # remove items from list
print(student) #['Salam', 'Balam', 'Kalam', 'Jalam', 'Samal', 'Kamal', 'Jamal', 'Bamal', 'Namal']
