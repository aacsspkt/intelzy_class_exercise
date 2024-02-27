import random

spr_dict = {
    "r": "Rock",
    "p": "Paper",
    "s": "Scissor"
}
value = spr_dict["p"]
def print_info():
    print("""
Choose one of the following:
r: Rock
p: Paper
s: Scissor
""")

def get_user_choice():
    user_input = None
    while user_input not in list(spr_dict.keys()):
        user_input= input("Enter your choice: ")
    user_choice = spr_dict[user_input]
    return user_choice


def check_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("It's a draw!")
        return
    
    if computer_choice == "Rock":
        if user_choice == "Paper":
            print("You win!")
        else:
            print("You lose!")
    elif computer_choice == "Paper":
        if user_choice == "Scissor":
            print("You win!")
        else:
            print("You lose!")
    else:
        if user_choice == "Rock":
            print("You win!")
        else: 
            print("You lose!")

def ask_to_play_again():
    ans = None
    while ans not in ["y", "n"]:
        ans = input("Do you want play again? (y/n):")
    if ans == "y":
        return True
    else:
        return False

play_again = True
while play_again: 
    print_info()
    user_choice = get_user_choice()
    computer_choice = spr_dict[random.choice(list(spr_dict.keys()))]
    print("user choice:", user_choice)
    print("computer choice:", computer_choice)
    check_winner(user_choice, computer_choice)
    play_again = ask_to_play_again()