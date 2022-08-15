number = int(input('enter a number : '))
sum = 0

while number != 0:
    reminder = number%10
    sum += reminder
    number = number // 10
print(sum)