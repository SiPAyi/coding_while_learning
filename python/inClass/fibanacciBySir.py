firstNumber = 0
secondNumber = 1

latestNumber = 0

while latestNumber <= 10:
    print(latestNumber, end=' ')
    firstNumber = secondNumber
    secondNumber = latestNumber
    latestNumber = firstNumber + secondNumber
