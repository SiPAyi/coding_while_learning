startingNumber = number = int(input('enter a number : '))

reversedNumber = 0 

# while number != 0:
#     reminder = number % 10
#     reversedNumber = reversedNumber * 10 + reminder
#     number = number//10

reversedNumber = str(number)[::-1] # as per sai kumars request

if startingNumber == int(reversedNumber):
    print("it's a polyndrom bro!!!",startingNumber,'=',reversedNumber)
else:
    print("it's not a polyndrom bro!!!",startingNumber,'!=',reversedNumber)
