# write a program to print all even numbers below 100 by using while loop

start = int(input('enter first number : '))
last = int(input('enter last number : '))

while start <= last:
    if start%2 == 0:
        print(start)
        start = start + 2
    else:
        print('yes')
        start = start + 1



