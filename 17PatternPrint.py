# Pattern printing 

# 1) Pattern printing--->

n=int(input('Enter a number that show how time pattern : '))

for i in range(n+1):
    print(i*"*")
#     """
#     n=3 --> *     
#             **   
#             *** 
#     n=5 --> *    
#             **   
#             ***  
#             **** 
#             *****
#     """

# 2) Pattern printing--->
for i in range(n+1):
    print(((2*i)-1)*"*")
# """
#     n=3 --> *           
#             ***        
#             *****     
#     n=5 --> *        
#             ***      
#             *****    
#             *******  
#             *********
#     """