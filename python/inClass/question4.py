# Take 3 integers from the keyboard or console and print their sum If any of the
# number is teen (example 13, 14, 16, 17, 18, 19) then that value counts as 0


number1 = int(input('enter a number : '))
number2 = int(input('enter a number again : '))
number3 = int(input('enter a number and again : '))
sum = number1 + number2 + number3

if 12 < number1 < 20 : 
    sum = sum - number1

if 12 < number2 < 20 : 
    sum = sum - number2

if 12 < number3 < 20 : 
    sum = sum - number3

print(sum)
