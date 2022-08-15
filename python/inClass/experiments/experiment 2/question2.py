# . Write a sand glass pattern program in python by using nested loops?

for i in range(5):
	for j in range(i):
	    	print(' ', end='')
	for k in range(5-i):
		print('o ', end='')
	print()
for i in range(1,5):
	for j in range(4-i):
		print(' ', end='')
	for k in range(i+1):
		print('o ', end='')
	print()
