originalList = [3, 4, 3, 6, 6, 3, 7, 8 ,9 ,34 , 55]

uniques = []


print('original list :',originalList)

for number in originalList:
	if number not in uniques:
		uniques.append(number)
		
print('after removing all duplicates',uniques)



