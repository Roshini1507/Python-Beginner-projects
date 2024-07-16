import random

user_score=0
computer_score=0

possible_actions = ["rock", "paper" , "scissors"]

while True:
    user_action= input("Type Rock/paper/scissors or q to quit : ").lower()
    if user_action.upper()=="Q":
       break
    
    if user_action not in ["rock" , "paper", "scissors"]:
        print("Invalid Input!")

    random_numbers=random.randint(0,2)
    # rock:0 , paper:1 , scissors:2
    computer_action = possible_actions[random_numbers]
    print(f"computer picked {computer_action}.")

    if user_action == computer_action:
        print("It's a tie!")
    elif user_action == "rock" and computer_action == "scissors":
        print("You won!")
        user_score+=1
    elif user_action == "paper" and computer_action == "rock":
        print("You won!")
        user_score+=1
    elif user_action == "scissors" and computer_action == "paper":
        print("You won!")
        user_score+=1
    else:
        print("You Lost!")
        computer_score+=1



print(f"You won {user_score} times.")
print(f"The computer won {computer_score} times.")
print("Good Byee!")