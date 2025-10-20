import random

def select_cpmputer_action():
    actions=["rock","paper","scissors"]
    return random.choice(actions)


while True:
    user_action=input("Enter a choice (rock, paper, scissors): ")
    
    computer_action=select_cpmputer_action()
    print(f"\nYou chose {user_action}, computer chose {computer_action}.\n")
    if user_action==computer_action:
        print(f"Both players selected {user_action}. It's a tie!")
    elif user_action=="rock":
        if computer_action=="scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_action=="paper":
        if computer_action=="rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    elif user_action=="scissors":
        if computer_action=="paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissors! You lose.")
    else:
        print("Invalid input! Please choose rock, paper, or scissors.")
    play_again=input("Play again? (yes/no): ")
    if play_again()!="yes":
        break
print("Thanks for playing!")