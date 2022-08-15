primes = 0 
currentNumber = 1
noOfPrimes = int(input('how many prime do you want : '))
while primes < noOfPrimes:
    factors = 0 
    for j in range(1, currentNumber+1):
        if currentNumber% j == 0 :
            factors += 1
    if factors == 2:
        print(currentNumber)
        primes = primes + 1 

    currentNumber = currentNumber + 1
