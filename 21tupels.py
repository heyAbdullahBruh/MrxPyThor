# Tuples is a python data structure that similar of python list data structure. 
# List's data can be change but tuples data cann't be change . 
# List start with [] and tupels start with ()

workers =(
    "Shamim", "Tamim","Bamim","Damim","Shakib","Thakib","Jhakib"
)

print(workers) #('Shamim', 'Tamim', 'Bamim', 'Damim', 'Shakib', 'Thakib', 'Jhakib')
print(workers[1]) #Tamim

# workers[3]='Namim' # ❌

# print(workers) # give a error -> 'tuple' object does not support item assignment

for x in workers:
    print(x)

eployees=(
    ("Jihad",18,20000),
    ("Khihad",34,50000),
    ("Sihad",28,35000),
    ("Lohad",58,100000),
    "Nihad",
    'Bihad'
)
print(eployees[1][1]) #34    

for x in eployees:
    print(x)
