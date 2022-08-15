student = {
	'name' : 'sai',
	'age' : 17,
	'id' : 'ro200174'
}

print(student)

print('name of the student', student['name'])

#modifying the values of a key
student['name'] = 'sadanand'

print(student['name'])

# adding key value pair to the dictionary
student['phoneNumber'] = 9340739487
print(student['phoneNumber'])

print('name of the student', student.get('Name'))

#if the argument doesn't work we give the another default value sai
print('name of the student', student.get('Name',"sai"))

# to prevent the below error we used the get method
print('to prevent the below error we used the get method in the 2nd above line')

print('name of the student', student['Name'])

