import random

game_action = ["rock", "scissors", "paper"]

user_action = input("Enter your action: ")
comp_action = random.choice(game_action)

if user_action in game_action:


    print(f'your choice is {user_action} and computer action is {comp_action}')

    if user_action ==comp_action:
        print("your choice is the same as computer, therefore is a tie")

    elif user_action == "rock":
        if comp_action =="scissors":
            print("rock smashes scissors, you win!")
        else:
            print("paper covers rock, you lose!")

    elif user_action =="paper":
        if comp_action =="rock":
            print("paper covers rock, you win")
        else:
            print("scissors cut paper, you lose")

    elif user_action =="scissors":
        if comp_action =="paper":
            print("scissors cut paper, you win")
        else:
            print("rock smashes scissors, you lose")

else:
    print("invalid action")