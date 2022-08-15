##### For explanation purpose uncomment the print statements in the below code

number1 = int(input('enter the first number to get lcm : '))
number2 = int(input('enter the second number to get lcm : '))

lcm = 1

divisor = 2
while number1 > 1 or number2 > 1:
    if number1 % divisor == 0 and number2 % divisor == 0:
        lcm = lcm * divisor
        print(divisor, " | ", number1, number2)
        number1 = number1 // divisor
        number2 = number2 // divisor
        divisor = 2

    elif number1 % divisor == 0:
        lcm = lcm * divisor
        print(divisor, " | ", number1, number2)
        number1 = number1 // divisor
        divisor = 2
    elif number2 % divisor == 0:
        lcm = lcm * divisor
        print(divisor, " | ", number1, number2)
        number2 = number2 // divisor
        divisor = 2
    else:
        divisor += 1

print(lcm)


#shreyash's code
for i in range(1, number2):
	k = a*i
	if k%b==0:
		print(k, 'is the lcm')
		break

##### Defining a fuction here to get the list of multiples
# number1 = int(input('enter the first number to get lcm : '))
# number2 = int(input('enter the second number to get lcm : '))

# def factorizer(number):
#     list_of_multiples = []
#     divisor = 2
#     while number > 1:
#         if number % divisor == 0:
#             list_of_multiples.append(divisor)
#             number = number // divisor 
#             divisor = 2
#         else:
#             divisor += 1
#     return list_of_multiples

