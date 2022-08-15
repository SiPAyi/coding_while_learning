import random
guess_count = 0
guess_limit = 3
secretNumber = random.random(1,10)

while guess_count < guess_limit :
	guess = int(input("Guess : "))
	if secretNumber == guess:
		print("you won the match")
		break
	else:
		print("you entered a wrong number!!, please try again")
		guess_count += 1
print("done")
