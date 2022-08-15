matrix1 = [
	[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9],
	[1, 2, 3]
	]

matrix2 = [
	[1, 2, 3], 
	[4, 5, 6], 
	[7, 8, 9]
	]


def product(matrix1, matrix2):
	m1r = len(matrix1)
	m1c = len(matrix1[0])
	m2r = len(matrix2)
	m2c = len(matrix2[0])
	
	if m1r == m2c:
		product = []
		for k in range(m1r):
			row = []
			for i in range(m1r):
				#below code for one element of product matrix
				sum = 0
				for j in range(m1c):
					sum += matrix1[k][j] * matrix2[j][i]
				row.append(sum)
			product.append(row)
	else:
		print('we cant do this')
	return product
print(product(matrix1, matrix2))
