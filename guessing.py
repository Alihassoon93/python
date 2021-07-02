import random

guesses = 0
random_num =  random.randint(0,100)

while guesses < 10:
	
	guessed_num = int(input("Enter random number: "))

	if guessed_num == random_num:
		print("You Won")
		break
	elif guessed_num < random_num:
		print("Guess is Low")
	else:
		print("Guss is High")

	guesses += 1


