
n =int(input("Enter n number : "))

# 1) 1 +2+3+4+.....+n
'''
sum =0
for i in range(1,n+1,1):
    sum = sum +i
print(sum)
'''

# 2) 2 +4+6+8+.....+n
'''
sum =0
for i in range(2,n+1,2):
    sum = sum +i
print(sum)
'''

# 3) 1+3+5+7+9+.....+n
'''
sum =0
for i in range(1,n+1,2):
    sum = sum +i
print(sum)
'''

# 4) 1^2+2^2+3^2+4^2+5^2+.....+n^2
'''
sum =0
for i in range(1,n+1,1):
    sum = sum +i**2
print(sum)
'''

# 5) 1^3+2^3+3^3+4^3+5^3+.....+n^3
'''
sum =0
for i in range(1,n+1,1):
    sum = sum +i**3
print(sum)
'''

# 6) 1+1/2+1/3+1/4+1/5+1/6.....+1/n
'''
sum =0
for i in range(1,n+1,1):
    sum = sum +1/i
print(sum)
'''

# 7) 1*2*3*4*.....*n

'''
sum =1
for i in range(1,n+1,1):
    sum = sum *i
print(sum)
'''

# 8) 2*4*6*8*.....*n
'''
sum =1
for i in range(2,n+1,2):
    sum = sum *i
print(sum)'''

# 9) 1^2 X 2^2 X 3^2 X 4^2 X 5^2 X.....Xn^2
"""
sum =1
for i in range(1,n+1,1):
    sum = sum * i**2
print(sum)
"""

# 10) Factorial n! --->
'''
sum =1
for i in range(n,1,-1):
    sum = sum *i
print(sum)
'''

# 11) Prime number --->

for i in range(2,n+1,1):
    if n%i != 0:
        print(f"This is Prime Number {i}")
    else :
        print(f"This is not Prime Number {i}")
        

