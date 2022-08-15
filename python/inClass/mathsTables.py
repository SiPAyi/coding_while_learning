# to print multiplication table of a given number up to 10 times


number = int(input('enter number : '))
times = int(input('how many times do you want : '))

for i in range(1,11):
    print(number, "*", i, '=', number*i)
