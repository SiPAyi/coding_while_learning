# print factorial of a given number

nThNumber = int(input('enter number : '))

factorial = 1

for i in range(1,nThNumber+1):
    factorial = factorial * i

print(factorial)