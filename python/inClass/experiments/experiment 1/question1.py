# Take 3 integers from the keyboard or console and print their sum If any of the
# number is teen (example 13, 14, 16, 17, 18, 19) then that value counts as 0.
# Example
# (1, 2, 3)-->6
# (7, 15, 5)-->27
# (2, 14, 11)-->13
# (5, 3, 19)-->8

number1 = int(input('enter the number : '))
number2 = int(input('enter the number : '))
number3 = int(input('enter the number : '))

sum = number1 + number2 + number3

if number1 in [13, 14, 16, 17, 18, 19]:
    sum = sum - number1
if number2 in [13, 14, 16, 17, 18, 19]:
    sum = sum - number2
if number3 in [13, 14, 16, 17, 18, 19]:
    sum = sum - number3

print(sum)
