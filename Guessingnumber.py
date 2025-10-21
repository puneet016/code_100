import math
import random
lower=int(input("Enter the lower bound: "))
upper=int(input("Enter the upper bound: "))
number_of_chances=math.log(upper-lower+1,2)
print(f"\n\tyou've only{number_of_chances} chance to guess the number\n")

generate_number=random.randint(lower,upper)
count=0
while count<number_of_chances:
    count+=1
    guess=int(input("Guess a number: "))
    if guess==generate_number:
        print(f"Congratulations you did it in {count} try")
        break
    elif guess<generate_number:
        print("You guessed too low")
    elif guess>generate_number:
        print("You Guessed too high")
if count>=number_of_chances:
    print(f"The number is {generate_number}")
    print("Better luck next time")