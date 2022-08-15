userInput = "nothing"

while userInput != quit:
	userInput = input("enter help to get information about the game :").lower()

	if userInput == "help" :
		print("start - to start the game \n end - to end the game \n quit - to quit the game ")
	elif userInput == "start" :
		print("game has started ")
	elif userInput == "end" :
		print("game has ended now ")
	elif userInput == "quit":
		print("you quit the game ")
		break
	else:
		print("I don't understand what are you talking about, you enter :", userInput)

