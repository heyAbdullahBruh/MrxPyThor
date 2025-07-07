#  File read and write with python --->

file = open('hello.txt','r+') 
'''
w=write file,r=read file , r+ = write / read files
'''
print(file.name) #hello.txt
print(file.writable()) #True

fileValues = file.read()
print(fileValues.split('\n')) # split file value by line
print(len(fileValues)) # get file length(character)

file.close()

