import random

def computerChoice():
	computerChoices = ["stone","paper","scissor"]
	getComputerChoice = random.choice(computerChoices)
	print(f"Computer Choice : {getComputerChoice}")
	return getComputerChoice

def userChoice():
	userChoices = input("User Choice! : ").lower()
	return userChoices

def gameRule(playUser,playComputer):
	#Draw Match
	if(playUser==playComputer):
		print("Match Draw")
	#User wins
	elif(playUser=="stone" and playComputer=="scissor"):
		print("User wins")
	elif(playUser=="scissor" and playComputer=="paper"):
		print("User wins")	
	elif(playUser=="paper" and playComputer=="stone"):
		print("User wins")
	#Computer wins
	elif(playUser=="stone" and playComputer=="paper"):
		print("Computer wins")
	elif(playUser=="scissor" and playComputer=="stone"):
		print("Computer wins")
	elif(playUser=="paper" and playComputer=="scissor"):
		print("Computer wins")
	else:
		print("Your Choice was incorrect")

	playAgain = input("Do you want to Play Again (yes/no) : ").lower()

	if playAgain=="yes":
		gameRule(playUser=userChoice(),playComputer=computerChoice())
	else:
		print("Bye see you Next time!")

gameRule(playUser=userChoice(),playComputer=computerChoice())