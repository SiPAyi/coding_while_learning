# Write a program to store the detail ( Roll number, Name, Section) of n number of
#  student in a tuple. Accept all data from the user.
#  Output:
#  ((1, 'Rahul', 'B'), (2, 'Vijay', 'C'), (3, 'seetha', 'A'), (4, 'cherly', 'D')) 

number_of_students = int(input('How many student details do you have : '))

students = ()

for i in range(number_of_students):
    roll_number = int(input("Enter student's Roll number : "))
    name = input("Enter student's name : ")
    section = input("Enter student's section : ")
    students += ((roll_number, name, section),)
    print()


print(students)