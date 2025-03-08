b=0 #This is while loop
while b<3:
    b+=1  
    for i in range(0, 6): #This is for loop
        a = int(input("Enter a number:")) #This is if else statement
        if a > 0:
            print("Number is positive")
        elif a == 0:
            print("Number is zero")
        else:
            print("Number is negative")        