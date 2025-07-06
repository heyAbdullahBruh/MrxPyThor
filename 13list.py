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

# 13)--->
student.remove("Pamal") # remove items from list
print(student) #['Salam', 'Balam', 'Kalam', 'Jalam', 'Samal', 'Kamal', 'Jamal', 'Bamal', 'Namal']

# 14)--->
student.sort() # sort list
print(student) #['Balam', 'Bamal', 'Jalam', 'Jamal', 'Kalam', 'Kamal', 'Salam', 'Samal']

number = [7,2,5,0,3,4,1,6]
number.sort()
print(number) #[0,1,2,3,4,5,6,7]

# 15)--->
student.pop() # CUT one items of value from last index of list 
print(student) #['Balam', 'Bamal', 'Jalam', 'Jamal', 'Kalam', 'Kamal', 'Salam']

# 16)--->
student2 = student.copy() # clear all of itmes from list
print(student2) #['Balam', 'Bamal', 'Jalam', 'Jamal', 'Kalam', 'Kamal', 'Salam']

# 17)--->
print(student.index("Kalam")) #5 ; it's get item index number in list

# 18)--->
student.clear() # clear all of itmes from list
print(student) #[]

# 19)--->
nums = [7,5,6,3,6,5,0,3,4,1,6]
print(nums.count(6)) # 3 ; it's return how many time have similar item in list, like 6 have three time in list . That's why it's return 3

'''

