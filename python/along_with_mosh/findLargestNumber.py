# numbers = [2, 23, 234 , 5, 13, 141 , 13, 42 ,34]

		
def findLargest(numbersList):
	largestNumber = 0

	for number in numbersList:
		if largestNumber < number:
			largestNumber = number
	return largestNumber
	
		
