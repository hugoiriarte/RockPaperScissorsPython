"""
Program: rockpapersic.py
Author: Hugo
"""
#Imports random
import random

#asks user for there name
userName = input("Hello user!\nWhat is your first name >>>")

#ask user if they want to play
userPlay = input("Hello," + userName + "\nWould you like to play rock, paper, scissors? \nEnter (Y) for yes or (N) for no >>>")

#array list of possible choices
arrayList = ["r", "p", "s"]

	#loop that runs as long as the user inputs y
while(userPlay.lower() == "y"):

	#picks a random choice from the arrayList 
	randomPick = random.choice(arrayList)
			
	#asks player what they want to play
	playerPick = input("Choose from the following:\n(R) for rock\n(P) for paper\n(S) for scissors >>>")
			
	#If statements that compares the user input and the random choice from the arrayList
	if playerPick.lower() == "r"  and randomPick == "r":    
		print("The game has ended in a tie, computer has chosen rock as well")
		userPlay = input("play again (Y) or (N)")
				
	elif playerPick.lower() == "r" and randomPick == "p":
		print("You have lost! Computer has chosen paper")
		userPlay = input("play again (Y) or (N)")
				
	elif playerPick.lower() == "r" and randomPick == "s":
		print("You won ! Computer has chosen scissors")
		userPlay = input("play again (Y) or (N)")
				
	elif playerPick.lower() == "p" and randomPick == "r":
		print("You have won! Computer has chosen rock")
		userPlay = input("play again (Y) or (N)")
				
	elif playerPick.lower() == "p" and randomPick == "s":
		print("You have lost! Computer has chosen scissors")
		userPlay = input("play again (Y) or (N)")
				
	elif playerPick.lower() == "p" and randomPick == "p":
		print("The game has ended in a tie, computer has chosen paper as well")
		userPlay = input("play again (Y) or (N)")
				
	elif playerPick.lower() == "s" and randomPick == "r":
		print("You lost! Computer has chosen rock")
		userPlay = input("play again (Y) or (N)")
				
	elif playerPick.lower() == "s" and randomPick == "p":
		print("You won! Computer has chosen paper")
		userPlay = input("play again (Y) or (N)")
				
	elif playerPick.lower() == "s" and randomPick == "s":
		print("The game has ended in a tie, computer has chosen scissors as well")
		userPlay = input("play again (Y) or (N)")