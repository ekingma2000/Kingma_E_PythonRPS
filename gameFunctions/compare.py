# import the random package so we can generate a random AI choice
from random import randint
# Import the gameVars file
from gameFunctions import gameVars, winlose


def compareChoices(player):

	if player == gameVars.computer:
		
		print("                You Tied. You Must Have The Mind of a Computer!")

	elif player == "quit":
		print("\n\n\n\n\n\n\n")
		print("               * * * * * * * * * * * * * * * * * * * * * * * * *")
		print("               *      You Chose to Quit. Please Play Again!    *")
		print("               * * * * * * * * * * * * * * * * * * * * * * * * * \n\n\n\n\n\n\n\n\n\n\n")
		exit()

	elif player == "rock":
		if gameVars.computer == "paper":
			print("                         You Lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("                         You Win!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print("                         You Lose!", gameVars.computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1

		else:
			print("                         You Win!", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
		
	elif player == "scissors":
		if gameVars.computer == "rock":
			print("                         You Lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1

		else:
			print("                         You Win!", player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	
		