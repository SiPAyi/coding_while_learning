number = input('enter the number to check wether it is strong number or not : ')

sumOfFactorials = 0 

for letter in number:
    factorial = 1
    for i in range(1,int(letter)+1):
        factorial = factorial * i
        
    sumOfFactorials = sumOfFactorials + factorial
        
if int(number) == sumOfFactorials:
    print("bro it's a strong number bro!!")
else:
    print("broo it's not a strong number bro :) ")