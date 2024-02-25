import random

print("******************* Number guessing game *******************")
list = [i for i in range(1, 11)]

# shuffle given list randomly
# random.shuffle(list)
# print("list", list)

rand_choice = random.choice(list)
# print("random #:", rand_choice)
guessed_num = -1
while guessed_num != rand_choice:
    guessed_num = int(input("Enter you guess #: "))

    if guessed_num > rand_choice:
        print("To high!")
    elif guessed_num < rand_choice:
        print("To low!")
    else:
        print("Equal")

print("You guessed right! The number is ", rand_choice)

