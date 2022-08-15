# Given 3 int values, a b c, return their sum. However, if one of the values is the same as
# another of the values, it does not count towards the sum

a = int(input('enter a number : '))
b = int(input('enter a number : '))
c = int(input('enter a number : '))

if a == b:
    print(a+c)
elif a == c:
    print(a+b)
elif a == b == c:
    print(a)
else:
    print(a+b+c)