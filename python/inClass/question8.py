#Take any 3 numbers from the keyboard and print the biggest number.

a = float(input('enter number : '))
b = float(input('enter number : '))
c = float(input('enter number : '))


print(a,b,c)

if a > b and a > c:
	print(a)
elif b > a and b > c:
	print(b)
else:
	print(c)
