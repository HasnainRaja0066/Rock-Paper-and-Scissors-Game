import random
# This game is Snack Water Gun
computer = random.choice([-1, 0, 1])

you_str = input("Enter your choise: r p and s: ")

you_dict = {"r":1, "p":-1, "s":0}

reverse_dict = {1:"Rock", 0:"Scissors.", -1:"Paper"}
you = you_dict[you_str]

print(f"You chose {reverse_dict[you]}\nComputer chose {reverse_dict[computer]}")


if(computer==you):
    print("Game Draw")

elif(computer == -1 or you == 1):
    print("You Win!")

elif(computer == -1 or you == 0):
    print("You Lose!")

elif(computer == 0 or you == -1):
    print("You Win!")

elif(computer == 0 or you == 1):
    print("You Lose!")

elif(computer == 1 or you == -1):
    print("You Lose!")

elif(computer == 1  or you == 0 ):
    print("You Lose!")