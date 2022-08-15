# highest common factor

a = number1 = int(input('enter the first number to get lcm : '))
b = number2 = int(input('enter the second number to get lcm : '))

if a < b : 
    g = a
    h = b
else:
    g = b
    h = a

#shreyash's code
shreyasCode = 0
for i in range(1, g+1):
    shreyasCode += 1 # to find the number of loops
    if g%i == 0 and h%(g/i)==0:
        # print(g/i,' is the hcf')
        break
print("shreyasCode", shreyasCode)


#sir's code
sirCode = 0
for i in range(g, 0, -1):
    sirCode += 1 # to find the number of loops
    if a%i == 0 and b%i == 0:
        # print(i)
        break
print("sirCode",sirCode)

