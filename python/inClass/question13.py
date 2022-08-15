# A 4 digit number is entered through keyboard. Write a program to print a new number
# with digits reversed as of orignal one

number = int(input('enter a 4 digit number : '))

reverse = (number%10)*1000 + (number%100 - number%10)*10 + (number%1000 - number%100)/10 + (number-number%1000)/1000


print('reverse of ',number , 'is : ',int(reverse))


# if 999 < number < 10000:
#     print('yes')
# else: 
#     print('no')