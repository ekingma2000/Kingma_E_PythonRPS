
# import the random package so we can generate a random AI choice
from random import randint
# Import the winlose, gameVars, and compare files
from gameFunctions import winlose, gameVars, compare

while gameVars.player is False:
	print("\n\n")
	print("                * * * * * * * * * * * * * * * * * * * * * * * * * \n")
	print("                *              Computer Lives", gameVars.computer_lives, "/", gameVars.total_lives,"            *\n")
	print("                *               Player Lives", gameVars.player_lives, "/", gameVars.total_lives,"             *\n")
	print("                * * * * * * * * * * * * * * * * * * * * * * * * * \n\n\n")
	print("                               choose your weapon      \n")
	player=input("                          rock, paper or scissors: ")

	print("               * * * * * * * * * * * * * * * * * * * * * * * * * \n")
	print("\n                         computer: ", gameVars.computer, "player:", player)
	print("               * * * * * * * * * * * * * * * * * * * * * * * * * \n")
	
	compare.compareChoices(player)

	if gameVars.player_lives is 0:
		winlose.winorlose("Lost")

	elif gameVars.computer_lives is 0:
		winlose.winorlose("Won")

	else:
		gameVars.player =False
		gameVars.computer = gameVars.weapons[randint(0,2)]