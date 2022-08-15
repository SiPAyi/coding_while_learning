# print factors of given number

number = int(input('enter number : '))

factor = 1

while factor <= number:
    if number%factor == 0:
        print(factor)
    factor = factor + 1