x = int(input("Enter Your Number below 200:"))
match x:
    case 0:
        print("It's Zero")
    case _ if x == 0:
        print("It's more then zero ")
    case _ if x <0:
        print("It's less then zero")
    case _ if x == 100:
        print("It's 100")
    case _ if x < 100:
        print("It's less then 100")
    case _ if x > 100 and x < 200:
        print("It's more then 100")
    case _:
        print("Invalid Input",x)                       