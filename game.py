
# impirt the random package so we can generate a random AI choice
from random import randint
from gameFunctions import winlose, gameVars

# "basket" of choices



while gameVars.player is False:
	print("==================================================\n")
	print("Computer Lives", gameVars.computer_lives, "/", gameVars.total_lives)
	print("player Lives", gameVars.player_lives, "/", gameVars.total_lives)
	print("==================================================\n")
	print("choose your weapon")
	player=input("choose rock, paper or scissors: \n")

	print("computer: ", gameVars.computer, "player:", player)
	#
	# start doing some logic and condition checking 
	# always chack a breaking condition first
	if player == gameVars.computer:
		# we have a tie, mo point in going any further
		print("tie, no one wins! try again")

	elif player == "quit":
		print("you choose to quit, quitter.")
		exit()

	elif player == "rock":
		if gameVars.computer == "paper":
			print("You lose!", gameVars.computer, "covers", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1
		else:
			print("You win!", player, "smashes", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	elif player == "paper":
		if gameVars.computer == "scissors":
			print("You lose!", gameVars.computer, "cuts", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1

		else:
			print("You win!", player, "covers", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1
		
	elif player == "scissors":
		if gameVars.computer == "rock":
			print("You lose!", gameVars.computer, "smashes", player, "\n")
			gameVars.player_lives = gameVars.player_lives -1

		else:
			print("You win!", player, "cuts", gameVars.computer, "\n")
			gameVars.computer_lives = gameVars.computer_lives -1

	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")
		
		

	player =False
	gameVars.computer = gameVars.weapons[randint(0,2)]