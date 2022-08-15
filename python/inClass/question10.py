# Write a program to display the last digit of a number and check it is divisible by 3 or not
# (hint : any number % 10 will return the last digit)


number = int(input('enter number : '))

if number % 3 == 0 :
    print('your number is divisible by 3')
else: 
    print('your number is not divisible by 3')

print("last digit of number is ", number%10)