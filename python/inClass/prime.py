# check the given number is prime number or not

number = int(input('enter number : '))

factor = 2

if number == 1:
    factor = 0
elif number == 2:
    factor = number
else:
    while factor < number:
        if number % factor == 0:
            factor = 0
            break
        else:
            factor += 1

if factor == number:
    print('prime')
elif factor == 0:
    print('not prime')