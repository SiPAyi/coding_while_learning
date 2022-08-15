# print sum n natural numbers

nThNumber = int(input('enter number : '))

# print((n*(n+1))*0.5)

sum = 0

for i in range(1,nThNumber+1):
    sum = sum + i

print(sum)