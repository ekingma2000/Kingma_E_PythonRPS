
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
	if gameVars.player_lives is 0:
		winlose.winorlose("lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("won")

	else:
		player =False
		gameVars.computer = gameVars.weapons[randint(0,2)]