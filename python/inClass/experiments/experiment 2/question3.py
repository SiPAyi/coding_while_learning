# .Write a program that takes input 1, 2, and 0
# if you enter 1 then it will ask to enter any number to find that, given number is a
# palindrome or not?(Hint: use while loop and take temp variable)
# If you enter 2 then it will ask to enter any number and check whether it is Armstrong
# Number or not? (Hint: use while loop and take temp variable)
# To stop this program you should give input as 0, otherwise program should keep
# running.
# If you enter other input values. It must display “enter valid input and try again”


while True:
    choice = input('Enter a number among 1, 2, and 0 : ')

    if choice == '1':
        number = input('Enter any positive number to find palindrome or not : ')
        if number == number[::-1]:
            print(number, 'is a polindrom number ')
        else:
            print(number, 'is not a polindrom number ')

    elif choice == '2':
        number = input("Enter any positive number to find Armstrong Number or not : ")
        sum = 0
        for digit in number:
            sum += int(digit)**len(number)
        if sum == int(number):
            print(number, 'is a amstrong number')
        else: 
            print(number, 'is not a amstrong number ')
    elif choice == '0':
        print('good bye!!!')
        break
    else:
        print('enter a valid number :( ')
    print()
    
    
    
    
    
