
# impirt the random package so we can generate a random AI choice
from random import randint

# "basket" of choices
weapons=["rock", "paper", "scissors"]

player_lives = 1
computer_lives = 1
#start doing some logic and condition checking
computer=weapons[randint(0,2)]
player = False

def winorlose(status):
	print("called win or lose", status)
	print("you", status, "! Would you like to play again")
	choice = input ("Y / N? ")

	if choice == "Y" or choice == "y":
		global player_lives
		global computer_lives
		global player
		global computer
 			#reset the game and start all over again
		player_lives = 1
		computer_lives = 1
		player = False 
		computer = weapons[randint(0,2)]

	elif choice == "N" or choice == "n":
			print("You chose to quit")
			exit()
	else: 
			print("Make a vaild Choice. Yes or No!!")

while player is False:
	print("==================================================\n")
	print("Computer Lives", computer_lives, "/1\n")
	print("player Lives", player_lives, "/1\n")
	print("==================================================\n")
	print("choose your weapon")
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

	elif player == "rock":
		if computer == "paper":
			print("You lose!", computer, "covers", player, "\n")
			player_lives = player_lives -1
		else:
			print("You win!", player, "smashes", computer, "\n")
			computer_lives = computer_lives -1

	elif player == "paper":
		if computer == "scissors":
			print("You lose!", computer, "cuts", player, "\n")
			player_lives = player_lives -1

		else:
			print("You win!", player, "covers", computer, "\n")
			computer_lives = computer_lives -1
		
	elif player == "scissors":
		if computer == "rock":
			print("You lose!", computer, "smashes", player, "\n")
			player_lives = player_lives -1

		else:
			print("You win!", player, "cuts", computer, "\n")
			computer_lives = computer_lives -1

	if player_lives is 0:
		winorlose("lost")
		# print("You lost! Loser. Would you like to play again?")
		# choice = input ("Y / N?")

		# if choice == "Y" or choice == "y":

		# 	player_lives = 1
		# 	computer_lives = 1
		# 	player = False 
		# 	computer = weapons[randint(0,2)]

		# elif choice == "N" or choice == "n":
		# 	print("You chose to quit")
		# 	exit()
		# else: 
		# 	print("Make a vaild Choice. Yes or No!!")


	elif computer_lives is 0:
		winorlose("won")
		# print("You Win. Would you lke to play again?")
		# choice = input ("Y / N?")

		# if choice == "Y" or choice == "y":

		# 	player_lives = 1
		# 	computer_lives = 1
		# 	player = False 
		# 	computer = weapons[randint(0,2)]

		# elif choice == "N" or choice == "n":
		# 	print("You chose to quit")
		# 	exit()
		# else: 
		# 	print("Make a vaild Choice. Yes or No!!")
		

	player =False
	computer = weapons[randint(0,2)]