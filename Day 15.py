import time

T = time.strftime('%H:%M')
print(T)
H = int(time.strftime('%H'))
print(H)
M = int(time.strftime('%M'))   
print(M)


if int(H) < 12:
    print("Good Morning")
elif int(H) >= 12 and int(H) < 16:
    print("Good Afternoon")
elif int(H) >= 16 and int(H) < 20:
    print("Good Evening")
else:
    print("Good Night")  
