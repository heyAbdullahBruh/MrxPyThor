# Python Dictionary --> Dictionary is a important data structure in Python . 
# It's work with key =value pair . 

student ={
    'name' :'Syful',
    'age':29,
    'classN':11,
    'isActive' : False
}

print(student) #{'name': 'Syful', 'age': 29, 'classN': 11, 'isActive': False}
print(student['name']) #Syful

student['age'] = 21
print(student) #{'name': 'Syful', 'age': 21, 'classN': 11, 'isActive': False}

print(student.get('isActive')) #False

# print(student['sallray']) # Give a error 
print(student.get('sallray')) # None
print(student.get('sallray',"Don't have any value under the key")) # Don't have any value under the key

