#  Coin Toss Guessing game using random methods.

import random


print(
     "Welcome to the coin Guessing Game!\n"
     " Choose a methode to toss the coin:\n "
     " 1. Using random.random()\n"
     " 2. Using random.randint()\n"
    )
#chose methode
user=input("Enter your choise between (1 or 2 ):\n")

guess=input("Enter your Guess (Heads or Tails)\n")

if user == "1":
    toss="heads" if random.random()< 0.5 else "tails"

elif user == "2":
    toss="heads " if random.randint(0,10)==5 else "tails"

if guess== toss:
    print(f"Great! you won the coin was: {toss}\nn")
else:
    print(f"Sorry, you lost. The coin was : {toss}\n")    
        

