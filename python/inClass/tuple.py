#n = int(input('enter length'))
#t = ()
#for i in range(n):
#	a = int(input('enter value : '))
#	t = t + (a,)
#print(t)

#union of two tuples


a = (1, 2, 3, 4)
b = (1, 2, 4, 8)

c = a  + b


# d = ()
# print(c)
# for i in c:
# 	if i not in d:
# 		d = d + (i,)

# print(d)

for i in a:
	if (i in b) and (i not in c):
		c = c+(i,)
		
print(c)


# # swap variable
# a = 15
# b = 17

# a = a + b
# b = a - b
# a = a - b

# print(a, b)



# # program to store 
# t = ()
# n = int(input('enter number of emails : '))
# x = ()
# y = ()

# for i in range(n):
# 	a = input('enter your email id : ')
# 	t = t + (a,)
# 	k = a.split('@')
# 	x += (k[0],)
# 	y += (k[1],)

	
# print(t, '\n', x, '\n', y)

# # finding name in email
# x = input('enter the name to find : ')
# for i in t:
# 	if i.split('@')[0].find(x) != -1:
# 		print('name is found')
# 		break
# 	else:
# 		print('name not found')
	


# numbers = [23, 324, 3, 5]

# number_with_cubes = ()
# for number in numbers:
# 	cubes = (number, number**3)
# 	number_with_cubes += (cubes,)
	
# print('numbers,',numbers, '\nnumber_with_cubes',number_with_cubes)
