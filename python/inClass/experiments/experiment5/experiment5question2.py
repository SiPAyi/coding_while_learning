# # A. Given a dictionary, write a program to find the sum of all items in the dictionary
# items = {'telugu':36, 'english':36, 'maths':40, 'physics':37, 'chemistry':40, 'it':40}

# sum = 0
# for item in items:
#     sum += items[item]

# print(sum)


# B. write a program to merge two dictionaries using update() method.

dic_a = {1: 'sai', 2: 'sai', 3:'sai'}
dic_b = {4: 'sai', 5: 'sai', 6:'sai'}
updated = {}

for key in dic_a:
    updated.update({key:dic_a[key]})

for key in dic_b:
    updated.update({key:dic_b[key]})
     
print(updated)


# C. Write a program to enter names of employees and their salaries as input and store
# them in a dictionary

# employees_details = {}
# number_of_employees = int(input('How many employees details do you have : '))

# for i in range(number_of_employees):
#     name  = input('Enter employee name : ')
#     salary = int(input('Salary : '))
#     employees_details[name] = salary    

# print(employees_details)

