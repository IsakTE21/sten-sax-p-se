import random

computer = random.choice(["rock", "paper", "scissors"])

user = input("rock, paper or scissors? ").lower()


# TODO - Implement the if statements that prints who wins


print("The computer chose", computer,"and the user chose", user +".")

if computer == user:
	print("Tie!")

elif computer == ("rock") and user == ("paper"):
	print("You won!")

elif computer == ("scissors") and user == ("paper"):
	print("You lost!")

elif computer == ("scissors") and user == ("rock"):
	print("You won!")

elif computer == ("paper") and user == ("rock"):
	print("You lost!")

elif computer == ("rock") and user == ("scissors"):
	print("You lost!")

elif computer == ("paper") and user == ("scissors"):
	print("You won!")




else:
	print("That is not a valid movement")
