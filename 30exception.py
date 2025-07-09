# exception is error handler on python . 
# Python have 60 built in exception.

# One Have universal exception -->
try:
    num= float(input('Enter a number : '))
    division = 20/num

    print(division) 
except Exception as e : 
    print(f"{type(e).__name__}-->Message: {e}")
    
    
print("done")
