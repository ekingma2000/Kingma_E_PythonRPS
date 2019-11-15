# import the random package so we can generate a random AI choice
from random import randint
# Import the gameVars file
from gameFunctions import gameVars

def winorlose(status):
	print("\n\n\n")
	print("               * * * * * * * * * * * * * * * * * * * * * * * * * *")
	print("               *    You", status, "! Would you like to play again?     *")
	print("               * * * * * * * * * * * * * * * * * * * * * * * * * *\n\n\n\n\n\n\n\n\n\n\n")
	choice = input ("Y / N? ")

	if choice == "Y" or choice == "y":
 			#reset the game and start all over again
		gameVars.player_lives = 2
		gameVars.computer_lives = 2
		gameVars.player = False 
		gameVars.computer = gameVars.weapons[randint(0,2)]

	elif choice == "N" or choice == "n":
		print("\n\n\n\n\n\n\n")
		print("               * * * * * * * * * * * * * * * * * * * * * * * * *")
		print("               *      You Chose to Quit. Please Play Again!    *")
		print("               * * * * * * * * * * * * * * * * * * * * * * * * * \n\n\n\n\n\n\n\n\n\n\n")
		exit()
	else: 
		print("\n\n\n\n\n\n\n")
		print("               * * * * * * * * * * * * * * * * * * * * * * * * *")
		print("               *          Please input a Valid Choice!         *")
		print("               * * * * * * * * * * * * * * * * * * * * * * * * * \n\n\n\n\n\n\n\n\n\n\n")
			# recursion => calling a funtion from inside itself
		winorlose(status)