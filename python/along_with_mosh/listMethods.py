numbers = [13,5,2,13,7,4]

print(numbers)
#to insert in the end of a list
numbers.append(13)
print('13 added at last',numbers)

# to insert in the middle of the list
numbers.insert(2,45)
print('45 added at 3rd position',numbers)

#removing items
numbers.remove(13) #it removes the first items you gave
print('13 is removed from the list', numbers)

#removing last item from the list
numbers.pop()
print('the last item is removed now ', numbers)

#to sort the list
print('the sorted list is here :', numbers.sort(),numbers) # the first argument doesn't give the sorted list because it's sorted the list not printing the list
numbers.reverse() # this will reverse the list
print('the reverse sorted list is here :', numbers)

#copying a list to another list
numbers_copy = numbers.copy()
print('this is the copy of numbers list : ' , numbers_copy)


# to know the index value of a item
print('index value of 5',numbers.index(5)) #it only gives the index value of first occurence

# to check wether a value is in the list or not
print('we checked wether 50 is in the list or not, so the answer is ', 50 in numbers)

#to check the number of occurences of an item
print(f'13 is occured {numbers.count(13)} time')

#clear a list
numbers.clear()
print('after using clear method',numbers)


