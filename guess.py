import random
number=random.randint(1,9)
guess=int(input("Enter a number between 1 to 9"))
if(guess>number):
    print("Too high")
if(guess<number):
    print("Too low")
if(guess==number):
    print("Exactly correct")