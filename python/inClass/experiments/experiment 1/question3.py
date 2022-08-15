# A simple calculator program which accepts 2 numbers and then carries out a
# calculation on them?

number1=float(input("enter the first number : "))
number2=float(input("enter the second number : "))
print('''
Press 1 to add them.
Press 2 to subtract
Press 3 to divide
Press 4 to multiply them.
''')
operator = input('enter the operator : ')

if operator == '1':
    print(number1 + number2)
elif operator == '2':
    print(number1 - number2)
elif operator == '3' and number2 != 0:
    print(number1 / number2)
elif operator == '3' and number2 == 0:
    print('denominator can\'t be 0 :(')
elif operator == '4':
    print(number1 * number2)
else:
    print('betterluck next time :(')
