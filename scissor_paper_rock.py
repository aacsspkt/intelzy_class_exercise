import random

spr_dict = {
    "1": "Rock", 
    "2": "Paper", 
    "3": "Scissor",
}

def print_info():
    print("""
Choose one of the following:
1: Rock
2: Paper
3: Scissor
""")

def get_user_choice():
    user_input = None
    while user_input not in ["1", "2", "3"]:
        user_input = input("Enter your choice: ")
    user_choice = spr_dict[user_input]

    return user_choice

def check_winner(computer_choice, user_choice):
    if computer_choice == user_choice:
        print("It's a draw.")
        return
    
    if computer_choice == "Rock":
        if user_choice == "Scissor":
            result = "Lose"
        else:
            result = "Win"
    elif computer_choice == "Paper":
        if user_choice == "Rock":
            result = "Lose"
        else:
            result = "Win"
    else:
        if user_choice == "Rock":
            result = "Win"
        else:
            result = "Lose"

    if result == "Win":
        print("You win.")
    else:
        print("You lose.")


def ask_to_play_again():
    user_input = None
    while user_input not in ["y", "n"]:
        user_input = input("Do you want to play again? (y/n):")
    if user_input == "y":
        return True
    else:
        return False


play_again = True
while play_again:
    print_info()
    user_choice = get_user_choice()
    computer_choice = spr_dict[random.choice(list(spr_dict.keys()))]
    print("\nComputer choice: ", computer_choice)
    print("User choice: ", user_choice)
    check_winner(computer_choice, user_choice)
    play_again = False
    play_again = ask_to_play_again()

