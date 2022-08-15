number = int(input('enter a number : '))

reversedNumber = 0 

while number != 0:
    reminder = number % 10
    reversedNumber = reversedNumber * 10 + reminder
    number = number//10
print(reversedNumber)  

#another method
# print(str(number)[::-1])


#another method
# for i in range(1,len(str(number))+1)

