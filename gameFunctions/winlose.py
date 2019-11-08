from random import randint
from gameFunctions import gameVars

def winorlose(status):
	print("called win or lose", status)
	print("you", status, "! Would you like to play again")
	choice = input ("Y / N? ")

	if choice == "Y" or choice == "y":
 			#reset the game and start all over again
		gameVars.player_lives = 1
		gameVars.computer_lives = 1
		gameVars.player = False 
		gameVars.computer = gameVars.weapons[randint(0,2)]

	elif choice == "N" or choice == "n":
			print("You chose to quit")
			exit()
	else: 
			print("Make a vaild Choice. Yes or No!!")
			# recursion => calling a funtion from inside itself
			winorlose(status)