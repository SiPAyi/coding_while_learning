# Python Program to Print Largest Even and Largest Odd Number in a List.
#  Accept all data from the user

number_of_terms = int(input('how many numbers do you have : '))

numbers = []

for i in range(number_of_terms):
    try:
        number = int(input('enter the item : '))
        numbers.append(number)
    except ValueError:
        # do not add this input to the numbers list
        continue

largest_odd = 0
largest_even = 0

for number in numbers:
    print(number)
    if number % 2 == 0 and number > largest_even:
        largest_even = number
    elif number % 2 != 0 and number > largest_odd:
        largest_odd = number
    else:
        continue

print("largest_odd", largest_odd, "largest_even", largest_even)