# check the given number is perfect square or not

number = int(input('enter the number to check it is prime or not : '))

# sir's method

for i in range(1, number):
    if i*i == number:
        print('it is perfect')
        break
else:
    print('not a perfect square')


# my method