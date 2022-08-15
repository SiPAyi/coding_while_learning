# # Write a program to check the person is major or not based on their age?
# # (If the age is greater than 18 then we call him/her major)

# age = int(input('hey can you enter your age : '))

# if age >= 18:
#     print('hey you are a major!!')
# else:
#     print('you are not a major!!')

# # Give two integer values from the keyboard or console, if 2 values are different then print
# # their sum. If 2 values are same then print double their sum

# number0 = int(input("enter first value : "))
# number1 = int(input("enter second value : "))

# if number0 == number2:
#     print(3*number1)
# else:
#     print(number0 + number2)

# # Take an integer from the keyboard or console and print the difference with 15.
# # If the entered number is greater than or equal to 15 then print double the difference

# number = int(input('enter a number : '))

# if number =< 15:
#     print(15 - number)
# else: 
#     print((number-15)*2)


# # Take 3 integers from the keyboard or console and print their sum If any of the
# # number is teen (example 13, 14, 16, 17, 18, 19) then that value counts as 0


# number1 = int(input('enter a number : '))
# number2 = int(input('enter a number again : '))
# number3 = int(input('enter a number and again : '))
# sum = number1 + number2 + number3

# if 12 < number1 < 20 : 
#     sum = sum - number1

# if 12 < number2 < 20 : 
#     sum = sum - number2

# if 12 < number3 < 20 : 
#     sum = sum - number3

# print(sum)


# # Given 3 int values, a b c, return their sum. However, if one of the values is the same as
# # another of the values, it does not count towards the sum

# a = int(input('enter a number : '))
# b = int(input('enter a number : '))
# c = int(input('enter a number : '))

# if a == b:
#     print(a+c)
# elif a == c:
#     print(a+b)
# elif a == b == c:
#     print(a)
# else:
#     print(a+b+c)


# # Ask the user to enter T or S or R. If the entered string is T then print formula of
# # the area of the triangle. If the entered string is S then print formula of the area of
# # the square. If it is R then print formula of the area of the rectangle.


# uInput = input('enter T or S or R : ')

# t = "0.5 * base * height"
# s = "side * side"
# r = "length * breadth"

# if uInput.lower() == 't':
#     print(t)
# elif uInput.lower() == 'r':
#     print(r)
# elif uInput.lower() == 's':
#     print(s)
# else:
#     print('no formula available!!')


# #Take any 3 numbers from the keyboard and print the biggest number.

# a = float(input('enter number : '))
# b = float(input('enter number : '))
# c = float(input('enter number : '))


# print(a,b,c)

# if a > b and a > c:
# 	print(a)
# elif b > a and b > c:
# 	print(b)
# else:
# 	print(c)


# # enerally we say leap year, if the year is divisible by 4 for normal years like 1976, 1788,
# # 2012 etc. If the years are like centuries 300,400,1300,1500,600,1800 etc then it should be
# # divisible by 400 then only we call the year as leap year


# year = int(input('enter year : '))

# # if year % 4 == 0:
# #     if year % 100 == 0 and year % 400 != 0:
# #         print('not leap year !!')
# #     else:
# #         print('leap year ')
# # else:
# #     print('not leap year')


# if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#     print('leap year')
# else:
#     print('not leap year!')



# # Write a program to display the last digit of a number and check it is divisible by 3 or not
# # (hint : any number % 10 will return the last digit)


# number = int(input('enter number : '))

# if number % 3 == 0 :
#     print('your number is divisible by 3')
# else: 
#     print('your number is not divisible by 3')

# print("last digit of number is ", number%10)


# # Write a program to accept a number from 1 to 7 and display the name of the day like 1 for
# # Sunday , 2 for Monday and so on

# day = int(input('enter the day number : '))

# if day == 1:
#     print('monday')
# elif day == 2:
#     print('tuesday')
# elif day == 3:
#     print('wednesday')
# elif day == 4:
#     print('thusday')
# elif day == 5:
#     print('friday')
# elif day == 6:
#     print('saturday')
# elif day == 7:
#     print('sonday')
# else :
#     print('Invalid input !!')


# # another way of doing this


# # days = ['monday','tuesday','wednesday','thusday','friday','saturday','sunday','invalid input']

# # if 1 < day < 7:
# #     print(days[day-1])
# # else:
# #     print(days[-1])


# # Write a program to accept two numbers and mathematical operators and perform
# # operation accordingly


# number1 = int(input('enter number : '))
# number2 = int(input('enter number : '))
# operator = input('enter the operator : ')

# if operator == '+':
#     print(number1 + number2)
# elif operator == '-':
#     print(number1 - number2)
# elif operator == '*':
#     print(number1 * number2)
# elif operator == '/':
#     print(number1 / number2)
# elif operator == '%':
#     print(number1 % number2)
# elif operator == '^':
#     print(number1 ** number2)



# # A 4 digit number is entered through keyboard. Write a program to print a new number
# # with digits reversed as of orignal one

# number = int(input('enter a 4 digit number : '))

# reverse = (number%10)*1000 + (number%100 - number%10)*10 + (number%1000 - number%100)/10 + (number-number%1000)/1000


# print('reverse of ',number , 'is : ',int(reverse))


# # to know it is a 4 digit number or not

# reverse = (number%10)*1000 + (number%100 - number%10)*10 + (number%1000 - number%100)/10 + (number-number%1000)/1000
# if 999 < number < 10000:
#     print('yes')
# else: 
#     print('no')