
print("Welcome to the quiz game")
print("The total price is 15cr")
Q =["Q.What is the Capital of India","Q.What is the capital of America","Q.What is the capital of Germany","Q.What is the capital of France","Q.What is the capital of Italy"]
Ans =["Delhi","Washington","Berlin","Paris","Rome",]
price =[1,2,3,4,5]
total_price = 0
def quiz():
    for i in range(len(Q)):
        print(Q[i])
        a = input("Enter your answer:")
    if a == Ans[i]:
        total_price += price[i]
        print("You are right")
        print("You won", price[i], "cr")
    else:
        print("You are wrong")  
        print("You lost", price[i], "cr")
        print("Correct answer is", Ans[i])  
print("Total price is", total_price, "cr")