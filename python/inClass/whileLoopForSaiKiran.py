Number = int(input('enter the number to check it is prime or not : '))
    
factors = 2

divisor = 2

while divisor < Number:
    reminder = Number % divisor
    if reminder == 0:
        factors = factors + 1
        break
    else:
        divisor = divisor + 1

if factors == 2:
    print('prime')
else:
    print('not a prime')










