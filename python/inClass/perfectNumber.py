# check the given number is perfect square or not
#sum of its factors is equal to that number

number = int(input('enter number : '))

factor = 1
sumOfFactors = 0

while factor <= number:
    if number%factor == 0:
        sumOfFactors = sumOfFactors + factor
    
    if sumOfFactors == number:
        print(number,' is a perfect number')
        break
    factor = factor + 1


