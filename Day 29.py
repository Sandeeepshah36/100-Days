# Docstring
def add(a,b):
    """This function adds two numbers and returns the result"""
    return a+b
print(add(10,20))
print(add.__doc__)
print(type(add.__doc__))
