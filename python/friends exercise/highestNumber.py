i = 0
greatestNumber = 0
while i < 10:
    number = int(input('enter the number : '))
    if number > greatestNumber:
        greatestNumber = number
    i = i+1

print(greatestNumber)