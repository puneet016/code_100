import random
roll_again="yes"
while roll_again=="yes":
   
   
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    print(f"You rolled a {dice1} and a {dice2}.")
    roll_again=input("Roll the dice again? (yes/no): ")
print("Thanks for playing!")

