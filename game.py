
# impirt the random package so we can generate a random AI choice
from random import randint

# "basket" of choices
weapons=["rock", "paper", "scissors"]
#start doing some logic and condition checking
computer=weapons[randint(0,2)]
player = False

while player is False:
	player=input("choose rock, paper or scissors: \n")

	print("computer: ", computer, "player:", player)
	#
	# start doing some logic and condition checking 
	# always chack a breaking condition first
	if player == computer:
		# we have a tie, mo point in going any further
		print("tie, no one wins! try again")

	elif player == "quit":
		print("you choose to quit, quitter.")
		exit()

	else:
		print("NOT a tie. Now we can check other conditions")
		if player =="rock":
			print("check and see wat the computer is, and win or lose")

	player =False
	computer = weapons[randint(0,2)]