# n = number = input('enter the number : ')

# digits = [i for i in number]

all_possibilities = [] #['12345', "12345", '12453']

digits = ['1', '2']

def noOfPossibilities(digits): # factor of the number gives the number of possibilities
	no_of_possibilities = 1
	for i in range(1, len(digits)+1):
		no_of_possibilities *= i
	return no_of_possibilities


def possibilityGenerator(digits):
	number = ''
	for i in range(noOfPossibilities(digits)):
		number += digits[i]
	all_possibilities.append(number)

possibilityGenerator(digits)

print(all_possibilities)