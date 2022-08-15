# Write a program to accept two numbers and mathematical operators and perform
# operation accordingly


number1 = int(input('enter number : '))
number2 = int(input('enter number : '))
operator = input('enter the operator : ')

if operator == '+':
    print(number1 + number2)
elif operator == '-':
    print(number1 - number2)
elif operator == '*':
    print(number1 * number2)
elif operator == '/':
    print(number1 / number2)
elif operator == '%':
    print(number1 % number2)
elif operator == '^':
    print(number1 ** number2)


