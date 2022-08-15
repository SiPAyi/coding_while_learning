# A. write a python program to find the maximum number of three numbers by using
# Functions

numbers_list = [1, 23, 23, 2424, 983]
def largest(numbers_list):
    largest = 0
    for number in numbers_list:
        if number > largest:
            largest = number
    return largest
print(largest(numbers_list))


# B. write a python program to calculate the Two numbers addition, subtraction,
# multiplication and division by using Functions

a = 5
b = 10

def addition(a, b):
    return a + b

def substraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    return a / b

print(addition(a, b), substraction(a, b), multiplication(a, b), division(a, b))