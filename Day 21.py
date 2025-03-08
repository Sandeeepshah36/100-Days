# ther is four type of function arguments
# 1. Required arguments
# 2. Keyword arguments
# 3. Default arguments
# 4. Variable-length arguments

# Required arguments
def add(a,b):
    return a+b
print(add(2,3))

# Keyword arguments
def sub(a,b):
    return a-b
print(sub(b=2,a=3))


# Default arguments
def mul(a=1,b=2):
    return a*b 
print(mul(2,3)) 

# Variable-length arguments
def div(*a):
    # print(type(a))
    sum=0
    for i in a:
        sum+=i
    return sum/2
print(div(2,3))    

